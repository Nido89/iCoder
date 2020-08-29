from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from blog.models import Post

# Create your views here.
#MY html Pages
def home(request):
    return render(request,'home/home.html')


def about(request):
    messages.info(request, 'Welcome1 to AboutUs')

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


def search(request):
    #allPosts = Post.objects.all()
    query= request.GET['query']
    if len(query)>100:
        allPosts= Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent,allPostsAuthor)
        if allPosts.count() == 0:
            messages.warning(request, "No matching results to your query. Please try again.")
    params = {'allPosts': allPosts, 'query':query}
    return render(request,'home/search.html',params)

#Authentication APIs
def handleSignup(request):
    if request.method == 'POST':
        #Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email  = request.POST['email']
        pass1  = request.POST['pass1']
        pass2 = request.POST['pass2']


        # checking for error inputs
        if len(username) >10:
            messages.error(request, "Username can not be longer than 10 characters.")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must be alpha numeric which means must contain only letters and numbers, coz no special characters allowed..")
            return redirect('home')

        if len(username) < 3:
            messages.error(request, "Username must be longer than 3 characters.")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, "Make sure to match password when confirming.")
            return redirect('home')
            #
        #Create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Congrats on your account registered at DevTalkies.")
        return redirect('home')

    else:
        return HttpResponse('Not Allowed')

def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged in")
            return redirect('home')
        else:
            messages.error(request, "Can not login because in valid credentials")
            return redirect('home')

    return HttpResponse('404-Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')

