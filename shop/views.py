from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib import messages
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator

class AllProducts(View):
    def get(self, request, slug=None):
        products = Product.objects.all()
        category = CategoryProduct.objects.filter(sub_cat=False)
        paginator = Paginator(products,6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    # form = SearchPost()
    # if 'search' in request.GET:
    #     form = SearchPost(request.GET)
    #     if form.is_valid():
    #         data = form.cleaned_data['search']
    #         page_obj = post.filter(title__icontains=data)
    #         paginator = Paginator(page_obj,3)
    #         page_number = request.GET.get('page')
    #         page_obj = paginator.get_page(page_number)
        if slug:
            category_obj = get_object_or_404(CategoryProduct, slug=slug)
            products = products.filter(category=category_obj)
        
        paginator = Paginator(products, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'products': page_obj,'category':category}
        return render(request, 'shop/Allproducts.html', context)



# display detail typeservice
class DetailProductView(View):
    product = Product.objects.all()
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        category = CategoryProduct.objects.filter(sub_cat=False)
        # form = SearchTypeService()
       
        # if 'search' in request.GET:
        #    form = SearchTypeService(request.GET)
        # if form.is_valid():
        #     data = form.cleaned_data['search']
        #     data = category.filter(Q(name__icontains=data))
          
        if slug:
            product = get_object_or_404(Product, slug=slug)
        context = {'product': product,'product': product,
                    'category': category,
                    }
        return render(request, 'shop/detail_product.html', context)
    
     
    
