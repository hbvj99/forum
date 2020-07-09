from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
import discussions.discussion_api
from django.conf.urls.static import static, settings

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('index/', views.homepage, name='homepage'),
    path('api-doc/', views.api_doc, name='api-doc'),
    path('discussions/new/', views.new_discussion, name='new_discussion'),
    path('discussion/<slug:title>/', views.discussion_detail, name="detail"),
    path('discussion/<slug:title>/edit/', views.discussion_update, name='discussion_update'),
    path('discussion/<slug:title>/delete/', views.discussion_delete, name='discussion_delete'),
    path('vote/', views.add_vote, name='add_vote'),

    path('api/v1/token/', obtain_auth_token, name='api_token_auth'),  # Get token
    path('api/v1/discussion/', discussions.discussion_api.DiscussionViewSet.as_view()),  # Discussion REST API
    path('api/v1/discussion/new/', discussions.discussion_api.DiscussionCreate.as_view()),  # Create discussion API
    path('api/v1/discussion/<slug:slug>/', discussions.discussion_api.DiscussionRetrieveUpdateDestroy.as_view()), # Update, delete discussion API
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
