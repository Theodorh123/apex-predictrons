# from django.conf import settings
# from django.contrib.sites.shortcuts import get_current_site
# from rest_framework import generics, permissions, status, viewsets
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# # from rest_framework.views import APIView

# from eventapp.api.serializers import EventBookingSerializer, EventSerializer, UserSerializer
# from eventapp.models import Event, EventBooking, TokenCode, User
# # from eventapp.permissions import IsAuthOrReadOnly
# from eventapp.utils import Util


# class EventView(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer


# class EventBookingView(viewsets.ModelViewSet):
#     queryset = EventBooking.objects.all()
#     serializer_class = EventBookingSerializer


# class RegisterView(generics.GenericAPIView):
#     """ Create a new user and send confirm email link """
#     serializer_class = UserSerializer

#     def post(self, request):
#         user = request.data
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         data = []
#         if Util.checkEmail(request.data.get('email')) != None:
#             data['error_message'] = 'That email is already in use.'
#             data['response'] = 'Error'
#             return Response({
#                 'error_message': 'That email is already in use.'
#             }, status=status.HTTP_400_BAD_REQUEST)

#         serializer.save()
#         user_data = serializer.data
#         user_data['is_success'] = True
#         user = User.objects.get(username=user_data['username'])
        
#         # Geneate code automatically
#         code = Util.generate()
        
#         # Then save the generated code to ToeknCode model for the email confirmation
#         token = TokenCode(user=user, code=code)
#         token.save()
        
#         # Get current url, build email body and data
#         current_site = get_current_site(request).domain
#         absurl = 'http://'+current_site+"/api/verify-email/" + \
#             "?token="+code+"&ui="+str(user.id)
#         email_body = 'Hi '+user.username + \
#             ' Use the link below to verify your email \n' + absurl
#         data = {'email_body': email_body, 'to_email': user.email,
#                 'email_subject': 'Verify your email'}

#         # Send functionality
#         Util.send_email(data)
#         return Response(user_data, status=status.HTTP_201_CREATED)


# class VerifyEmail(generics.GenericAPIView):
#     """ Verify token code sent to a user's email address and activate the email """
    
#     def get(self, request):
#         t = request.GET.get('token')
#         # Check to ensure user (uid) or token (code) model does exist in our database system
#         try:
#             user = User.objects.get(id=request.GET.get('ui'))
#             token = TokenCode.objects.get(user_id=user.id)
#             if token.code == t:
#                 if not user.is_active:
#                     token.delete()
#                     user.is_active = True
#                     user.save()
#         except User.DoesNotExist or Token.DoesNotExist:
#             return Response({'error': 'User does not exist or Token code is not valid'},
#                             status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response({'email': 'Successfully activated'},
#                             status=status.HTTP_200_OK)


# @api_view(['POST', 'GET', 'DELETE'])
# def event_booking_view(request, pk=None):
#     if request.method == "POST":
#         """ User books event - Event Registration """
#         user = None
#         event = None
#         try:
#             uid = request.data.get('user_id')
#             eid = request.data.get('event_id')
#             ticket = request.data.get('ticket')
#             phone_number = request.data.get('phone_number')
#             time = request.data.get('time')
#             event = Event.objects.get(id=eid)
#             user = User.objects.get(id=uid)
            
#             # Check whether event room is full or not
#             length = Util.lengthEventBooking(eid)
#             if int(event.room_capacity) <= int(length):
#                 return Response({'error': 'Sorry, room is alreay full', 'status_code': 800})
#             books = EventBooking.objects.filter(event_id__exact=event.id)
#             user_books = EventBooking.objects.filter(user_id__exact=user.id)
#             timeLists = []
#             for book in user_books:
#                 timeLists.append(book.event.time)

#             # Check whether the user has already booked the event or not
#             if Util.checkIfUserHasBook(books, user.id):
#                 return Response({
#                     'result': "Look like you have booked the event already!",
#                     'status_code': 700
#                 })

#             # if event.time in timeLists:
#             #     return Response({
#             #         'result': f'Sorry, you can\'t book an event that conflicts with {event.time} time',
#             #         'status_code': 670,
#             #         'time': event.time
#             #     })
#             # Check if an selected event's time the user tries to book is conflicted with other event time
#             if time in timeLists:
#                 return Response({
#                     'result': f'Sorry, you can\'t book an event that conflicts with {time} time',
#                     'status_code': 670,
#                     'time': time
#                 })

