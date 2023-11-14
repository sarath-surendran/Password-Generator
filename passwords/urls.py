from django.urls import path
from . import views

urlpatterns = [
    path('save/', views.savepassword, name="save_password"),
    path('view/',views.viewsavedpasswords, name="view_saved_passwords"),
]