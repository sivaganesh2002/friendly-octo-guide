"""
URL configuration for code_judge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from accounts import views as accounts_views
from problem_bank import views as problem_bank_views
from problem import views as problem_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', accounts_views.home, name='home'),
    path('login/', accounts_views.cj_login, name='login'),
    path('logout/', accounts_views.cj_logout, name='logout'),
    path('signup/', accounts_views.register, name='signup'),
    path('accounts/login/', accounts_views.cj_login),
    path('create/', problem_views.create_problem, name='create_problem'),  
    path('', problem_bank_views.problem_bank, name='problem_bank'),
    path('problem/', include('problem.urls')),
]
