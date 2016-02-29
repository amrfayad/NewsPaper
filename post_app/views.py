from django.shortcuts import render
from django.contrib.auth import authenticate,login , logout
from django.http import HttpResponse,HttpResponseRedirect
from .models import Section,Post,Tag
<<<<<<< HEAD
from post_app.forms import RegistrationForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
=======
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render_to_response
>>>>>>> 82e97c8c883c3290211181afd7ce7b20d90266da
# Create your views here.
def sections (request):
	all_section= Section.objects.all()
	context={'sections':all_section}
	print context
	return render(request,'post_app/sections.html',context)


def post (request,section_name):
<<<<<<< HEAD
	all_section= Section.objects.all()
	section= Section.objects.get(title= section_name)
	post_list= Post.objects.filter(section= section)
	
	paginator = Paginator(post_list, 5)
	
	page = request.GET.get('page')
	
	try:
        	posts = paginator.page(page)
		
        except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        	posts = paginator.page(1)
				
		
    	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        	posts = paginator.page(paginator.num_pages)
	
	#context= {'posts':posts}
	context = {'posts': posts , 'sections':all_section}
	return render(request,'post_app/sec_post.html',context)
=======
	print section_name
	all_section= Section.objects.get(title= section_name)
	posts= Post.objects.filter(section= all_section)
	print posts
	context= {'posts':posts}
	return render(request,'post_app/posts.html',context)
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():

            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return render(request,'registration/success.html/')
    else:

        form = RegistrationForm()

    return render(request,'registration/register.html',{'form':form})
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('home')
def home (request):

    blogs = Post.objects.all()

    if request.method == "POST":
        username = request.POST['username']
        pwd = request.POST['password']

        #returns None if user isn't in database
        user = authenticate(username=username,password=pwd)

        if user is not None:
            if user.is_active: #Check If User Isn't banned

                login(request,user)
                return render (request,"home.html",{'blogs':blogs,'request':request})
            else:
                return HttpResponse("Disabled Please Check Admin")

    return render(request,"home.html",{'blogs':blogs,'request':request})

>>>>>>> 09e252fd8a15d2b54b070e1f1dbb0d8589b34d37

#

def index (request,post_id):
    obj = Post.objects.get(id=post_id)
    context = {'post':obj}
    return render(request,'ok.html',context)


def pagination(request):
	post_list = Post.objects.all()
	
	paginator = Paginator(post_list, 5)
	
	page = request.GET.get('page')
	
	try:
        	posts = paginator.page(page)
		
        except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        	posts = paginator.page(1)
				
		
    	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        	posts = paginator.page(paginator.num_pages)

  	return render_to_response('pagination.html', {'posts': posts})


def mainview(request):
	all_section= Section.objects.all()
	#all_sec={'sections':all_section}
	post_list = Post.objects.all()
	
	paginator = Paginator(post_list, 5)
	
	page = request.GET.get('page')
	
	try:
        	posts = paginator.page(page)
		
        except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        	posts = paginator.page(1)
				
		
    	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        	posts = paginator.page(paginator.num_pages)
	
	#all_posts = {'posts': posts}
	context = {'posts': posts , 'sections':all_section}
	return render_to_response('post_app/index.html',context)
def showpost(request,post_id):
    obj = Post.objects.get(id=post_id)
    all_section= Section.objects.all()
    context = {'post':obj,'sections':all_section}
    return render(request,'post_app/show_post.html',context)
	


