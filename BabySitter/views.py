from rest_framework import viewsets
from .serializer import UserSerializer,NannySerializer,ReservationSerializer
from .models import User,Nanny,Reservation

# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class NannyView(viewsets.ModelViewSet):
    serializer_class = NannySerializer
    queryset = Nanny.objects.all()

class ReservationView(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
