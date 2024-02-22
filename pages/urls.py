from django.urls import include, path

from pages import admin

from .views import home_page_view, shelter_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
]