from django.test import TestCase

# for some reason, we have to use get_user_model and not settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from .models import PackageRequest


class PackageRequestTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(email="test@gmail.com", password="pass")
        testuser1.save()
        test_packagerequest = PackageRequest.objects.create(
            owner=testuser1, item_name="Green Eggs and Ham", body="I do not like green eggs and ham, Sam I  am."
        )
        test_packagerequest.save()

    def test_blog_content(self):
        packagerequest = PackageRequest.objects.get(id=1)
        self.assertEqual(str(packagerequest.owner), "test@gmail.com")
        self.assertEqual(str(packagerequest.item_name), "Green Eggs and Ham")
        self.assertEqual(str(packagerequest.item_description), "I do not like green eggs and ham, Sam I  am.")
