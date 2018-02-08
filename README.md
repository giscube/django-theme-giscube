Django Theme GISCube
=========================

Install
-------

pip install -e git+https://github.com/giscube/django-theme-giscube.git#egg=theme_giscube


Use
---

Add 'theme_giscube' to 'INSTALLED_APPS', before 'django.contrib.admin'

```
INSTALLED_APPS = [
    ...
    'theme_giscube',
    ...
    'django.contrib.admin',
    ...
]
```


Customize
---------

Create a ''base_site.html'' file in ''your_app/templates/admin'', with an extends line like in this example:

```
{% extends "theme_giscube/base_site.html" %}

{% block branding %}
<h1 id="site-name"><img src="/foo/bar/static/logo.svg" /><a href="{% url 'admin:index' %}">{{ site_header|default:_('Django administration') }}</a></h1>
{% endblock %}
```
