from django.contrib import admin
from django.urls import path
from nithish import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Power/',views.power,name="Power"),
    path('',views.power,name="Power")
]