from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),  # welcome.html 페이지 매핑
    path('work/', views.work, name='work'),   # work.html 페이지 매핑
    path('work/<int:todo_id>/', views.work, name='work'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),   # work.html 조회
]