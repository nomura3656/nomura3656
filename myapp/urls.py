from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_product/', views.add_product, name='add_product'),  # 追加
    path('success/', views.success, name='success'),  # 'success'という名前のURLパターンを追加

]
