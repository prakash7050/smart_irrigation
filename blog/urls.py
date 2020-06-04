


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog'),
    path('<int:blog_id>/',views.details,name='detail'),
]