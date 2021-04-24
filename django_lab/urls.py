from django.urls import path

from .views import CelebrityCreateView, CelebrityDeleteView, CelebrityEditView

urlpatterns = [
    path('', CelebrityCreateView.as_view()),
    path('<int:pk>/', CelebrityEditView.as_view()),
    path('<int:pk>/delete', CelebrityDeleteView.as_view())
]
