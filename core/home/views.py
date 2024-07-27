from django.shortcuts import render
from .models import Products,contact



# Create your views here.
def home(request):
    items = Products.objects.all()
    things_to_send= {'items':items}
    return render(request, 'home/home.html',things_to_send)

def Contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name,email,subject,message)
        if name and email and subject and message:
            dic={'name':name,'email':email,'subject':subject,'message':message}
            contact.objects.create(**dic)
    
    return render(request, 'home/contact.html')



def menue(request):
    return render(request, 'home/menue.html')