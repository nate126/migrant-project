from django.urls import include, path

from pages import admin

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
    path("", HomeView.as_view(), name= 'my_home_view')
]