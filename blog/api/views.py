from rest_framework.generics import ListAPIView, RetrieveAPIView

from ..models import Post
from .serializers import PostSerializers


class PostListView(ListAPIView):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializers


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
