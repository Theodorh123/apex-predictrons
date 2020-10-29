# from rest_framework import serializers
# from rest_framework.response import Response

# from eventapp.models import Event, User, EventBooking


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'first_name', 'last_name',
#                   'password', 'address', 'city')
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }

#     def save(self):
#         user = User(
#             email=self.validated_data['email'],
#             username=self.validated_data['username'],
#             first_name=self.validated_data['first_name'],
#             last_name=self.validated_data['last_name'],
#             address=self.validated_data['address'],
#             city=self.validated_data['city'],
#         )
#         user.is_active = False
#         user.set_password(self.validated_data['password'])
#         user.save()


# class EventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Event
#         fields = ('id','title', 'time', 'date', 'location',
#                   'room_capacity', 'speaker', 'tagline', 'attendees')


# class EventBookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EventBooking
#         fields = ('user', 'event', 'time', 'ticket', 'phone_number')
