from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shopstore'
urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('cart/<str:user_name>/', views.cart, name='cart'),
    path('books_detail/<slug:isbn>/', views.books, name='books'),
    path('message_board/', views.leave_message, name='leave_message'),
    path('order_confirm/<str:user_name>/', views.order_confirm, name='order_confirm'),
    path('pay_success/<int:order_number>', views.pay_success, name='pay_success'),
    path('add_into/<slug:isbn>/', views.add_into, name='add_into'),
    path('add_success/<slug:isbn>', views.add_success, name='add_success'),
    path('pay/', views.pay, name='pay'),
    path('search_result/', views.search_result, name='search_result')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
