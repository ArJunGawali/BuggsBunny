

# Create your views here.

from django.shortcuts import render,redirect
from . import models
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail

def adminhome(request):
	return render(request,'adminhome.html',{})

# def add(request):
# 	return render(request,'add.html',{})



def add(request):
	if request.method=='GET':
		return render(request,'add.html',{'output':''})	
	else:
		dname=request.POST.get('dname')
		
		disc=request.POST.get('disc')
		prec=request.POST.get('prec')
		# foodicon=request.FILES['foodicon']
		# fs = FileSystemStorage()
		# filename = fs.save(foodicon.name,foodicon)





		
		query="insert into Dadd values(NULL,'%s','%s','%s')" %(dname,disc,prec)
		models.cursor.execute(query)
		models.db.commit()

		query1='select username from register'
		models.cursor.execute(query1)
		elist=models.cursor.fetchall()
		email1 = 'Hello there,'
		email2='We have got new disease update'
		email3=dname
		email4=disc
		email5=prec
		for i in elist:
			send_mail('Disease Update',email1 + '\n' + email2 + '\n' + '\n' + 'Disease Name: ' + email3 + '\n' + '\n' + 'Description : ' + email4 + '\n' + '\n' + 'Precaution: ' + email5,'arjungawali111@gmail.com',i,fail_silently=False)


		return render(request,'add.html',{'output':'Disease Added Successfully'})

def chat(request):
    #from django.contrib.auth import authenticate
    #user = authenticate(username='john', password='secret')


    
    
    user=request.user
    finallist=[]
    userlist=User.objects.values('username')
    
    print(userlist[0])
    chatmsg ='chat' in request.POST and request.POST['chat']
    print(chatmsg)
    if(chatmsg!=False):
        chatmg=emojitotext(chatmsg)
        c=chatmsgs(user=user,message=chatmg)
        #print(chatmsg)
        #if chatmsg !='':
        c.save()
            
        chatemoj=texttoemojitag(chatmsg)
        print(chatemoj)
        d=chatemojiss(user=user,message=chatemoj)
        #if chatemoj !='':
        d.save()
    #u = User.objects.get(special=True)
    main_id=user.id
    print(main_id)
    userpf=UserProfiles.objects.filter(user_id=main_id).values('deaf')
    result=userpf[0]['deaf']
    print("ans")
    print(result)
    if(result==True):
        emojimessg=chatemojiss.objects.values('message','user_id')
        print(emojimessg)
        try:
            i = 0
            while(emojimessg[i]['message'] != ""):
                msg=emojimessg[i]['message']
                user_id=emojimessg[i]['user_id']
                userobj=User.objects.filter(id=user_id).values('username')
                print(userobj)
                finallist.append([userobj[0]['username'],msg])
                i = i + 1
        except IndexError:
            pass    
    else:
        try:
            emojimessg=chatmsgs.objects.values('message','user_id')
            j = 0
            while(emojimessg[j]['message'] !=" "):
                msg=emojimessg[j]['message']
                user_id=emojimessg[j]['user_id']
                userobj=User.objects.filter(id=user_id).values('username')
                finallist.append([userobj[0]['username'],msg])
                j = j+1
            print(finallist)        
        except IndexError:
            pass


    #print(userpf.id)
    #if (user.special in User==False):
    #    print("kaam bhari bhari kaam")

    return render(request,"chathome.html",{'user':user,'finallist':finallist,'userlist':userlist})

def dloc(request):
	if request.method=='GET':
		return render(request,'dloc.html',{'output':''})	
	else:
		city=request.POST.get('city')
		
		dsp=request.POST.get('dsp')
		ani=request.POST.get('ani')
		# foodicon=request.FILES['foodicon'] 
		# fs = FileSystemStorage()
		# filename = fs.save(foodicon.name,foodicon)


		query="insert into dloc values(NULL,'%s','%s','%s')" %(city,dsp,ani)
		models.cursor.execute(query)
		models.db.commit()
		return render(request,'dloc.html',{'output':'Disease and Location Added Successfully'})



def message(request):
	return render(request,'message.html',{})
