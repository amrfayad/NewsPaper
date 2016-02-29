from django.shortcuts import render
from django.contrib.auth import authenticate,login , logout
from django.http import HttpResponse,HttpResponseRedirect
from .models import Section,Post,Tag

from post_app.forms import RegistrationForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render_to_response
# Create your views here.
def sections (request):
	all_section= Section.objects.all()
	context={'sections':all_section}
	return render(request,'post_app/index.html',context)
def post (request,section_name):

	all_section= Section.objects.all()
	section= Section.objects.get(title= section_name)
	post_list= Post.objects.filter(section= section)
	paginator = Paginator(post_list, 5)
	page = request.GET.get('page')
	try:
        	posts = paginator.page(page)
        except PageNotAnInteger:
        	posts = paginator.page(1)
    	except EmptyPage:
        	posts = paginator.page(paginator.num_pages)
	context = {'posts': posts , 'sections':all_section}
	return render(request,'post_app/sec_post.html',context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return render(request,'post_app/index.html')
    else:
        form = RegistrationForm()
    return render(request,'post_app/Register.html',{'form':form})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('post_app/index.html')

def home (request):
	all_section= Section.objects.all()
	post_list = Post.objects.all()
	paginator = Paginator(post_list, 5)
	page = request.GET.get('page')
	try:
        	posts = paginator.page(page)	
        except PageNotAnInteger:
        	posts = paginator.page(1)				
    	except EmptyPage:
        	posts = paginator.page(paginator.num_pages)
	context = {'posts': posts , 'sections':all_section}

	if request.method == "POST":
		username = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=username,password=pwd)
        if user is not None:
            if user.is_active: #Check If User Isn't banned
                login(request,user)
                return render (request,"post_app/index.html", context)
            else:
                return HttpResponse("Disabled Please Check Admin")
	return render(request,"post_app/index.html", context)

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
        	posts = paginator.page(1)	
    	except EmptyPage:
        	posts = paginator.page(paginator.num_pages)
  	return render_to_response('pagination.html', {'posts': posts})
def mainview(request):
	all_section= Section.objects.all()
	post_list = Post.objects.all()
	paginator = Paginator(post_list, 5)
	page = request.GET.get('page')
	try:
        	posts = paginator.page(page)	
        except PageNotAnInteger:
        	posts = paginator.page(1)				
    	except EmptyPage:
        	posts = paginator.page(paginator.num_pages)
	context = {'posts': posts , 'sections':all_section}
	return render_to_response('post_app/index.html',context)
def showpost(request,post_id):
    obj = Post.objects.get(id=post_id)
    all_section= Section.objects.all()
    context = {'post':obj,'sections':all_section}
    return render(request,'post_app/show_post.html',context)
	


