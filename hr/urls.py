from django.urls import path
from hr import views

app_name = "hr"

urlpatterns = [
    path('office/', views.OfficeList.as_view()),
    path('office/<int:pk>', views.OfficeDetail.as_view()),
    path('title/', views.TitleList.as_view()),
    path('title/<int:pk>', views.TitleDetail.as_view()),
    
    path('employee/', views.EmployeeList.as_view()),
    path('employee/<str:pk>', views.EmployeeDetail.as_view()),
    path('employee-title/', views.EmployeeTitleList.as_view()),
    path('employee-title/<int:pk>', views.EmployeeTitleDetail.as_view()),
    path('employee-office/', views.EmployeeOfficeList.as_view()),
    path('employee-office/<int:pk>', views.EmployeeOfficeDetail.as_view())
]