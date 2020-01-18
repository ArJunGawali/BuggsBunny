from django.shortcuts import render,redirect
from . import models 
import time
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import requests
from django.core.mail import send_mail

curl=settings.CURRENT_URL

def home(request):
	return render(request,'index.html',{})




@csrf_protect
def register(request):
	if request.method=='GET':
		return render(request,'register.html',{'curl':curl,'output':''})
	else:
		name=request.POST.get('name')
		username=request.POST.get('username')
		password=request.POST.get('password')
		address=request.POST.get('address')
		mobile=request.POST.get('mobile')
		Rtype=request.POST.get('type')
		
		dt=time.asctime(time.localtime(time.time()))
		
		query="insert into register values(NULL,'%s','%s','%s','%s','%s','%s')" %(name,username,password,address,mobile,Rtype)
		models.cursor.execute(query)
		models.db.commit()
		
		return render(request,'register.html',{'curl':curl,'output':'Registration successfull....'})

def about(request):
	return render(request,'about.html',{})


@csrf_exempt
def login(request):
	if request.method=='GET':
		return render(request,'login.html',{'curl':curl,'output':''})
	else:
		username=request.POST.get('username')
		password=request.POST.get('password')
		print(username)
		
		
		query= "select * from register where username='%s' and password='%s' "%(username,password)
		models.cursor.execute(query)
		userDetails=models.cursor.fetchall()
		print(userDetails)
		# models.cursor.close()
		
		if len(userDetails)>0:
			if userDetails[0][6]=='1':
				ip_request = requests.get('https://ipinfo.io')
				my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
				print(my_ip)
# Prints The IP string, ex: 198.975.33.4

# Step 2) Look up the GeoIP information from a database for the user's ip

				geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
				geo_request = requests.get(geo_request_url)
				geo_data = geo_request.json()
				print(geo_data)

				loc=geo_data["city"]
				print(loc)

				
				query="select * from dloc"
				models.cursor.execute(query)
				clist=models.cursor.fetchall()
				c=0
				for j in clist:
					c=c+1
				print(c)

				for i in range(c):
					print(clist[i][1])
					print(loc)
					if clist[i][1] == loc :
						send_mail('Location info','your are in the city' + loc + ' And there is ' + clist[i][2] + 'named disease spreading','arjungawali111@gmail.com',[username],fail_silently=False)
					# else:
					# 	send_mail('Location info','your are in the city' + loc + ' And there is no disease spreading','arjungawali111@gmail.com',[username],fail_silently=False)



				return redirect('http://127.0.0.1:8000/user/',{'username':username})
			else:
				return redirect('http://127.0.0.1:8000/doctor/',{'username':username})	
		else:
			return render(request,'login.html',{'curl':curl,'output':'Login failed, invalid user or verify your account'})	
