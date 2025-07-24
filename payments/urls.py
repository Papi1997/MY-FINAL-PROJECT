from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('create/', views.create_payment, name='create_payment'),
    path('confirm/', views.confirm_payment, name='confirm_payment'),
    path('payees/', views.payee_list, name='payee_list'),
    path('payees/add/', views.add_payee, name='add_payee'),
    path('payees/<int:pk>/edit/', views.edit_payee, name='edit_payee'),
    path('payments/<int:pk>/', views.payment_detail, name='payment_detail'),
]
