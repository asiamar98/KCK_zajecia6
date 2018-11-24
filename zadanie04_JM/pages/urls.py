from django.urls import path

from .views import AboutPageView, HomePageView, StronaPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('dodatkowastrona/', StronaPageView.as_view(), name='dodatkowastrona'),
]
