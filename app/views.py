from django.shortcuts import render
from .models import *



def home(request):
    #for from
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        new_massage = massage(name = name,email = email,sub = subject,text = massage)
        new_massage.save()
    
    #end from code
    my_services = services.objects.all()
    my_work = work.objects.all()
    my_about = about.objects.all()
    diction = {'myservices':my_services,'mywork':my_work,'myabout':my_about}
    return render(request,'home.html',context=diction)


 
