from django.db import models

# Create your models here.


class User(models.Model):

    name = models.CharField(max_length=30, unique=True, verbose_name='用户名')
    email = models.EmailField(unique=True, verbose_name='邮箱')
    create_time = models.DateField(auto_now_add=True, verbose_name='创建时间')
    phone_number = models.CharField(max_length=11, verbose_name='电话号码')
    password = models.CharField(max_length=120, verbose_name='密码', default='123456')  # s数据库中存的是密码的哈希值
    address = models.TextField(verbose_name='地址', default='重庆市邮电大学')
    balance = models.FloatField(verbose_name='余额', default=50)

    class Meta:
        ordering = ['-create_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.name


class Books(models.Model):
    book_category = (
        ('Finance', '金融'),
        ('Management', '管理'),
        ('Math', '数学'),
        ('Computer','计算机'),
        ('English', '英语'),
        ('Art', '艺术'),
        ('Literature', '文学'),
        ('Project','工程'),
        ('Other', '其他')

    )
    ISBN = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=50, verbose_name='书籍名称')
    old_price = models.FloatField(verbose_name='以前价格', default=0)
    price = models.FloatField(verbose_name='价格', default='0')
    book_image = models.ImageField(verbose_name='书籍图片', upload_to='book_image/')
    # 实际路径 /BASE_DIR/media/book_image
    category = models.CharField(max_length=10, choices=book_category, verbose_name='类别')
    description = models.TextField(verbose_name='描述')
    version = models.CharField(max_length=10, verbose_name='版本', blank=True,null=True)
    sale_volume = models.PositiveIntegerField(verbose_name='销量', default=0)
    storage = models.PositiveIntegerField(verbose_name='库存', default=1)
    user = models.ManyToManyField(User, through='BooksUser', verbose_name='用户')

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍'

    def __str__(self):
        if len(self.name) > 10:
            return self.name[0:10]+'...'
        else:
            return self.name


class Order(models.Model):
    order_number = models.AutoField(primary_key=True, verbose_name='订单编号')
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    trade_time = models.DateTimeField(auto_now_add=True, verbose_name='交易日期')
    # consignee_name = models.CharField(max_length=30, verbose_name='收货人姓名', default=user.name)
    # consignee_phoneNumber = models.CharField(max_length=11, verbose_name='收货人电话', default=user.phone_number)
    # consignee_address = models.TextField(verbose_name='收货人地址', default=user.address)
    books = models.ManyToManyField(Books, through='BooksOrder', verbose_name='书籍')

    class Meta:
        ordering = ['-trade_time']
        verbose_name_plural = '订单'
        verbose_name = '订单'

    def __str__(self):
        return str(self.order_number) + '--' + self.user.name


class BooksOrder(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name='书籍')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='订单')
    count = models.PositiveSmallIntegerField(default=1, verbose_name='数量')

    class Meta:
        verbose_name = '订单_书籍关系表'
        verbose_name_plural = '订单--书籍'

    def __str__(self):
        return self.order.__str__() + '--' + self.book.__str__()


class BooksUser(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name='加入购物车的书籍')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    count = models.PositiveSmallIntegerField(default=1, verbose_name='数量')

    class Meta:
        verbose_name_plural = '购物车'
        verbose_name = '购物车'
        unique_together = ('book', 'user')  # 联合主键

    def __str__(self):
        return self.user.name + '--' + self.book.__str__()



