from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bmi/', views.bmi_calculator, name='bmi_calculator'),
    path('glucose/', views.glucose_evaluator, name='glucose_evaluator'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('type1/', views.type1, name='type1'),
    path('type2/', views.type2, name='type2'),

]
