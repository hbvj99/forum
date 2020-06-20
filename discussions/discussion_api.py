from rest_framework.response import Response
from discussions.serializers import DiscussionSerializer
from discussions.models import Discussion
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError


class DiscussionPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class DiscussionViewSet(ListAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('user', 'title', 'content', 'category', 'tags')
    search_fields = ('title', 'content', 'category', 'tags')
    pagination_class = DiscussionPagination


class DiscussionCreate(CreateAPIView):

    serializer_class = DiscussionSerializer

    def create(self, request, *args, **kwargs):
        try:
            discussion = request.data.get('user_id')
            if discussion is None:
                raise ValidationError({'response': 'user_id field is required.'})
        except ValueError:
            raise ValidationError({'response': "user_id isn't valid"})
        if request.data.get('user_id') != request.user.id:
            raise ValidationError({'response': "You don't have permission. Check if your user_id is correct."})
        return super().create(request, *args, **kwargs)


class DiscussionRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):

    queryset = Discussion.objects.all()
    lookup_field = 'slug'
    serializer_class = DiscussionSerializer

    def delete(self, request, slug, *args, **kwargs):
        post = Discussion.objects.get(slug=slug)
        update_usr = request.user
        if post.user != update_usr:
            return Response({'response': "You don't have permission to delete this discussion."})
        else:
            discussion_id = request.data.get('slug')
            response = super().delete(request, *args, **kwargs)
            if response.status_code == 204:
                from django.core.cache import cache
                cache.delete('discussion_data_{}'.format(discussion_id))
            return response

    def update(self, request, slug, *args, **kwargs):
        post = Discussion.objects.get(slug=slug)
        update_usr = request.user

        if request.data.get('user_id'):
            return Response({'response': "Including user_id as a field is not supported."})
        if post.user != update_usr:
            return Response({'response': "You don't have permission to edit this discussion."})
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            discussion = response.data
            cache.set('discussion_data_{}'.format(discussion['slug']), {
                'user': discussion['user'],
                'title': discussion['title'],
                'updated': discussion['updated'],
                'timestamp': discussion['timestamp'],
                'content': discussion['content'],
                'img': discussion['img'],
                'category': discussion['category'],
                'tags': discussion['tags'],
                'views': discussion['views'],
                'votes': discussion['votes'],
            })
        return response


