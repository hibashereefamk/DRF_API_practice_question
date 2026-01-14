from .model import Author,Book
from rest_framework import serializers

# Q1
class Bookserializer(serializers.ModelSerializer):
    
    class Meta:
        model=Book
        fields='__all__'
# Q2
class Bookserializer(serilaizers.ModelSerializer):
    author=serializers.CharField(source='author.name',read_only=True)
    class Meta:
        model=Book
        fields=['id','title','author']
# ?q3
class Bookserializer(serilaizers.ModelSerializer):
    
    class Meta:
        model=Book
        fields='__all__'
        depth=1
# q4
class AuthorSerializer(serilaizers.modelserializer):
    
    class meta:
        model=Author
        fields='__all__'
        
class Bookserializer(serilaizers.ModelSerializer):
    author=AuthorSerializer(read_only=True)
    class Meta:
        model=Book
        fields=['id','title','author']
        
# Q5
class Bookserializer(serilaizers.ModelSerilaizer):
    
    class Meta:
        model=Book
        fields='__all__'
class Authorserializer(serilaizers.ModelSerilaizer):
    books=Bookserializer(many=True,read_only=True)
    class Meta:
        model=Author
        fields=['id','name','books']
        
# Q6
class Bookserializer(serilaizers.ModelSerilaizer):
    author=models.SlugRelatedField(read_only =True,slug_field='slug')
    class Meta:
        model=Book
        fields=['id','title','author']
# q7
class Bookserializer(serilaizers.ModelSerilaizer):
    author=serializers.SlugRelatedField(
        author=serializers.objects.all(),slug_field='slug'
        )
   
    class Meta:
        model=Book
        fields=['title','author']
        
#  q8      
class BookSerilaizer(serilaizers.ModelSerilaizer):
    author_name=serilaizers.CharField(
        source ='author.name',read_only='slug')
        
    author=serilaizer.PrimaryKeyRelatedField(
        Queryset=Author.objects.all(),
        write_only =True)
        
class Meta:
    model=Book
    fields =['id','name','author','author_name']
