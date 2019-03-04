from datetime import datetime

from django import template

from giscube.utils import get_version

register = template.Library()


@register.simple_tag
def giscube_version():
    return get_version()


@register.simple_tag
def giscube_copyright_year():
    return datetime.now().year
