from django import template

from blog.models import InstantMessage


register = template.Library()

@register.filter
def message_count(user):
    if user.is_authenticated:
        qs = InstantMessage.objects.filter(recipient=user,read=False)
        if qs.exists():
            return qs[0].message_content.count()
    return 0