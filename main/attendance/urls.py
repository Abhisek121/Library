from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.userlogin , name = 'userlogins'), 
    #path('', auth_views.LoginView.as_view() , name = 'login'),
    path('home/', views.index , name = 'index'),
    path('indexprocessing/', views.index1 , name = 'index1'),
    path('manageprocessing/', views.manage1 , name = 'manage1'),
    path('detailprocessing/', views.details1 , name = 'details1'),
    path('bookprocessing/', views.bookdetails1, name = 'bookdetails1'),
    path('about_me/', views.about_me, name = 'about_me'),
    path('process/', views.process, name = 'process'),
    path('processbook/', views.processbook, name = 'processbook'),
    path('users/', views.details, name = 'details'),
    path('books/', views.details_book, name = 'books'),
    path('manage/', views.manage , name = 'manage'),
    path('cardselect/', views.card , name = 'card'),
    path('cardedit/', views.edit , name = 'cardedit'),
    path('searchuser/', views.search , name = 'search'),
    #path('register/', views.register_request, name="register"),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('add_book/', views.add_book, name='add_book'),
    path('click_add/', views.click_add),
    path('click_add_book/', views.click_add_book),
    path('export/', views.exportcsv, name='export'),
    path('empLeave/', views.EmpLeaveApp, name= 'empLeave'),
    path('leaves/', views.leaves, name= 'leaves'),
    path('notification/', views.notification, name= 'notification'),
    path('notice_view/', views.notice_view, name= 'notice_view'),
    path('empticket/', views.sendticket, name='empticket'),
    path('ticketview/', views.tickets, name='ticketview')
]
