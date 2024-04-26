from django.shortcuts import render
from .models import Comment

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'comment_list.html', {'comments': comments})

def add_comment(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        comment = Comment(author=author, text=text)
        comment.save()
    return render(request, 'add_comment.html')