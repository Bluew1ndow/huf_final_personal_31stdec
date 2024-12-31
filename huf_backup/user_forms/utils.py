import pyotp
from datetime import timedelta, datetime
from django.conf import settings
from django.core.mail import send_mail

def send_otp(request):
    print("Sending OTP")
    totp = pyotp.TOTP(pyotp.random_base32(), interval=60)
    otp = totp.now()
    request.session['otp_secret_key'] = totp.secret
    valid_until = datetime.now() + timedelta(minutes=5)
    request.session['otp_valid_until'] = str(valid_until)

    subject = 'Welcome to HUF'
    message = f'Your One Time Password is {otp}'
    from_email = settings.EMAIL_HOST_USER
    recipient = [request.session['email_address']]

    try:
        send_mail(subject, message, from_email, recipient)
        print(f"Your OTP is {otp}")
    except Exception as e:
        print(f"Error sending email: {e}")
