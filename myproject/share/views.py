
# File Name: share/views.py

from django.shortcuts import render
from django.views.generic import TemplateView, ListView


# 创建视图类需要基础视图基类
# 例如 TemplateView 就是用于展示页面的模板视图基类
# 该类仅提供 get 方法，用于处理 GET 请求
# 当然也可以自定义其它方法，例如 post
class HomeView(TemplateView):
    '''用来展示主页的视图类
    '''

    # 展示主页的话，只需要提供模板文件的名字即可
    # 当客户端发起 get 请求时，由父类的 get 方法处理请求
    # 该属性用于提供模板文件，在父类的方法中被调用
    template_name = 'base.html'
