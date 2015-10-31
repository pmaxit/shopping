from django.conf.urls import include, url
from .views import SignUpView, MyFormView

urlpatterns = [
   # url(r'^(?P<profile_id>\d+/$)', profile, name='profile'),
    url(r'^create/$', SignUpView.as_view(), name='create'),
]