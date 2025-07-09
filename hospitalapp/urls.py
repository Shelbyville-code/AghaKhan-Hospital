from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.index,name='index'),
    path('', views.register,name='register'),
    path('login', views.login_view,name='login'),
    path('starter', views.starter,name='starter'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('doctors/', views.doctors,name='doctors'),
    path('appointment/', views.appointment,name='appointment'),
    path('departments/', views.departments,name='departments'),
    path('contact/', views.contact,name='contact'),
    path('show/', views.show,name='show'),
    path('delete/<int:id>', views.delete),
    path('show_contact/', views.show_contact,name='show_contact'),
    path('delete_contact/<int:id>', views.delete_contact),
    path('edit/<int:id>', views.edit,name='edit'),
]
