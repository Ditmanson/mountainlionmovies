from django import template


register = template.Library()

@register.filter
def get_similarity(similarity_scores, viewer_id):
    score = similarity_scores.get(viewer_id, 0)  # Default to 0 if missing
    return f"{score * 100:.1f}%"  # Convert to percentage and format

@register.filter
def runtime_format(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value

@register.filter
def as_percentage(value, decimal_places=1):
    try:
        percentage = float(value) * 100
        return f"{percentage:.{decimal_places}f}%"
    except (TypeError, ValueError):
        return "N/A"
