from django.urls import path
from . import views


app_name = "books"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/thread/", views.thread_create, name="thread_create"),
    # path("<int:pk>/thread/<int:thread_pk>/", views.thread_create, name="thread_create"),
]
