from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status="Published", category=category_id)

    # Use try/except when we want to do custom action, if the cateogry does not exists
    try:
        category = Category.objects.get(pk=category_id)
    except:
        # category not exists, redirect user to homepage
        return redirect('home')

    # Use get_object_or_404 when you want to show 404 error page if the category does not exists
    #category = get_object_or_404(Category, pk=category_id)

    context ={
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)