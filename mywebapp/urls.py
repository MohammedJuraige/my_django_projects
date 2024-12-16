from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/', views.page_detail, name='page_detail'),
]
urlpatterns += [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]