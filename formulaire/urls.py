from django.urls import path
from .views import controleform1,controleform2, controleform3,contactView

urlpatterns = [
    path('form1/', controleform1, name='controleform1'),  
    path('form2/', controleform2, name='controleform2'), 
    path('form3/', controleform3, name='controleform3'), 
    path('contact/', contactView, name='contact'),  # URL for the contact form
    

]

