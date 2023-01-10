from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts import views as acc_view
from posts import views as posts_view, views

acc_router = DefaultRouter()
acc_router.register('register', acc_view.ProfileRegisterAPIView)

posts_router = DefaultRouter()
posts_router.register('tweet', posts_view.SecondTweetViewSet)
posts_router.register('comment', posts_view.SecondCommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),

    path('api/accounts/', include(acc_router.urls)),
    path('api/posts/', include(posts_router.urls)),
    path('api/tweet/', views.TweetViewSet.as_view()),
    path('api/posts/tweet/<int:pk>/', views.TweetRetrieveUpdateDestroyAPIView.as_view()),
    path('api/posts/comment/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('api/posts/tweet/', views.TweetViewSet.as_view()),
    path('api/posts/comment/', views.CommentViewSet.as_view()),
    # path('tweet/<int:tweet_id>/like/', views.LikeTweetView.as_view(), name='like_tweet'),


]
