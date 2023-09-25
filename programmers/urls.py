from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('programmer/<int:programmer_id>/', views.programmer_full_information, name='programmer_full_information'),

]
