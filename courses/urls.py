from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CourseView.as_view(), name='course-list'),
    path('<int:id>', views.CourseView.as_view(), name='course-detail'),
    path('<int:id>/delete', views.CourseDeleteView.as_view(), name='course-delete'),
    path('create', views.CourseCreateView.as_view(), name='course-create'),
]