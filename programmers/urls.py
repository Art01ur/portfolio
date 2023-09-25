from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('programmer/<int:programmer_id>/', views.programmer_full_information, name='programmer_full_information'),
    path('new/programmer', views.new_programmer, name='new_programmer'),
    path('new/programmer/data', views.new_programmer_data, name='new_programmer_data'),
    path('new/project', views.new_project, name='new_project'),
    path('new/project/data', views.new_project_data, name='new_project_data')

]
