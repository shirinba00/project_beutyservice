from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.core.paginator import Paginator
import urllib3
from blog.forms import SearchPost
from .models import Category,Post
from django.contrib import messages



def post_list(request, slug=None,id=None):
    post = Post.objects.all().order_by('-datetime_created')
    form = SearchPost()
    category = Category.objects.filter(sub_cat=False)
    paginator = Paginator(post, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if 'search' in request.GET:
        form = SearchPost(request.GET)
        if form.is_valid():
            data = form.cleaned_data['search']
            page_obj = post.filter(title__icontains=data)
            paginator = Paginator(page_obj,3)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
    if slug and id:
        data = get_object_or_404(Category,)
        page_obj = post.filter(category=data)
        paginator = Paginator(page_obj,3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    return render(request, 'blog/blog.html', {'post': page_obj, 'category': category,
                                                 
                                                  'form': form,'page_number':page_number,
                                                  })


def category_and_sub(request, slug=None,id=None):
    post = Post.objects.all().order_by('-datetime_created')
    category = Category.objects.filter(sub_cat=False)
    if slug and id:
        data = get_object_or_404(Category,)
        page_obj = post.filter(category=data)
        paginator = Paginator(page_obj, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', {'post': page_obj,
                                               'category': category,
                                               'page_number':page_number,
                                                  })



def post_detail(request, slug):
    global data3
    post = get_object_or_404(Post, slug=slug)
    post.save()
    category = Category.objects.filter(sub_cat=False)
    create = Post.objects.all().order_by('-datetime_created')[:10]
    # comment = Comment.objects.filter(post__slug=slug).order_by('-datetime_create')
    # comment_form = CommentForm()
    similar = post.tags.similar_objects()[:6]
    if slug:
        data3 = get_object_or_404(Post, slug=slug,)

    return render(request, 'blog/blog_detail.html', {'post': post,
                                                    # 'comment': comment,
                                                    # 'comment_form': comment_form,
                                                    'category': category,
                                                    'similar': similar,
                                                    'create': create,
                                                    'data3': data3,
                                                    })










# # display posts in category and subcategory
# def post_list_by_category(request, category_id):
#     # category = get_object_or_404(Category, id=category_id)
#     product = Product.objects.all().order_by('-created_datetime')[:10]
#     category = get_object_or_404(Category, slug=uri_to_iri(category_id))
#     # post = Post.objects.all().order_by('-datetime_created')
#     # create = Post.objects.all().order_by('-datetime_created')[:3]
#     create = Post.objects.all().order_by('-num_view')[:12]
#     posts = category.post.all()

#     return render(request, "mag/post_list.html", {'posts': posts, 'category': category,
#                                                   'create': create,
#                                                   'product': product,
#                                                   })

