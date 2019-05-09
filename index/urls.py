from django.urls import path
from . import views
# 设置首页url地址
urlpatterns = [
    path('', views.indexView, name='index')
]