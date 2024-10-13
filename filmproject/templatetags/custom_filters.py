from django import template

register = template.Library()

@register.filter
def runtime_format(value):
    try:
        hours = value // 60
        minutes = value % 60
        if hours > 1 and minutes > 1:
            return f'{hours} hours, {minutes} minutes'
        elif hours > 1 and minutes == 1:
            return f'{hours} hours, {minutes} minute'
        elif hours == 1 and minutes > 1:
            return f'{hours} hour, {minutes} minutes'
        elif hours == 1 and minutes == 1:
            return f'{hours} hour, {minutes} minute'
        elif minutes > 1:
            return f'{minutes} minutes'
        else:
            return f'{minutes} minute'
    except (ValueError, TypeError):
        return value