from django.urls import path
from django.http import HttpResponse
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('search', views.search, name="search"),
    path('create-course', views.create_course, name="create_course"),
    path('<slug:slug>', views.details, name="course_details"),
    # path('kategori/<int:category_id>', views.getCoursesByCategoryId),
    path('kategori/<slug:slug>', views.getCoursesByCategory, name='courses_by_category'),
 
]
