
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from .models import Document


class DocumentSecurityTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(
            username="owner",
            password="TestPass123!"
        )
        self.other_user = User.objects.create_user(
            username="other",
            password="TestPass123!"
        )

        self.document = Document.objects.create(
            owner=self.owner,
            title="Test Document",
            file=SimpleUploadedFile(
                "test.txt",
                b"Sample test content",
                content_type="text/plain"
            )
        )

    def test_owner_can_download_document(self):
        self.client.login(
            username="owner",
            password="TestPass123!"
        )

        response = self.client.get(
            reverse(
                "download_document",
                args=[self.document.id]
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_unauthorized_user_cannot_download(self):
        self.client.login(
            username="other",
            password="TestPass123!"
        )

        response = self.client.get(
            reverse(
                "download_document",
                args=[self.document.id]
            )
        )

        self.assertEqual(response.status_code, 403)

    def test_shared_user_can_download(self):
        self.document.shared_with.add(self.other_user)

        self.client.login(
            username="other",
            password="TestPass123!"
        )

        response = self.client.get(
            reverse(
                "download_document",
                args=[self.document.id]
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_revoked_user_cannot_download(self):
        self.document.shared_with.add(self.other_user)
        self.document.shared_with.remove(self.other_user)

        self.client.login(
            username="other",
            password="TestPass123!"
        )

        response = self.client.get(
            reverse(
                "download_document",
                args=[self.document.id]
            )
        )

        self.assertEqual(response.status_code, 403)
