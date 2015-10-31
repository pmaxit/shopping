__author__ = 'puneet'

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button, Field, Fieldset, HTML, Div, MultiField
from crispy_forms.bootstrap import FormActions, TabHolder, Tab, AppendedText


class CommonLayout(Layout):
    def __init__(self, *args, **kwargs):
        super(CommonLayout, self).__init__(
            Div(
                HTML("<p> PLEASE CAREFULLY READ THESE TERMS OF USE. BY USING THIS WEBSITE YOU INDICATE "
                     "YOUR UNDERSTANDING AND ACCEPTANCE OF THESE TERMS. IF YOU DO NOT AGREE TO THESE TERMS YOU MAY NOT USE THIS WEBSITE. </p>"),
                Div(
                    Field('needletters'),

                ),
                Div(
                    Field('agreeterms'),

                ),
                css_class='well'
            )
        )
