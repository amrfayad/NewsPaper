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
	print context
	return render(request,'MyDesign.html',context)

def post (request,section_name):
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
            return render(request,'MyDesign.html')
    else:

        form = RegistrationForm()

    return render(request,'registration/Register.html',{'form':form})
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('MyDesign.html')
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
