from rest_framework import serializers
from user.models import NewUser

from .models import tourist, Review

class touristSerializer(serializers.ModelSerializer):
    # reviews=serializers.SerializerMethodField(read_only = True)

    class Meta:
        model =tourist
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model =Review
        field ="__all__"

def get_reviews(self, obj):
    reviews =obj.review_set.all()
    serializer = ReviewSerializer(reviews,many =True)
    return serializer.data