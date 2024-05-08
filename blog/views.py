from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
import urllib3
from django.db.models import Q
from blog.forms import CommentForm, ReplayForm, SearchPost
from .models import Category,Post,Comment
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


# Display List Category
class CategoryAndSubView(View):
    def get(self, request, slug=None):
        post = Post.objects.all().order_by('-datetime_created')
        category = Category.objects.filter(sub_cat=False)
        if slug:
            category_slug = get_object_or_404(Category, slug=slug)
        context = {'category': category,'category_slug':category_slug,'post':post,}
        return render(request, 'blog/blog.html', context)




def post_detail(request, slug):
    global data3
    post = get_object_or_404(Post, slug=slug)
    post.save()
    category = Category.objects.filter(sub_cat=False)
    create = Post.objects.all().order_by('-datetime_created')[:3]
    comment = Comment.objects.filter(post__slug=slug).order_by('-datetime_created')
    comment_form = CommentForm()
    reply_form = ReplayForm()
    form = SearchPost()
    similar = post.tags.similar_objects()[:3]
    if 'search' in request.GET:
           form = SearchPost(request.GET)
    if form.is_valid():
            data = form.cleaned_data['search']
            page_obj = post.filter(Q(title__icontains=data))
            paginator = Paginator(page_obj, 3)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
    if slug:
        data3 = get_object_or_404(Post, slug=slug,)

    return render(request, 'blog/blog_detail.html', {'post': post,
                                                    'comment': comment,
                                                    'comment_form': comment_form,
                                                    'category': category,
                                                    'similar': similar,
                                                    'create': create,
                                                    'data3': data3,
                                                     'reply_form': reply_form,
                                                     'form' : form ,
                                                    })




def comment_post(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():

            data = comment_form.cleaned_data
            Comment.objects.create(fullname=data['fullname'],email=data['email'],text=data['text'],
                                   post_id=id)
            messages.success(request, 'نظر شما با موفقیت ثبت شد.')
            return redirect(url)
        else:
            messages.success(request, 'ثبت نظر با مشکل مواجه شد لطفا دوباره تلاش کنید .')
            return redirect(url)


def comment_replay(request, id, comment_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        replay_form = ReplayForm(request.POST)
        if replay_form.is_valid():
            data = replay_form.cleaned_data
            Comment.objects.create(
                text=data['text'],
                post_id=id,
                replay_id=comment_id,
                is_reply=True
            )
            messages.success(request, 'Thank you for the reply', 'primary')
            return redirect(url)
        else:
            return redirect(url)              




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

