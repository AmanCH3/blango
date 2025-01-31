import logging
from django.contrib.auth import get_user_model
from django import template
from django.utils.html import format_html
from blog.models import Post

logger = logging.getLogger(__name__)

user_model = get_user_model()
register = template.Library()

@register.filter
def author_details(author, current_user):
    """Returns the author's details as a formatted HTML string."""
    if not isinstance(author, user_model):
        return ""

    if author == current_user:
        return format_html("<strong>me</strong>")

    name = f"{author.first_name} {author.last_name}" if author.first_name and author.last_name else author.username

    if author.email:
        return format_html('<a href="mailto:{}">{}</a>', author.email, name)

    return format_html("{}", name)

@register.simple_tag
def row(extra_classes=""):
    """Returns the opening div tag for a row with optional extra classes."""
    return format_html('<div class="row {}">', extra_classes)

@register.simple_tag
def endrow():
    """Returns the closing div tag for a row."""
    return format_html("</div>")

@register.simple_tag(takes_context=True)
def author_details_tag(context):
    """Returns the author's details formatted as an HTML string, considering the request context."""
    request = context["request"]
    current_user = request.user
    post = context["post"]
    author = post.author

    if author == current_user:
        return format_html("<strong>me</strong>")

    name = f"{author.first_name} {author.last_name}" if author.first_name and author.last_name else author.username

    if author.email:
        return format_html('<a href="mailto:{}">{}</a>', author.email, name)

    return format_html("{}", name)

@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
    """Returns the five most recent posts, excluding the current post."""
    posts = Post.objects.exclude(pk=post.pk).order_by("-created_at")[:5]  # Assuming `created_at` exists
    logger.debug("Loaded %d recent posts for post %d", len(posts), post.pk)
    return {"title": "Recent Posts", "posts": posts}
