from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('detail', views.product_detail_view, name='detail'),
    path('create', views.product_create_view, name='create'),
    path('raw_create', views.product_create_raw_view, name='raw_create'),
    path('django_raw_create', views.product_create_django_form_view, name='django_raw_create'),
    path('initial_data', views.render_initial_data, name='initial_data'),
    path('dynamic_detail/<int:my_id>', views.dynamic_lookup_view, name='dynamic_view'),
    path('delete/<int:id>', views.product_delete_view, name='delete'),
]
