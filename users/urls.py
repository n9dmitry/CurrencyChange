from django.urls import path
from users.views import registration

app_name = 'users'

urlpatterns = [
    path('registration/', registration, name='registration'),

]