from . import views
from django.urls import path

urlpatterns = [
    # path('',views.myfun,name='demo'),
    path('',views.mymember,name='mymember')
]