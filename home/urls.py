import requests
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path(''       , views.tables,  name='index'),
  path('password/', views.password, name='password'),
  path('edit_password/<int:password_id>/', views.edit_password, name='edit_password'),
  path('delete_password/<int:password_id>/', views.delete_password, name='delete_password'),
  path('export_passwords_csv/', views.export_passwords_csv, name='export_passwords_csv'),
  path('import_passwords_csv/', views.import_passwords_csv, name='import_passwords_csv'),
  path('generator/', views.password_generator, name='generator'),
]

