from django.shortcuts import render
from django.http import HttpResponse
from .awsm import AWSManager as awsm


def index_page():
    pass

def instance_list(request):
    ec2 = awsm().ec2_instance()['Reservations']
    return render(request, 'awsm/list.html', {'ec2': ec2})
