import logging
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.urls import reverse
from django.contrib.auth import get_user_model


def send_verification_email(user_id):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=user_id)
        html_content = get_template('email.html').render({'uuid': reverse('verify', kwargs={'uuid': str(user.verification_uuid)})})
        text_content = 'This is an important message.'
        msg = EmailMultiAlternatives('Подтверждение вашего аккаунта', text_content, settings.EMAIL_HOST_USER, [user.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    except UserModel.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)