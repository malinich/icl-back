from rest_framework.routers import SimpleRouter

from app.point.views import PointsView

router = SimpleRouter(trailing_slash=False)
router.register(r'points', PointsView, base_name='point')

urlpatterns = router.get_urls()
