from django.urls import path
from .views import HomePageView, SamplePageView

core_patterns = ([
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
], 'core')