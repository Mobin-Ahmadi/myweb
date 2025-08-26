from django.shortcuts import render
from blog.models import Post

def projects_view(request):
    posts = Post.objects.filter(published=True, attachment__isnull=False).order_by('-created_at')
    return render(request, 'projects/projects.html', {'posts': posts})
