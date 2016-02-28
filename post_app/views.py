from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from models import Post

def index (request,post_id):
    obj = Post.objects.get(id=post_id)
    context = {'post':obj}
    return render(request,'ok.html',context)
