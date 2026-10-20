from django.contrib import admin
from .models import Document, AuditLog

admin.site.register(Document)
admin.site.register(AuditLog)