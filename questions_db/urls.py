from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Topics', views.TopicViewSet)
router.register(r'Level', views.LevelViewSet)
router.register(r'McqQuestion', views.McqQuestionViewSet)
router.register(r'RelatedExam', views.RelatedExamViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('apis/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
