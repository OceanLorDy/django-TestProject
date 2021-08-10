from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home, name="homepage"),
    path("accounts/", include('accounts.urls')),
    path("detail/<int:id>", views.index, name="index"),
    path("articles/", include('articles.urls')),
    path("about/", views.about, name="about"),
]

urlpatterns += staticfiles_urlpatterns()
