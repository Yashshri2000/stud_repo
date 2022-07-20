# from django.http import JsonResponse

from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'index.html')



class ChartData(APIView):
	authentication_classes = []
	permission_classes = []
    labels = []
    chartdata =[]

	def get(self, request, format = None):
        obj = student.objects.all()
        for names in obj:
            n= names.obj.name
            labels.append(n)
            
		for marks in obj:
            m= marks.obj.marks
            chartdata.append(m)
            
		chartLabel = "my data"
		
		data ={
					"labels":labels,
					"chartLabel":chartLabel,
					"chartdata":chartdata,
			}
		return Response(data)


# def index(request):
#     return render(request,'index.html')