from django.test import TestCase

from .models import Hitter


class HitterTest(TestCase):
    def test_hitter_model_should_have_email_field(self):
        hitter = Hitter.objects.create(
            email='supawit@prontomarketing.com'
        )
        self.assertEqual(hitter.email, 'supawit@prontomarketing.com')
