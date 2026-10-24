# TrustVault - AI Usage Documentation

## 1. AI Tools Used
ChatGPT was used as a learning and development assistant during the project.

## 2. How AI Was Used
- Understand Django project structure and setup.
- Learn how to implement document uploads and downloads.
- Debug errors during development.
- Implement document sharing and access revocation.
- Understand authentication and authorization checks.
- Create automated tests for document access permissions.
- Prepare project documentation and threat analysis.

## 3. Issues Encountered and Fixes
- **Django setup:** Fixed project setup and configuration issues.
- **Document upload:** Fixed errors in document upload handling.
- **Access control:** Updated download permissions to block unauthorized users.
- **Sharing:** Implemented sharing and revocation functionality.
- **Security testing:** Added tests for owners, shared users, unauthorized users, and revoked users.

## 4. Testing
Ran `python manage.py test documents`. All four document access security tests passed.

## 5. Responsible AI Use
AI suggestions were reviewed and tested during development. The project owner is responsible for understanding the code, verifying the implementation, and disclosing AI assistance honestly.# TrustVault – AI Assistance and Debugging Log

## Project Information

**Project:** TrustVault – Secure Document Sharing Platform  
**AI Tool Used:** ChatGPT  
**Development Framework:** Django  
**Challenge:** SNOVASYS Fresher Hiring Challenge 2026

## 1. How I Used AI

I used ChatGPT to understand Django concepts, develop initial features, troubleshoot errors, and improve project documentation.

I tested the suggested solutions locally and on the deployed application. When something failed, I used error messages and test results to identify the problem and make corrections.

## 2. Django Login Redirect Issue

**Problem:** After logging in, users were redirected to `/home/`, but the application returned a 404 error.

**Cause:** The document application's URL configuration did not match the login redirect path.

**Fix:** I checked `documents/urls.py` and updated the home route to match `/home/`.

**Verification:** I tested the login flow again and confirmed that normal users could access their dashboard.

**Lesson:** URL patterns and redirects must match exactly.

## 3. Production Admin Command Error

**Problem:** The custom `ensure_admin` Django management command failed with an error indicating that the module did not contain a `Command` class.

**Fix:** I corrected the management command structure by defining a class that inherits from Django's `BaseCommand`.

**Verification:** I ran the command's help option locally and confirmed that Django recognized it. After deployment, I successfully accessed the production admin dashboard.

**Lesson:** Django management commands require the correct file structure and `Command` class.

## 4. Missing Django Secret Key

**Problem:** The local application returned a 500 Internal Server Error.

**Error:**

`django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.`

**Fix:** I generated a local Django secret key and configured the `DJANGO_SECRET_KEY` environment variable.

**Verification:** The application started without the secret-key configuration error.

**Lesson:** Development and production environments require correctly configured environment variables.

## 5. Homepage Not Found Error

**Problem:** The deployed application's main URL returned a Not Found error, although other application pages were accessible.

**Fix:** I updated the root URL configuration to redirect visitors to the login page.

**Verification:** I opened the Render live website and confirmed that the login page loaded successfully.

**Lesson:** The application's main URL should lead visitors to a working page.

## 6. Admin Dashboard Logout Button

**Problem:** The custom admin dashboard did not have a logout button.

**Fix:** I added a logout form using the existing Django logout URL, the POST method, and a CSRF token.

**Verification:** I tested the logout button and confirmed that it redirected to the login page.

**Lesson:** Authentication features must be accessible through the user interface and tested after implementation.

## 7. Testing

I ran the Django document application's automated tests using:

`python manage.py test documents`

**Result:**

- Tests discovered: 4
- Tests passed: 4
- Tests failed: 0

I also manually tested user registration, login, document upload, download, sharing, access revocation, admin access restrictions, and logout protection.

## 8. What AI Did Not Replace

AI helped me understand errors and suggested possible solutions, but I still needed to run commands, inspect error messages, update files, and verify whether the application worked.

I learned that generated code should not be accepted without testing, especially when working with authentication, permissions, and deployment settings.

## 9. Remaining Improvements

The application still needs stronger uploaded-file validation, malware scanning, additional automated security tests, and verification of long-term file storage reliability.

These limitations are documented rather than presented as completed features.