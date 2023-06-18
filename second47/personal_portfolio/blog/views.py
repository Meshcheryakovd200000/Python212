from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required  # эта страница не должна показываться незаавторизованным пользователям
def blogs(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)  # если данные существуют то будут попадать в переменную
    # blog, если не существуют то ошибка 404
    return render(request, 'blog/details.html', {'blog': blog})
