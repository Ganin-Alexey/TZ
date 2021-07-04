from django.contrib.auth import get_user_model
from django.http import Http404

# Create your views here.
from django.shortcuts import redirect
from django.views import View



class VerifyView(View):
    def get(self, request, uuid):
        try:
            user = get_user_model().objects.get(verification_uuid=uuid, is_verified=False)
        except get_user_model().DoesNotExist:
            raise Http404("User does not exist or is already verified")
        user.is_verified = True
        user.save()
        return redirect('home')