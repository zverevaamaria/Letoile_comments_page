from django.shortcuts import render
from .models import Comment
from django.http import HttpResponseRedirect
from django.utils import timezone

def index(request):
    if (request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        url = request.POST.get('like')
        dt = timezone.now()
        comment = Comment(Name = name, url = url, Email = email, Body = body, dt = dt )
        comment.save()
    latest_comm_list = Comment.objects.order_by('-dt')[:10]
    return render(request, 'letu.html', {'latest_comm_list' : latest_comm_list} )
