from django.urls import path
from .views import *

urlpatterns = [
    # path('',index, name='home'),
     path('', HomeView.as_view()),
    # path('test-api', views.get_data),
    path('api',ChartData.as_view()),
    
]