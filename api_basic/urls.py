from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import article_list, article_detail
from .views import ArticleAPIView, ArticleDetailsAPIView, GenericAPIView
from .views import ArticleViewSet, ArticleGenericViewSet
from .views import author_view

router = DefaultRouter()
router.register('article-viewset', ArticleViewSet, basename='article')
router.register('article-viewset-generic', ArticleGenericViewSet, basename='article-generic')

urlpatterns = [

    # With def and api_view / csrf
    path('article/', article_list),
    path('article-detail/<int:pk>/', article_detail),

    # With class and APIView
    path('article-view/', ArticleAPIView.as_view()),
    path('article-detail-view/<int:pk>/', ArticleDetailsAPIView.as_view()),

    # With class, GenericAPIView and mixins
    path('article-generic/', GenericAPIView.as_view()),
    path('article-generic/<int:pk>/', GenericAPIView.as_view()),

    # With router and viewset
    # With pk/ get métodos with pk
    path('', include(router.urls)),

    path('author', author_view, name='author_view')
]
