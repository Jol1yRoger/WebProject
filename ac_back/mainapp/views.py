from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course, Enrollment, Category
from .serializers import CourseSerializer, EnrollmentSerializer, CategorySerializer

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny

class CourseList(APIView):

    def get(self, request):
        courses = Course.objects.all()
        category = request.query_params.get('category')
        if category:
            courses = courses.filter(category__id=category)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class EnrollCourse(APIView):
    def post(self, request, course_id):
        course = Course.objects.get(id=course_id)
        enrollment = Enrollment(user=request.user, course=course)
        enrollment.save()
        return Response(status=status.HTTP_201_CREATED)




class CreateUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
def add_category(request):
    name = request.data.get('name')
    description = request.data.get('description')
    imageLink = request.data.get('imageLink')

    if not name or not description or not imageLink:
        return Response({'error': 'You must provide name, description and link to image for the category'}, status=status.HTTP_400_BAD_REQUEST)
    
    category = Category.objects.create(name=name, description=description, imageLink=imageLink)
    
    return Response({'success': 'Category created successfully'}, status=status.HTTP_201_CREATED)
