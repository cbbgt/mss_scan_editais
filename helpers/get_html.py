from lxml import html
from .reduce_html import reduce_html


def get_html(page, xpath):
    tree = html.fromstring(page.content)
    content_list = tree.xpath(xpath)
    content = content_list[0].text_content()
    return reduce_html(content.lstrip())
