from django.shortcuts import render

from django.http import HttpResponse
from .models import Section,Post,Tag
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
