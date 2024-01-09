from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_pk>[0-9]+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]