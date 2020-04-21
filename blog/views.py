from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request):
    return render(request,'blog/blogHome.html')
    #return HttpResponse('This is blogHome.We will keep all the BlogPost here.')

def blogPost(request,slug):
    return render(request,'blog/blogPost.html')
    #return HttpResponse(f'This is blogPost:{slug}')