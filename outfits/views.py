from rest_framework import generics 
from .serializer import PostSerializer
from .models import Outfits

class PostLists(generics.ListCreateAPIView):
    queryset = Outfits.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outfits.objects.all()
    serializer_class = PostSerializer