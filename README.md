# TrustVault – Secure Document Sharing Platform

**A Django-based web application for secure document management, controlled sharing, and activity tracking.**


## Demo Accounts

The following accounts are provided for testing the TrustVault application.

| Role | Username | Password | Access |
|---|---|---|---|
| Admin | `SNOVASYS` | `s1n2o3@1` | Administrative access |
| Document Owner | `user` | `u1s2e3r4@` | Upload, manage, download, and share owned documents |
| Viewer | `user1` | `u1s2e3r4@1` | View and download documents shared with them |


## Project Overview

TrustVault is a web application designed to help users securely upload, manage, download, and share documents.

Document owners can grant access to registered users and revoke permissions whenever required. The system enforces access-control checks before document downloads and maintains audit logs of important document activities.

The platform also provides an administrative dashboard for monitoring users, documents, sharing activity, and recent audit logs.

## Key Features

- **User Authentication:** User registration, login, and logout.
- **Document Management:** Upload and download documents with a maximum upload size of 5 MB.
- **Secure Document Sharing:** Share documents with other registered users.
- **Access Revocation:** Document owners can remove previously granted access.
- **Permission-Based Downloads:** Only authorized users can download protected documents.
- **Audit Logging:** Track upload, download, sharing, and revocation activities.
- **Admin Dashboard:** View platform statistics and recent activities.
- **File Validation:** File extension validation and upload size restrictions.
- **Access Protection:** Prevent unauthorized access to protected pages.

## Technology Stack

| Component | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS |
| Authentication | Django Authentication System |
| Local Database | SQLite |
| Production Database | PostgreSQL |
| Deployment | Render |
| Version Control | Git, GitHub |
| Production Server | Gunicorn |

## Live Application

**Live Website:** https://trustvault-nc69.onrender.com/

**GitHub Repository:** https://github.com/shaffi0809/TrustVault

## How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/shaffi0809/TrustVault.git
cd TrustVault
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Generate a local Django secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Set the generated key in PowerShell:

```powershell
$env:DJANGO_SECRET_KEY="YOUR_GENERATED_SECRET_KEY"
```

Keep secret keys and database credentials private. Do not commit them to GitHub.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Run Automated Tests

```bash
python manage.py test documents
```

## Security Features

TrustVault implements several application-level security measures:

- Django authentication for user accounts.
- Role-based access restrictions for administrative pages.
- Document ownership and sharing permission checks.
- Protected document downloads.
- File extension validation.
- Maximum upload size of 5 MB.
- Audit logging for important document actions.
- Logout and protected-page access checks.

**Security limitations:** File extension validation alone cannot guarantee file safety. Future improvements include file-content validation, malware scanning, enhanced storage protection, and additional automated security testing.

## Application Workflow

1. A user registers and logs in.
2. The user uploads a document.
3. The document appears in the user's document dashboard.
4. The owner shares the document with another registered user.
5. The recipient accesses the document through the shared documents section.
6. The owner can revoke access when necessary.
7. Important document activities are recorded in audit logs.

## Testing and Deployment Status

The application has been deployed on Render.

The following workflows have been manually verified on the live application:

- User registration and login.
- Administrative login and dashboard access.
- Document upload and download.
- Document sharing and access revocation.
- Restriction of administrative access for normal users.
- Protection of the user dashboard after logout.

Further production security review, file-storage persistence testing, and performance testing are recommended.

## Future Enhancements

- Email-based password recovery.
- Document version history.
- Expiring document-sharing permissions.
- Improved file scanning and validation.
- More comprehensive automated security tests.
- Enhanced monitoring and notifications.

## Project Information

**Project Name:** TrustVault

**Category:** Secure Document Management and Sharing

**Purpose:** SNOVASYS Fresher Hiring Challenge 2026

**Status:** Deployed and core functionality tested