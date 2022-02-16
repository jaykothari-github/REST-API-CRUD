from django.urls import path
from . import views

urlpatterns = [
    path('',views.overview,name='overview'),
    path('all-data/',views.all_data,name='all-data'),
    path('create-data/',views.create_data,name='create-data'),
    path('one-data/<int:pk>',views.one_data,name='one-data'),
    path('update-data/<int:pk>',views.update_data,name='update-data'),
    path('delete-data/<int:pk>',views.delete_data,name='delete-data'),
]
