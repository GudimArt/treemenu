from django import template
from django.utils.safestring import mark_safe
from urllib.parse import urlparse

from core.apps.treemenu.models import MenuItem


register = template.Library()


@register.simple_tag
def draw_menu(menu_name, current_url):
    menu_items = MenuItem.objects.filter(menu__title=menu_name)
    html_tags = ["<ul class='tree'>"]
    menu_items_buffer = []
    for item in menu_items:
        draw_item(item, current_url, menu_items_buffer, html_tags)
    html_tags.append("</ul>")
    html_tags = open_parents(html_tags)
    html_tree = "".join(html_tags)
    return mark_safe(html_tree)


def draw_item(item, current_url, menu_items_buffer, html_tags):
    print(current_url)
    if item not in menu_items_buffer:
        if item.children is not None:
            if urlparse(item.url).path == current_url or item.url == current_url:
                html_tags.append("<li>")
                html_tags.append("<details open>")
                html_tags.append(
                    f"<summary> <a href='{item.url}'><strong>{item.title}</strong></a></summary>"
                )
            else:
                html_tags.append("<li>")
                html_tags.append("<details>")
                html_tags.append(
                    f"<summary> <a href='{item.url}'>{item.title}</a></summary>"
                )
                html_tags.append("<ul>")
            menu_items_buffer.append(item)
            for item in item.children.all():
                draw_item(item, current_url, menu_items_buffer, html_tags)
                html_tags.append("</ul></details></li>")

        if item.children is None:
            parent = item.parent
            html_tags.append("<ul>")
            for item_without_child in parent.children:
                html_tags.append(
                    f"<li><a href='{item_without_child.url}'>{item_without_child.title}</a></li>"
                )
                menu_items_buffer.append(item_without_child)
            html_tags.append("</ul>")

    return html_tags


def open_parents(html_tags):
    details_buffer = []
    for i in range(0, len(html_tags)):
        if html_tags[i] == "<details open>":
            for i in details_buffer:
                html_tags[i] = "<details open>"
            break
        elif html_tags[i] == "<details>":
            details_buffer.append(i)

    return html_tags
