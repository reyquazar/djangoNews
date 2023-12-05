from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from news.views import home, add_article, register, article_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add_article/', add_article, name='add_article'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='news/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),
]
