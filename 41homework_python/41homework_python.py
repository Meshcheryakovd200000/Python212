# список в html странице

from jinja2 import Template

menu = [
    {'href': '/index', 'menu2': 'Главная'},
    {'href': '/news', 'menu2': 'Новости'},
    {'href': '/about', 'menu2': 'О компании'},
    {'href': '/shop', 'menu2': 'Магазин'},
    {'href': '/contacts', 'menu2': 'Контакты'}
]

link = """<ul>
{% for c in menu -%}
{%- if c.menu2 == 'Главная' -%}
<li><a href="{{c['href']}}" class="active">{{ c['menu2'] }}</a></li>
{% else -%}
<li><a href="{{c['href']}}">{{c['menu2']}}</a></li>
{% endif -%}
{% endfor -%}
</ul>"""

tm = Template(link)
msg = tm.render(menu=menu)

print(msg)
