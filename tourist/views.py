from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from .serializers import touristSerializer

from rest_framework import status

from tourist.models import tourist
from tourist.models import Review


# Get all tours and reviews 
@api_view (['GET'])
def getTourist_place(request):
    tours=tourist.objects.all()
    serializer =touristSerializer(tours, many=True)
    return Response(serializer.data)


# Get Tour
@api_view(['GET'])
def getTouristPlacesbyUser(request,user):
    try:
        tours = tourist.objects.filter(user_id =user)

        if(tours):
            serializer =touristSerializer(tours, many=True)
            return Response(serializer.data)
        else:
            return Response("NO TOUR FOR THE USER")
    except:
        return Response(" NO CONTENT FOUND")

    
# Create tour
@api_view(['POST'])
def tourist_place_create(request, format=None):
    serializer = touristSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
       
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    

# Get single tour
@api_view(['GET'])
def getTourDetail (request, id):
    try:
        tour =tourist.objects.get(pk=id)
    except tourist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer =tourist(tour, many =False)
    return Response(serializer.data)


# update single tour
@api_view(['PUT'])
def tourist_places_update(request,id, format =None):
    try:
        tour = tourist.objects.get(pk = id)
    except tourist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer =touristSerializer(tour, data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete single tour
@api_view(['DELETE'])
def delete_tour(request,id):
    try:
        tour =tourist.objects.get(pk=id)
    except tourist.DoesNotExist:
        return Response(status =status.HTTP_404_NOT_FOUND)
    tour.delete
    return Response('tour deleted successfully' , status = status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createReviewForTour(request,id):
    user =request.user
    tour =tourist.objects.get(pk=id)
    data =request.data


# Create your views here.
