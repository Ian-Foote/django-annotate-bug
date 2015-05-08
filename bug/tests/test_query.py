import datetime

from django.db.models import Case, F, IntegerField, Sum, When
from django.test import TestCase
from django.utils.timezone import utc

from .. import models


class TestAnnotate(TestCase):
    def test_empty_comments(self):
        past = datetime.datetime(2000, 1, 1, tzinfo=utc)
        post = models.Post.objects.create(created=past)

        posts = models.Post.objects.annotate(
            unread_comments=Sum(
                Case(
                    When(comments__created__gt=F('created'), then=1),
                    default=0,
                    output_field=IntegerField(),
                ),
            ),
        )
        self.assertIn(post, posts)
