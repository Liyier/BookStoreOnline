"""BookStoreOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path  # django版本新增
from django.conf.urls import include,url

"""
1.参数name可用于templates，models，views...，对应相应的网址
2.from django.urls import reverse, 可以通过reverse获取对应网址，用法revers(name, args=()),在网页模板中，可以如此使用{% url 'name' %}
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('shopstore.urls', namespace='shopstore')),
    path('captcha', include('captcha.urls'))
]
