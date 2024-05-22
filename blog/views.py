from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
import urllib3
from django.db.models import Q
from blog.forms import CommentForm, ReplayForm, SearchPost
from .models import Category,Post,Comment
from pages.models import AboutUS,ContactUs
from django.contrib import messages
from taggit.models import Tag
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request, slug=None, id=None):
    posts = Post.objects.all().order_by('-datetime_created')
    form = SearchPost()
    category = Category.objects.filter(sub_cat=False)
    tag_slug = request.GET.get('tag_slug')
    
    if tag_slug:
        try:
            tag = Tag.objects.get(slug=tag_slug)
            posts = Post.objects.filter(tags=tag)
        except Tag.DoesNotExist:
            posts = None

    if 'search' in request.GET:
        form = SearchPost(request.GET)
        if form.is_valid():
            data = form.cleaned_data['search']
            posts = posts.filter(title__icontains=data)

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    return render(request, 'blog/blog.html', {'post': page_obj, 'category': category,
                                              'form': form, 'tag_slug': tag_slug})
# Display List Category
class CategoryAndSubView(View):
    def get(self, request, slug=None):
        post = Post.objects.all().order_by('-datetime_created')
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
        if slug:
            category_slug = get_object_or_404(Category, slug=slug)
            # data = get_object_or_404(Category)
            # page_obj = post.filter(category=data)
            # paginator = Paginator(page_obj,3)
            # page_number = request.GET.get('page')
            # page_obj = paginator.get_page(page_number)
        context = {'category': category,'category_slug':category_slug,'post':page_obj,'page_number':page_number,}
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


def tagged_posts(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    post= Post.objects.filter(tags=tag)
    paginator = Paginator(post, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/blog.html', {'tag': tag, 'post': page_obj,})

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




# display posts in category and subcategory
def post_list_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    post = Post.objects.filter(category=category)
    paginator = Paginator(post, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.filter(sub_cat=False)
    
    return render(request, "blog/blog.html", {'category': category, 'post': page_obj, 'categories': categories})


