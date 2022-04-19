from django.urls import path

# Import the home view
from .views import index, redirect_url_view

appname = "shortUrl"

urlpatterns = [
    # Home view
    path('', index, name='home'),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
]