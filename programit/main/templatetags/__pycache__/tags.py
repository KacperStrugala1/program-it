from django import template

register = template.Library()

@register.filter
def format_duration(value):
    total_seconds = int(value.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

@register.filter(name='add_class')
def add_class(field, css):
    return field.as_widget(attrs={"class": css})