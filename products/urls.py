# Product urls
from django.conf.urls import include, url
from .views import CategoryListView,CategoryDetailView

urlpatterns = [
    url(r'^products/(?P<slug>.*)/$', CategoryDetailView.as_view(), name='single_category'),
    url(r'^$', CategoryListView.as_view(), name='home'),

]