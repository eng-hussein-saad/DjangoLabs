from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
  return value * arg

#create a custom filter that if truncates a paragrapth if it is longer than 500 words.

@register.filter(name='truncatewords')
def truncatewords(value, arg):
  words = value.split()
  return ' '.join(words[:arg])