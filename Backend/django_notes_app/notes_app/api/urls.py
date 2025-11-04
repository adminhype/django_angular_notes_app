from rest_framework import routers
from django.urls import path, include
from .views import NoteViewSet

router = routers.SimpleRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
