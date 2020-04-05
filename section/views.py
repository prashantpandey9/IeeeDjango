from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
# Create your views here.
from .models import *
def main(request):
	member=Member.objects.exclude(title__contains='Branch').exclude(title__contains='Director')
	society=Society.objects.all()
	event=Event.objects.all()
	xtreme=Xtreme.objects.all().order_by("-version")
	o=['Director','Branch']
	s=[]
	for m in o:
		s+=list(Member.objects.filter(title__contains=m))
	context={
	"member":member,
	"society":society,
	"event":event,
	"xtreme":xtreme,
	"s":s
	}
	return render(request,'index.html',context)

def xtreme(request,pk):
	xtreme=Xtreme.objects.filter(version=pk).order_by("-version")
	team=Team.objects.filter(ver__version=pk).order_by("college_rank")
	context={
	"team":team,
	"xtreme":xtreme,
	}
	return render(request,'xtreme.html',context)	
