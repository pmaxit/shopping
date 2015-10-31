from django import forms
from models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Button
from crispy_forms.layout import Field, HTML
from crispy_forms.bootstrap import FormActions, TabHolder, Tab


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            TabHolder(

                Tab('My Account',

                    Field('username', css_class='cz-input-text'),
                    Field('password1',css_class='cz-input-text'),
                    Field('password2',css_class='cz-input-text'),
                    FormActions(
                        Submit('save', 'Save Changes'),
                        Button('cancel', 'Cancel')
                        )
                    ),
                Tab('MyAds',
                    Field('username', css_class='cz-input-text'),
                ),

                Tab('Messages')
            )

        )