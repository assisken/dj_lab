from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import CelebrityCreateView, CelebrityDeleteView, CelebrityEditView, LoginView, RegistrationView

urlpatterns = [
    path('', CelebrityCreateView.as_view(), name='celeb-edit'),
    path('<int:pk>/', CelebrityEditView.as_view(), 'celeb-view'),
    path('<int:pk>/delete', CelebrityDeleteView.as_view(), name='celeb-delete'),

    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
    path('register', RegistrationView.as_view(), name='registration'),
]
