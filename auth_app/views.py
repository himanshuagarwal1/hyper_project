from django.contrib.auth import get_user_model
from .models import Organization
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegisterView(APIView):



    def post(self, request):
        data = request.data
        org_id  = data.get('organization_id', None)
        invite_code =  data.get("invite_code", None)
        if not org_id and not invite_code:
            return Response({"message": "User registration unsucessfull."})
        
        if org_id:
            org = Organization.objects.get(id=org_id)
        elif invite_code:
            org = Organization.objects.get(invite_code=invite_code)
        if not org:
            return Response({"message": "User registration unsucessfull."})


        try:
            User.objects.create_user(
            username=data['username'],
            password=data['password'],
            role=data['role'],            
            organization_id= org.id
        )
            return Response({"message": "User registered successfully."})

        except:
            return Response({"message": "User registration unsucessfull."})

class LoginView(APIView):
    def post(self, request):
        user = User.objects.get(username=request.data['username'])
        if user.check_password(request.data['password']):
            refresh = RefreshToken.for_user(user)
            return Response({"refresh": str(refresh), "access": str(refresh.access_token)})
        return Response({"error": "Invalid credentials"}, status=401)
