from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('add_teacher/',views.Add_Teacher, name='add_teacher' ),
    path('view_teacher/',views.View_Teacher, name='view_teacher' ),
    path('update_teacher/<int:pid>/',views.Update_Teacher, name='update_teacher' ),
    path('delete_teacher/<int:pid>/',views.Delete_Teacher, name='delete_teacher' ),

    path('add_student/',views.Add_Student, name='add_student' ),
    path('view_student/',views.View_Student, name='view_student' ),
     path('update_student/<int:pid>/',views.Update_Student, name='update_student' ),
     path('delete_student/<int:pid>/',views.Delete_Student, name='delete_student' ),

    path('login/', auth_views.LoginView.as_view(template_name='hospital/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='hospital/logout.html'), name='logout'),

    path('feedback/',views.Feedback, name='feedback'),
    
    
]

