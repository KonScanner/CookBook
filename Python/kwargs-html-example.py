import html

"""
An html make_element() function that
accepts any number of keyword arguements
"""


def make_element(name, value, **kwargs):
    key_values = [' %s="%s"' % item for item in kwargs.items()]
    attr_str = ''.join(key_values)
    element = f'<{name}{attr_str}>{html.escape(value)}</{name}>'
    return element


print(make_element('item', 'Test Item', size='large', quantity=6),
      make_element('p', '<spam>'), sep='\n')
