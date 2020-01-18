from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from . import models 
import time
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail

curl=settings.CURRENT_URL

# Create your views here.
# def userhome(request):
# 	return render(request,'userhome.html',{})

def userhome(request):
	query="select * from Dadd"
	models.cursor.execute(query)
	clist=models.cursor.fetchall()
	return render(request,'userhome.html',{'curl':curl,'clist':clist})

def locs(request):
	if request.method=='GET':
		return render(request,'locs.html',{'output':''})	
	else:
		city=request.POST.get('city')

		query="select * from dloc"
		models.cursor.execute(query)
		clist=models.cursor.fetchall()
		c=0
		for j in clist:
			c=c+1
		print(c)

		

		for i in range(c):
			if clist[i][1] == city :
				


				return render(request,'locs.html',{'curl':curl,'clist':clist , 'output':'Disease in '+city+' is '+clist[i][2]})
			else:
				return render(request,'locs.html',{'curl':curl,'clist':clist , 'output':'No Disease ' })





		