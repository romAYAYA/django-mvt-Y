from django.template import Library
from django_app.models import Post, PostRating

register = Library()


@register.simple_tag
def post_rating(post_id: str) -> int:
    post = Post.objects.get(id=int(post_id))
    ratings = PostRating.objects.all().filter(post=post)
    return (
        ratings.filter(is_liked=True).count() - ratings.filter(is_liked=False).count()
    )
