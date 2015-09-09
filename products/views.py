from django.shortcuts import render
from .models import Product, Category
from django.views.generic import ListView, DetailView
from django.http import Http404

# Create your views here.
APP_DIR = 'products'

def home(request):
    template = 'products/home.html'
    context = locals()
    return render(request, template, context)




class CategoryListView(ListView):
    model = Category
    template_name = 'products/home.html'
    queryset = model.objects.main_categories()

    # by default it uses requestContext. Check TemplateResponse class resolve_context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'products/category_details.html'
    context_object_name = 'category'

    def get_path(self):
        if self.object is None:
            return Http404("Object does not exist")
        path=[]
        p = self.object
        while(p):
            path.insert(0, p)
            p = p.parent

        return path

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView,self).get_context_data(**kwargs)
        context['path']= self.get_path()
        #context['products'] = self.object.product_set.all().order_by('created_at')
        context['products'] = Product.objects.all().order_by('created_at')
        return context