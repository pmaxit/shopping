from django.shortcuts import render
from .models import Product, Category
from django.views.generic import ListView, DetailView, CreateView
from django.http import Http404
import sys

# Add your forms here
from .forms import ProductSearchForm, AddClassifiedForm

# Create your views here.
APP_DIR = 'products'
MAX_URL_PATH_LENGTH = 12


def conditions(request):
    template = 'conditions.html'
    context = locals()
    return render(request, template, context)


class CategoryListView(ListView):
    model = Category
    template_name = 'products/home.html'
    queryset = model.objects.main_categories()

    # by default it uses requestContext. Check TemplateResponse class resolve_context
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data()
        context['recommended'] = "Recommended strings are here."

        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_base_details.html'
    context_object_name = 'product'


class AddProducts(CreateView):
    form_class = AddClassifiedForm
    template_name = 'products/addClassified.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'products/category_details.html'
    context_object_name = 'category'
    form = ProductSearchForm()


    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView,self).get_context_data(**kwargs)

        #context['products'] = self.object.product_set.all().order_by('created_at')

        context['products'] = Product.objects.all().order_by('created_at')
        context['searchform'] = self.form

        return context
