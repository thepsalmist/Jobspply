"""boilerplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from jobs.sitemaps import JobSitemap, StaticSitemap, BlogSitemap
from users import views as user_views
from jobs import views as jobs_views

sitemaps = {
    "static": StaticSitemap,
    "jobs": JobSitemap,
    "blog": BlogSitemap,
}

handler404 = jobs_views.error_404
handler500 = jobs_views.error_500


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", user_views.register, name="register"),
    path("profile/", user_views.profile, name="profile"),
    path("profile-update/", user_views.profile_update, name="profile-update"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("tinymce/", include("tinymce.urls")),
    path("", include("jobs.urls", namespace="jobs")),
    path("career/", include("career.urls", namespace="career")),
    path("cv-services/", include("resume.urls", namespace="resume")),
    path("courses/", include("courses.urls", namespace="courses")),
    path("subscribe/", include("marketing.urls", namespace="marketing")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    # REST_FRAMEWORK URLS
    path("api-auth/", include("rest_framework.urls")),
    path("api/jobs/", include("jobs.api.urls", namespace="jobs_api")),
    path("api/users/", include("users.api.urls", namespace="users_api")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