#             # Many to Many relationship
#             # Event adds attendees (user) and save user to EventBooking model
#             event.attendees.add(user)
#             book = EventBooking(user=user, event=event,
#                                 ticket=ticket, phone_number=phone_number, time=time)
#             book.save()
#             return Response({
#                 'result': "Booked successfully",
#             }, status=status.HTTP_201_CREATED)
#         except User.DoesNotExist:
#             return Response({
#                 'error': 'User does not exist',
#             }, status=status.HTTP_404_NOT_FOUND)

#         except Event.DoesNotExist:
#             return Response({
#                 'error': 'Event does not exist',
#             }, status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         """ Retrieve user book history with user pk if that user has booked any events or not """
#         try:
#             uid = pk
#             user = User.objects.get(id=uid)
#             books = EventBooking.objects.all().filter(user_id__exact=user.id)
#             data = []
#             for book in books:
#                 data.append({
#                     'ticket': book.ticket,
#                     'book_id': book.id,
#                     'user_id': book.user_id,
#                     'event_id': book.event_id,
#                     'event_title': book.event.title,
#                     'event_location': book.event.location,
#                     'event_speaker': book.event.speaker,
#                     'event_tagline': book.event.tagline,
#                 })
#         except User.DoesNotExist:
#             return Response({'error': 'User does not exist!'}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response(data, status=status.HTTP_200_OK)

#     if request.method == 'DELETE':
#         """ User is able to cancel any events the user has booked """
#         user = None
#         event = None
#         book_id = request.data.get('book_id')
#         try:
#             book = EventBooking.objects.get(id=book_id)
#             event = Event.objects.get(id=book.event_id)
#             user = User.objects.get(id=book.user_id)
            
#             # Remove attendee relate to user and delete an existing book 
#             event.attendees.remove(user)
#             book.delete()
#         except User.DoesNotExist:
#             return Response({
#                 'error': 'User does not exist',
#             }, status=status.HTTP_204_NO_CONTENT)
#         except Event.DoesNotExist:
#             return Response({
#                 'error': 'Event does not exist',
#             }, status=status.HTTP_204_NO_CONTENT)
#         except EventBooking.DoesNotExist:
#             return Response({
#                 'error': 'Event booking does not exist',
#             }, status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response({
#                 'is_success': True,
#             }, status=status.HTTP_200_OK)


# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def user_view(request, username):
#     data = {}
#     if request.method == 'GET':
#         """ Retrieve a exiting user with username """
#         user = None
#         try:
#             user = User.objects.get(username=username)
#             data['username'] = user.username
#             data['first_name'] = user.first_name
#             data['last_name'] = user.last_name
#             data['email'] = user.email
#             data['address'] = user.address
#             data['city'] = user.city
#             data['is_superuser'] = user.is_superuser
#             data['is_staff'] = user.is_staff
#             data['pk'] = user.pk
#         except User.DoesNotExist:
#             return Response({'error': 'User does not exist!'},
#                             status=status.HTTP_404_NOT_FOUND)
#         if user != None:
#             return Response(data, status=status.HTTP_200_OK)

# @api_view(['GET', ])
# def users(request):
#     """ Retrieve all users """
#     data = []

#     if request.method == "GET":
#         users = User.objects.all()
#         for user in users:
#             data.append({
#                 'username': user.username,
#                 'name': user.first_name + " " + user.last_name,
#                 'email': user.email,
#                 'address': user.address,
#                 'city': user.city,
#                 'is_staff': user.is_staff,
#                 'pk': user.pk,
#             })

#         return Response(data, status=status.HTTP_200_OK)

# @api_view(['DELETE', ])
# def delete_event(request):
#     """ Superuser can delete existing events """
#     try:
#         event_id = request.data.get('event_id')
#         event = Event.objects.get(id=event_id)
#         event.delete()
#     except Event.DoesNotExist:
#         return Response({
#             'error': 'Event does not exist',
#         }, status=status.HTTP_204_NO_CONTENT)
#     else:
#         return Response({
#             'is_success': True,
#         }, status=status.HTTP_200_OK)