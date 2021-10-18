from rest_framework import routers
from .api import ScheduleViewSet


router = routers.DefaultRouter()
router.register('api/shedule', ScheduleViewSet, 'shedule')


urlpatterns = router.urls