from django.urls import path
from .views import home_page

urlpatterns = [
    path("", home_page, name="home"),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),  # 設定首頁
]