from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment,Certificate
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

def base_view(request):
    posts = Post.objects.all().order_by('-created_at')
    search = request.GET.get('search')
    category = request.GET.get('category')
    if search:
        posts = posts.filter(title__icontains=search)
    if category:
        posts = posts.filter(category=category)
    return render(request,'mainview/base.html',{'posts':posts})

def about_view(request):
    return render(request,'mainview/about.html')

def certificate_view(request):
    certificates = Certificate.objects.all()
    return render(request,'mainview/cetificate.html', {'certificates': certificates})

def resume_view(request):
    return render(request,'mainview/resume.html')

def detail_view(request,pk):
    post = get_object_or_404(Post,pk=pk)
    comments = post.comments.all()
    context = {
        'post':post,
        'comments':comments,
    }
    return render(request,'mainview/detail.html',context)


@login_required
@csrf_exempt
def edit_comment_ajax(request, comment_id):
    comment = Comment.objects.get(id=comment_id, user=request.user)
    if request.method == 'POST':
        data = json.loads(request.body)
        comment.content = data['content']
        comment.approved = False  # دوباره نیاز به تایید
        comment.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
@csrf_exempt
def delete_comment_ajax(request, comment_id):
    comment = Comment.objects.get(id=comment_id, user=request.user)
    if request.method == 'POST':
        comment.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def contact_view(request):
    return render(request,'mainview/contact.html')