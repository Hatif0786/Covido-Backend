from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.News_List),

]
