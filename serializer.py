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


Q1. SerializerMethodField (Tax calculation)
class ProductSerializer(serializer.modelSerializer):
    price_with_tax=serializer.SerializerMethodField()
    class Meta:
        model=Product
        field=['id','name','price','price_with_tax']
        
    def get_price_with_tax(self,obj):
        return obj.price*1.18
# -q2. read_only=True-
class UserProfileserilaizer(serializers.modelSerializer):
    
    class Meta:
        model=User
        field=['id','usrname','email','created_at']
        extra_kwargs={
            'created_at':{'read_only':True}
      }
#   Q3. Conditional SerializerMethodField     
class Studentserializer(serializers.modelSerializer):
    result=serializers.SerializerMethodField()
    class Meta:
        model=Student
        field=['id','name','mark','result']
        
    def get_result(self,obj):
        return "Pass" if obj.marks >= 40 else "Fail"
        #Q4. extra_kwargs (write-only & required) 
class EmployeeSerializer(serializers.modelSerialize):
    
    class Meta:
        model=Employee
        fields=['id','name','email','salary']
        extra_kwargs={
            'salary':{'write_only':True},
            'email':{'require':True}
        }
     
        #Q5. Combine ALL (MethodField + read_only + extra_kwargs) 
class Orderserializers(serializers.modelSerializers):
    amount_in_rupees=serializers.serialzerMathodField()
    
    class Meta:
        model=Order
        Field=['order_id','amount','created_at','amount_in_rupees']
        extra_kwargs={
            'created_at':{'read_only':True},
            'order_id':{'require':True}
        }
    def get_amount_in_rupees(self,obj):
        return f"₹{obj.amount}"
    
        # Q6. Password security (write_only)
        
    class UserSerializer(serializer.ModelSerializer):
        class Meta:
            model=Employee
            fields='__all__'
            extra_kwargs={
                'password': {'write_only': True}
                }
# Q7. Dynamic output (Discount logic)
class  SubscriptionSerilaizer(serializer.ModelSerializer):
    discounted_price=serializers.serializerMethodField()
    class Meta:
        model =Subscription
        field=['plan','price','discounted_price']
    def get_discounted_price(self,obj):
        if obj.plan =='premium':
            return obj.price * 0.20
        return obj.price
        
# Q8. Namespace Versioning
from django.urls import path
from .models import User

app_name='v1'
            
urlspattern=[
            path('users/',UserView.asview(),name=users)
            ]
# main.py

path('api/v1',include('api.v1.urls'))
path('api/v1',include('api.v2.urls'))

# Q9. Accept-Header Versioning

REST_FRAMEWORK={
    'DEFAULT_VERSIONING_CLASS':
        'rest_framework.versioning.acceptHeaderVersioning',
    'DEFAULT_VERSION':'1.0',
    'ALLOWED_VERSIONS':['1.0','2.0']
} 
# Q10. Different serializers per version
class UserView(APIView):
    def get_serilaizer_class(self):
        if self.request.version =='2.0':
            return UserDetailSerializer
        return UserSerializer
