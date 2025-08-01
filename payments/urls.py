from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('create/', views.create_payment, name='create_payment'),
    path('confirm/', views.confirm_payment, name='confirm_payment'),
    path('payees/', views.payee_list, name='payee_list'),
    path('payees/add/', views.add_payee, name='add_payee'),
    path('payees/<int:pk>/edit/', views.edit_payee, name='edit_payee'),
    path('payees/<int:pk>/statement/', views.payee_statement, name='payee_statement'),
    path('payments/<int:pk>/', views.payment_detail, name='payment_detail'),
    path('analytics/', views.payment_analytics, name='payment_analytics'),
    path('payments/<int:pk>/update_status/<str:status>/', views.update_payment_status, name='update_payment_status'),
]
