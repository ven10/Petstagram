from django.urls import path

from petstagram.photos.views import photo_add_page, photo_details_page, photo_edit_page

urlpatterns = (
    path('photos/add/', photo_add_page, name='photo_add_page'),
    path('photos/<int:pk>/', photo_details_page, name='photo_details_page'),
    path('photos/<int:pk>/edit/', photo_edit_page, name='photo_edit_page'),
)
