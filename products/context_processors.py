from products.models import Category


def add_context(request):
    categories = Category.objects.main_categories()
    return {
        'categories': categories
    }