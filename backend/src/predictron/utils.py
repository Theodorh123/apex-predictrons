# from django.core.mail import EmailMessage
# from predictron.models import User
# import datetime


# class Util:
#     @staticmethod
#     def send_email(data):
#         email = EmailMessage(
#             subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
#         email.content_subtype = "text/html"
#         email.send()
    
#     @staticmethod
#     def validate_username(username):
#         user = None
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             return None
#         if user != None:
#             return username

#     @staticmethod
#     def checkEmail(email):
#         user = None
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             return None
#         if user != None:
#             return email

#     @staticmethod
#     def generate():
#         import random
#         alpnum = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
#         ls = list(alpnum)
#         random.shuffle(ls)
#         return "".join(ls[0:5])
    
  
  
    

    