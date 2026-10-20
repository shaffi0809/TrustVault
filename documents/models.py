from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owned_documents"
    )
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    shared_with = models.ManyToManyField(
        User,
        blank=True,
        related_name="shared_documents"
    )

    def __str__(self):
        return self.title
class AuditLog(models.Model):
    ACTION_CHOICES = [
        ("UPLOAD", "Document Uploaded"),
        ("SHARE", "Document Shared"),
        ("REVOKE", "Access Revoked"),
        ("DOWNLOAD", "Document Downloaded"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    document = models.ForeignKey(
        Document,
        on_delete=models.SET_NULL,
        null=True
    )
    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES
    )
    details = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} - {self.timestamp}"