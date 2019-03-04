# coding:utf-8
from django.shortcuts import render  # render用于渲染模板
from . import models
from django.shortcuts import redirect  # 重定向
from . import forms
import hashlib  # 密码加密
from django.http import HttpResponse


# Create your views here.


def hash_code(s, salt='@liyi'): # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接受bytes
    return h.hexdigest()  # 加密后的十六进制序列


def index(request):
    """首页视图"""
    category = ['计算机', '数学', '英语', '文学', '金融', '管理', '工程', '其他']
    book_list = models.Books.objects.all()[:20]  # 返回数据库前20个对象
    return render(request, 'shopstore/index.html', locals())


def login(request):
    """登录视图"""
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '填写有误！'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = '密码不正确'
            except:
                message = '用户不存在'
        return render(request,'shopstore/login.html', locals())
    login_form = forms.UserForm()
    # locals()是python内置的一个函数，可以返回当前所有本地变量字典
    return render(request, 'shopstore/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态下不允许注册
        redirect('/index/')
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = '填写有误'
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            if password1 != password2:
                message = '两次输入的密码不一样'
                return render(request, 'shopstore/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user: # 有用户使用此用户名
                    message = '用户名已存在'
                    return render(request, 'shopstore/register.html')
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '邮箱已被注册'
                    return render(request, 'shopstore/register.html', locals())
            # 所有判断完成之后，创建新用户
            new_user = models.User()
            new_user.name = username
            new_user.password = hash_code(password1)
            new_user.email = email
            new_user.save()
            return redirect('/login/')  # 自动跳转登录页面
    register_form = forms.RegisterForm()
    return render(request, 'shopstore/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/index/')
    request.session.flush()

    return redirect('/index/')


def cart(request, user_name):
    context = {}
    if not request.session.get('is_login', None):
        message = '请先登录！'
        context['message'] = message
        return render(request, 'shopstore/login.html', context)
    else:
        user = models.User.objects.get(name=user_name)
        user_cart = models.BooksUser.objects.filter(user=user)

        return render(request, 'shopstore/shoppingCart.html', locals())


def books(request, isbn):
    """书籍详情页"""
    try:
        book = models.Books.objects.get(ISBN=isbn)
        context = {
            'book': book
        }
        return render(request, 'shopstore/book_detail.html', context)
    except:
        return HttpResponse('没有该书籍...')


def add_into(request, isbn):
    """将书籍添加到购物车"""
    context = {}
    if not request.session.get('is_login', None):
        message = '请先登录！'
        context['message'] = message
        return render(request, 'shopstore/login.html', context)
    else:
        book = models.Books.objects.get(ISBN=isbn)
        username = request.session.get('user_name', None)
        user = models.User.objects.get(name=username)
        col = models.BooksUser.objects.filter(book=book, user=user)
        if col:
            col[0].count += 1
            col[0].save()
        else:
            models.BooksUser.objects.create(book=book, user=user, count=1)
        route = '/add_success/' + str(book.ISBN)
        return redirect(route)


def add_success(request, isbn):
    context ={'isbn':isbn}
    return render(request, 'shopstore/add_success.html', context)


def leave_message(request):
    return render(request, 'shopstore/message_board.html')


def order_confirm(request, user_name):
    if request.method == 'POST':
        books_name = request.POST.getlist('checkbox_list')
        if books_name:
            counts = request.POST.getlist('counts')
            user = models.User.objects.get(name=user_name)
            user_cart = models.BooksUser.objects.filter(user=user)
            order_books = []
            total = 0
            order = models.Order.objects.create(user=user)  # 每次提交创建一个订单
            for item, count in zip(user_cart, counts):
                if item.book.name in books_name:
                    order_book = models.BooksOrder.objects.create(order=order, book=item.book, count=count)
                    order_books.append(order_book)
                    total += item.book.price*int(count)
            context = {'order_books': order_books, 'user': user}
            return render(request, 'shopstore/orderConfirmation.html', locals())
        else:
            return redirect('/cart/'+user_name)
    else:
        return HttpResponse("没有订单提交")


def pay(request):
    username = request.session.get('user_name')
    user = models.User.objects.get(name=username)
    total = request.GET.get('total')
    order_number = request.GET.get('order_number')
    return render(request, 'shopstore/pay.html', locals())


def pay_success(request, order_number):
    if request.method == 'POST':
        password = request.POST.get('password', None)
        username = request.session.get('user_name')
        user = models.User.objects.get(name=username)
        order = models.Order.objects.get(order_number=order_number)
        books_order = models.BooksOrder.objects.filter(order=order)

        total = 0
        for item in books_order:
            total += item.book.price*item.count
        route = '/pay/' + '?total=' + str(total) + '&order_number=' + str(order_number)
        if user.password == hash_code(password):
            if user.balance >= total:
                user.balance -= total
                user.save()
                return render(request, 'shopstore/success.html', {'order_number':order_number,\
                              'total':total, 'balance':user.balance})
            else:
                redirect(route)
        else:
            return redirect(route)
    return HttpResponse('没有数据提交')


def search_result(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword', None)
        if keyword:
            result_by_name = models.Books.objects.filter(name__contains=keyword)
            if result_by_name:
                length = len(result_by_name)
                return render(request, 'shopstore/index.html', {'book_list': result_by_name,'length':length})
            else:
                result_by_category = models.Books.objects.filter(category__icontains=keyword)
                length = len(result_by_category)
                return render(request,'shopstore/index.html', {'book_list':result_by_category,'length':length})
        else:
            return redirect('/index/')

    else:
        return HttpResponse('没有数据提交！')
        

