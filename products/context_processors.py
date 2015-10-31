from products.models import Category
from products.forms import ProductSearchForm, SignInForm

def add_context(request):
    categories = Category.objects.main_categories()
    return {
        'categories': categories,
        'searchform': ProductSearchForm(),
        'signinform': SignInForm()
    }