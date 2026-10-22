
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count

from documents.models import Document, AuditLog


# COMMON LOGIN - USER + ADMIN
def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect("admin_dashboard")
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_active:
            login(request, user)

            if user.is_staff:
                return redirect("admin_dashboard")

            return redirect("/home/")

        return render(
            request,
            "accounts/login.html",
            {"error": "Invalid username or password"}
        )

    return render(request, "accounts/login.html")


# REGISTER - NORMAL USERS ONLY
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


# ADMIN ACCESS CHECK
def is_admin(user):
    return user.is_authenticated and user.is_staff


# CUSTOM ADMIN DASHBOARD
@user_passes_test(is_admin, login_url="/login/")
def admin_dashboard(request):
    User = get_user_model()

    total_users = User.objects.count()
    total_documents = Document.objects.count()

    total_shares = Document.objects.aggregate(
        total=Count("shared_with")
    )["total"] or 0

    recent_logs = AuditLog.objects.select_related(
        "user", "document"
    ).order_by("-timestamp")[:10]

    recent_documents = Document.objects.select_related(
        "owner"
    ).order_by("-uploaded_at")[:8]

    context = {
        "total_users": total_users,
        "total_documents": total_documents,
        "total_shares": total_shares,
        "recent_logs": recent_logs,
        "recent_documents": recent_documents,
    }

    return render(
        request,
        "accounts/admin_dashboard.html",
        context
    )

from django.views.decorators.http import require_POST

@require_POST
def logout_view(request):
    logout(request)
    return redirect("login")