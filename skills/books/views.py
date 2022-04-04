from django.shortcuts import get_object_or_404

from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from books.models import Book, Author

from books.serializers import AuthorSerializer, BookSerializer

# Create your views here.
class RetrieveBooks(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        books_list = Book.objects.all()
        serializer = BookSerializer(books_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveAuthors(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        author_list = Author.objects.all()
        serializer = AuthorSerializer(author_list, many=True)
        return Response(serializer.data)


class CreateAuthor(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
#        author_obj = Author.objects.create(
#            first_name = request.data.get('first_name',''),
#            last_name = request.data.get('last_name',''),
#            birth_date = request.data.get('birth_date','')
#        )
        data = request.data
        serializer = AuthorSerializer(data=data)
        serializer.is_valid(raise_exception=True)
# Metodo de validacion no recomendado porque no siempre indica el error correcto 
#        if serializer.is_valid():
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateBook(APIView):
    permission_classes =(AllowAny,)

    def post(self, request):
#        book_obj = Book.objects.create(
#            name = request.data.get('name',''),
#            isbn = request.data.get('isbn',''),
#            publisher_date = request.data.get('publisher_date','1700-01-01'),
#            author_id =request.data.get('author_id',1)
#        )
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RetrieveAuthorAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, author_id):
        author_obj = Author.objects.get(id=author_id)
        serializer = AuthorSerializer(author_obj)
        return Response(serializer.data)


class RetrieveBookAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, book_id):
        book_obj = get_object_or_404(Book, pk=book_id)
        #book_obj = Book.objects.get(id=book_id)
        serializer = BookSerializer(book_obj)
        return Response(serializer.data)