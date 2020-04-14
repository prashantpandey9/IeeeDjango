from django.shortcuts import render,get_object_or_404
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

	# r=[]#for verison collection
	# for jn in xtreme:
	# 	r.append(jn.version) 
	context={
	"member":member,
	"society":society,
	"event":event,
	"xtreme":xtreme,
	"s":s,
	}
	return render(request,'index.html',context)

def xtreme_view(request,pk):
	xtreme=Xtreme.objects.filter(version=pk).order_by("-version")
	team=Team.objects.filter(version__version=pk).order_by("college_rank")
	post = get_object_or_404(Xtreme, pk=pk)
	context={
	"team":team,
	"xtreme":xtreme,
	"post":post,
	}
	return render(request,'xtreme.html',context)	

