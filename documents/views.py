from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, HttpResponseForbidden
from .models import Document, AuditLog
from django.contrib.auth.models import User
import os
from django.core.exceptions import ValidationError
ALLOWED_EXTENSIONS = {
    ".pdf",
    ".doc",
    ".docx",
    ".txt",
    ".jpg",
    ".jpeg",
    ".png",
}

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

@login_required(login_url="/login/")
def home(request):
    error = ""

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        uploaded_file = request.FILES.get("file")

        if not title or not uploaded_file:
            error = "Please enter a title and choose a file."

        else:
            extension = os.path.splitext(uploaded_file.name)[1].lower()

            if extension not in ALLOWED_EXTENSIONS:
                error = (
                    "Unsupported file type. Upload PDF, DOC, DOCX, "
                    "TXT, JPG, JPEG or PNG."
                )

            elif uploaded_file.size > MAX_FILE_SIZE:
                error = "File must be 5 MB or smaller."

            else:
                document = Document.objects.create(
                    owner=request.user,
                    title=title,
                    file=uploaded_file
                )

                AuditLog.objects.create(
                    user=request.user,
                    document=document,
                    action="UPLOAD",
                    details="Document uploaded successfully"
                )

                return redirect("home")

    my_documents = Document.objects.filter(
        owner=request.user
    ).order_by("-uploaded_at")

    shared_documents = Document.objects.filter(
        shared_with=request.user
    ).order_by("-uploaded_at")

    return render(request, "documents/home.html", {
        "my_documents": my_documents,
        "shared_documents": shared_documents,
        "error": error,
    })



@login_required(login_url="/login/")
def download_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    # Only the owner or an authorized user can download
    if document.owner_id != request.user.id:
        has_access = document.shared_with.filter(
            id=request.user.id
        ).exists()

        if not has_access:
            return HttpResponseForbidden(
                "403 Forbidden: You don't have access to this document."
            )

    AuditLog.objects.create(
        user=request.user,
        document=document,
        action="DOWNLOAD",
        details="Document downloaded successfully"
    )

    return FileResponse(
        document.file.open("rb"),
        as_attachment=True,
        filename=document.file.name.split("/")[-1]
    )

@login_required(login_url="/login/")
def share_document(request, document_id):
    document = get_object_or_404(
        Document,
        id=document_id,
        owner=request.user
    )

    message = ""

    if request.method == "POST":
        username = request.POST.get("username", "").strip()

        try:
            user_to_share = User.objects.get(username=username)

            if user_to_share == request.user:
                message = "You already own this document."
            elif document.shared_with.filter(
                id=user_to_share.id
            ).exists():
                message = "Document is already shared with this user."
            else:
                document.shared_with.add(user_to_share)
                AuditLog.objects.create(
                    user=request.user,
                    document=document,
                    action="SHARE",
                    details=f"Shared with {user_to_share.username}"
                )
                message = "Document shared successfully."

        except User.DoesNotExist:
            message = "User not found."

    return render(request, "documents/share.html", {
        "document": document,
        "message": message,
    })


@login_required(login_url="/login/")
def revoke_access(request, document_id, user_id):
    if request.method != "POST":
        return redirect("home")

    document = get_object_or_404(
        Document,
        id=document_id,
        owner=request.user
    )

    user_to_remove = get_object_or_404(
        User,
        id=user_id
    )

    document.shared_with.remove(user_to_remove)
    AuditLog.objects.create(
        user=request.user,
        document=document,
        action="REVOKE",
        details=f"Access revoked for {user_to_remove.username}"
    )

    return redirect("share_document", document_id=document.id)