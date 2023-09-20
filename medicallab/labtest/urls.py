from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from labtest import views


# url routing for dia app
urlpatterns = [
    path('', LandingAPI.as_view(), name="landing"),

    path('download', views.download, name="download"),
    path('pdf/', views.generatePDF, name="pdf"),

    path('dashboard/', DashboardAPI.as_view(), name="dashboard"),
    path('register/', RegisterAPI.as_view(), name="register"),
    path('login/', LoginAPI.as_view(), name="login"),
    path('logout/', views.user_logout, name='logout'),

    path('staff/', StaffListView.as_view(), name='staff-list'),
    path('staff/<int:staff_id>/tests/', views.staff_tests, name='staff-tests'),

    path('create-customer/', CreateCustomerView.as_view(), name='create-customer'),
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),

    path('create-test/', CreateTestView.as_view(), name='create-test'),
    path('test-list/', TestListView.as_view(), name='test-list'),
    path('staff-test-list/', StaffTestList.as_view(), name='staff-test-list'),
    path('test/<int:pk>/', TestDetailView.as_view(), name='test-detail'),

]