# Product urls
from django.conf.urls import include, url
from .views import CategoryListView,CategoryDetailView,ProductDetailView, AddProducts, conditions

urlpatterns = [
    url(r'^product/add/$', AddProducts.as_view(), name='add_product'),
    url(r'^products/(?P<slug>.*)/$', CategoryDetailView.as_view(), name='single_category'),
    url(r'^product/(?P<slug>.*)/$', ProductDetailView.as_view(), name='single_product'),
    url(r'^conditions/$', conditions, name='conditions'),

    url(r'^$', CategoryListView.as_view(), name='home'),

]