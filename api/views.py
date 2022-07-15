from django.contrib.auth.models import User, Group
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from api.models import Post, Comment
from api.serializers import UserSerializer, GroupSerializer, PostSerializer, CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    @action(detail=True, methods=['GET', 'POST'])
    def comments(self, request, pk):

        if request.method == 'POST':
            comment_instance = Comment(
                post_id=pk,
                user_id=request.data.get('user_id'),
                body=request.data.get('body')
            )
            comment_instance.save()
            serializer = CommentSerializer(comment_instance, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            comment_instances = Comment.objects.filter(post_id=pk).all()
            serializer = CommentSerializer(comment_instances, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
