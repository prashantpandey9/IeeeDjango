from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
# Create your views here.
def main(request):
	context={
	}
	return render(request,'index.html',context)