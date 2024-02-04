from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserAttributeViewSet, UserSegmentViewSet, UserAttributeFilterViewSet, UserFilterConditionViewSet, ActivityFilterViewSet


router = DefaultRouter()
router.register(r'atr', UserAttributeViewSet, basename='atr'),

router = DefaultRouter()
router.register(r'sgm', UserSegmentViewSet, basename='sgm'),

router = DefaultRouter()
router.register(r'afl', UserAttributeFilterViewSet, basename='afl'),

router = DefaultRouter()
router.register(r'ufc', UserFilterConditionViewSet, basename='ufc'),

router = DefaultRouter()
router.register(r'afc', ActivityFilterViewSet, basename='afc')

urlpatterns = [

    path('atr/', UserAttributeViewSet.as_view({'get':'list'}), name='atr'),
    path('sgm/', UserSegmentViewSet.as_view({'get': 'list'}), name='sgm'),
    path('afl/', UserAttributeFilterViewSet.as_view({'get': 'list'}), name='afl'),
    path('ufc/', UserFilterConditionViewSet.as_view({'get': 'list'}), name='ufc'),
    path('afc/', ActivityFilterViewSet.as_view({'get': 'list'}), name='afc'),
]