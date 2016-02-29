from django.shortcuts import render

from django.http import HttpResponse
from .models import Section,Post,Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render_to_response
# Create your views here.
def sections (request):
	all_section= Section.objects.all()
	context={'sections':all_section}
	print context
	return render(request,'post_app/sections.html',context)


def post (request,section_name):
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

from models import Post

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
	


