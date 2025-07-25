from django.urls import path
from . import views

urlpatterns = [
    path('<int:pid>/', views.p_detail, name='problem_detail'),
]