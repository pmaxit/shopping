from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button, Field, Fieldset, HTML, Div
from crispy_forms.bootstrap import FormActions, TabHolder, Tab, AppendedText
from django.contrib.auth.models import User

from .models import Product
from .common import CommonLayout

class ProductSearchForm(forms.Form):
    search_text = forms.CharField(label='search', max_length=100)

    def __init__(self, *args, **kwargs):
        super(ProductSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('search_text', css_class='form-control'),
                HTML(' <small><a href="#" class="btn-advanced-search">Advanced</a></small>'),
                Submit('search', 'Search', css_class='btn btn-danger btn-sm btn-search')
            )
        )


class AddClassifiedForm(forms.ModelForm):
    CHOICES = (
        ('EXMPL', 'Example'),
        ('SIMPL', 'Simple'),
    )

    SECTIONS = [
        'Classified sections',
        'Classified details',
        'Personal details',
    ]

    main_section = forms.ChoiceField(choices=CHOICES, required=True, label='Main Section')
    type = forms.ChoiceField(choices=CHOICES, required=True, label='Type')
    category = forms.ChoiceField(choices=CHOICES, required=True, label='Category')

    heading = forms.CharField(label = 'heading')
    text = forms.CharField(label ='Text', widget=forms.Textarea)
    price = forms.IntegerField(label ='Price')
    zipcode = forms.CharField(label = 'Zip code')

    username = forms.CharField(label = 'Your Name')
    phone = forms.CharField(label = 'Phone')
    email = forms.CharField(label = 'E-mail')

    needletters = forms.BooleanField(label = 'Sign Up for Newsletter')
    agreeterms = forms.BooleanField(label = 'I agree to <a href=""> Terms of Use</a>')

    def __init__(self, *args, **kwargs):
        super(AddClassifiedForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(
                    HTML("<h3 class='panel-title'> %s </h3>"%(self.SECTIONS[0])),
                    css_class='panel-heading',
                ),
                Div(
                    Field('main_section'),
                    css_class='panel-body'
                ),
                css_class='panel panel-info'
            ),

            Div(
                Div(
                    HTML("<h3 class='panel-title'> %s </h3>"%(self.SECTIONS[1])),
                    css_class='panel-heading',
                ),
                Div(
                    Field('type'),
                    Field('category'),
                    Field('heading', placeholder='eg. Apple IPAD mini 32GB Wi-Fi + Cellular 1 Year old'),
                    Field('text'),
                    Div(
                        AppendedText('price', '$'),
                        css_class='input-group'
                    ),
                    Div(
                        Field('zipcode'),
                        css_class= 'input-group'
                    ),
                    css_class='panel-body'

                ),
                css_class='panel panel-info'
            ),
             Div(
                Div(
                    HTML("<h3 class='panel-title'> %s </h3>"%(self.SECTIONS[2])),
                    css_class='panel-heading',
                ),
                Div(
                    Field('username', placeholder='John Smith'),
                    Field('phone', placeholder='XXX-XXX-XXXX'),
                    Field('email', placeholder='abc@gmail.com'),

                    css_class='panel-body'

                ),
                css_class='panel panel-info'
            ),
            CommonLayout(),
              Div(
                    Button('Preview & Save', 'Preview & Save', css_class='btn btn-success'),
                    css_class='form-group'
                ),


        )

    class Meta:
        model = Product
        fields = '__all__'


class SignInForm(forms.ModelForm):
    remember_me = forms.BooleanField()

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                Div(
                    Field('email', css_class='form-control', placeholder='Email Address'),
                    css_class='form-group',
                ),
                Div(
                    Field('password', css_class='form-control', placeholder='Password'),
                    css_class='form-group',
                ),
                Div(
                    Field('remember_me'),
                    HTML('Remember me '),
                    css_class= 'checkbox',
                ),


                Div(
                    Button('Sign In', 'Sign In', css_class='btn btn-success btn-block'),
                    css_class='form-group'
                ),

            )
        )

    class Meta:
        model = User
        fields = ['email','password']
