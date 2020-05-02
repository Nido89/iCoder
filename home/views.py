from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home/home.html')


def about(request):
    messages.info(request, 'Welcome1 to AboutUs')
    messages.info(request, 'Welcome2 to AboutUs')
    messages.info(request, 'Welcome3 to AboutUs')
    return render(request,'home/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name,email,phone,content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)< 5:
            messages.error(request,"Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone,content=content)
            contact.save()
            messages.success(request,"Your message sent correctly")
    return render(request,'home/contact.html')