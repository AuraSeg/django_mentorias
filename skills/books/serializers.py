from rest_framework import serializers

from books.models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id','first_name','last_name', 'birth_date', 'status')
        #fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['author'] = AuthorSerializer(instance.author).data
        return response