
from django.urls import path
from . import views


urlpatterns = [
    path('', views.testlist),
    path('yourname/<str:name>', views.yourname)

]
