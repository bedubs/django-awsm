from django.urls import path
from django.conf.urls import url
from awsm import views

app_name = 'awsm'
urlpatterns = [
    path('', views.index_page, name='index'),
    path('ec2', views.instance_list, name='instance_list'),
]
