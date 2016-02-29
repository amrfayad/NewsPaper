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
	print section_name
	all_section= Section.objects.get(title= section_name)
	posts= Post.objects.filter(section= all_section)
	print posts
	context= {'posts':posts}
	return render(request,'post_app/posts.html',context)

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
