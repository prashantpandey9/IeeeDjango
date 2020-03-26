from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
# Create your views here.
from .models import *
def main(request):
	j=member.objects.all()
	context={
	"image":j
	}
	return render(request,'index.html',context)