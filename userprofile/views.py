from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.template import RequestContext
from django.views import generic
from django.views.generic import View
from django.shortcuts import render
from forms import UserProfileForm, RegistrationForm, SignUpForm

# Create your views here.


class MyFormView(View):
    form_class = RegistrationForm
    initial = {'key': 'value'}
    template_name = 'userprofile/update_profile.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial= self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            pass

        return render(request, self.template_name, {'form': form})


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    model = UserProfile
    template_name = 'userprofile/update_profile.html'


@login_required
def update_profile(request):
    #userProfile = UserProfile.objects.get(user=request.user)
    form =RegistrationForm()
    return render_to_response('userprofile/update_profile.html',
                              {'form': form}, RequestContext(request))
