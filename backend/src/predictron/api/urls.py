# from django.conf.urls import url
# from django.urls import include, path
# from rest_framework.routers import DefaultRouter

# from eventapp.api.views import EventBookingView, EventView, RegisterView, VerifyEmail, delete_event, event_booking_view, user_view, users

# router = DefaultRouter()
# router.register('events', EventView, basename='events')
# router.register('eventbookings', EventBookingView, basename='eventbookings')


# app_name = 'predictron'


# urlpatterns = [
#     path('', include(router.urls)),
#     path('register/', RegisterView.as_view(), name="register"),
#     path('verify-email/', VerifyEmail.as_view(), name="verify-email"),
#     path('users/', users, name="users"),
#     path('event-book/', event_booking_view, name="event-book"),
#     path('event-book/<int:pk>/', event_booking_view, name="event-book"),
#     path('remove_user_book/', event_booking_view, name="event-book"),
#     path('delete_event/', delete_event, name="delete_event"),
#     path('user/<str:username>/', user_view, name="user-detail"),
# ]
