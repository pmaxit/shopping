from django import template
from django.template.defaultfilters import stringfilter
import datetime

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    :param value: parent string from which characters need to be removed
    :param arg: characters needed to be removed
    :return: return string after characters are removed

    Removes all values of arg from the given string
    """
    return value.replace(arg, "")


@register.filter
@stringfilter
def lower(value):
    return value.lower()

@register.simple_tag(takes_context=True)
def addClassWhenActive(context, object, cssClass):
    if object in context.get('path',[]):
        return cssClass
    else:
        return "non-active"

# Example of simple tags
# these tags work independently on arguments and produce output
@register.simple_tag
def current_time(format_string):
    return "%s"%(datetime.datetime.now().strftime(format_string))

@register.tag('mycomment')
def do_comment(parser, token):
    nodelist = parser.parse(('endmycomment',))
    parser.delete_first_token()
    return commentNode()

class commentNode(template.Node):
    def render(self, context):
        return ''

