from django.urls import path
from django.http import HttpResponse
from . import views



urlpatterns = [
    path('', views.index),
    path('<kurs_adi>', views.details),
    path('kategori/<int:category_id>', views.getCoursesByCategoryId),
    path('kategori/<str:category_name>', views.getCoursesByCategory, name='courses_by_category'),
 
]
