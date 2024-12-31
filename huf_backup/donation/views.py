import stripe
import logging
import json
import time
from datetime import datetime
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import donation_table

# Configure logging
logger = logging.getLogger('file_log')

stripe.api_key = "sk_test_51PIcMaSDzGtWFPx2dhRMeupgfB4tnC1oCTPI4bY5PEvttyYuxnSXyV8zAHPws3T1uA77bWTbEIE4ztu47DxOyGhe00gDeBYisg"
endpoint_secret = 'whsec_af932a8c451bd7aab2c3f06d0fdc1e9ddb448a9a4991a688ea20285a89a4fd92'

def success(request):
    return JsonResponse({"message": "Donation successful"})

@csrf_exempt
def create_checkout_session(request):
    start_time = time.time()
    logger.info("\nRequest to create a Stripe checkout session")
    logger.info(f"Time: {datetime.now()}")

    # logger.info("Email: %s, Phone: %s, Address: %s", email_address, phone_number, address)

    try:
        if request.method != "POST":
            return JsonResponse({"message": "Invalid request method"}, status=405)

        data = json.loads(request.body.decode('utf-8'))

        email_address = str(data.get('email_address'))
        phone_number = str(data.get('phone_number'))
        address = str(data.get('address'))
        donation_amount = data.get('donation_amount')
        message = str(data.get('message', ''))
        receive_updates = data.get('receive_updates')

        logger.info("Email: %s, Phone: %s, Address: %s", email_address, phone_number, address)

        # Email validation
        if not email_address or '@' not in email_address:
            return JsonResponse({"message": "Invalid email address"}, status=400)

        # Phone number validation
        if not phone_number.isdigit() or len(phone_number) < 10 or len(phone_number) > 15:
            return JsonResponse({"message": "Phone number must be between 10 and 15 digits and contain only numbers"}, status=400)

        # Donation amount validation
        try:
            donation_amount = float(donation_amount)
            if donation_amount <= 0:
                return JsonResponse({"message": "Donation amount must be a positive number"}, status=400)
        except (ValueError, TypeError):
            return JsonResponse({"message": "Donation amount must be a valid number"}, status=400)

        # Create a Stripe Checkout Session
        amount_in_cents = int(donation_amount * 100)  # Convert to cents
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": amount_in_cents,
                        "product_data": {
                            "name": "Donation",
                        },
                    },
                    "quantity": 1,
                }
            ],
            metadata={
                "email_address": email_address,
                "phone_number": phone_number,
                "address": address,
                "message": message,
                "receive_updates": str(receive_updates),
            },
            mode="payment",
            success_url="http://www.google.com/",       #test
            cancel_url="http://www.yahoo.com/",         #test
        )

        logger.info("Stripe checkout session created successfully")
        logger.info(f"Time taken: {time.time() - start_time} seconds")
        return JsonResponse({"url": session.url})

    except Exception as e:
        logger.error(f"Error while creating Stripe checkout session: {e}")
        return JsonResponse({"message": "An error occurred while creating the Stripe session", "error": str(e)}, status=500)

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
    endpoint_secret = 'whsec_af932a8c451bd7aab2c3f06d0fdc1e9ddb448a9a4991a688ea20285a89a4fd92'

    # Verify the webhook signature to ensure the event is from Stripe
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError as e:
        logger.error(f"Invalid payload: {e}")
        return JsonResponse({"message": "Invalid payload"}, status=400)
    except stripe.error.SignatureVerificationError as e:
        logger.error(f"Invalid signature: {e}")
        return JsonResponse({"message": "Invalid signature"}, status=400)

    # Handle the event type you are interested in
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        # Extract metadata and Stripe session information
        email_address = session.get("metadata", {}).get("email_address")
        phone_number = session.get("metadata", {}).get("phone_number")
        address = session.get("metadata", {}).get("address")
        donation_amount = session.get("amount_total") / 100  # Convert from cents to dollars
        message = session.get("metadata", {}).get("message", "")
        receive_updates = session.get("metadata", {}).get("receive_updates", False)
        stripe_id = session.get("id")

        # Log details for debugging
        logger.info(f"Donation completed for {email_address} with amount {donation_amount}")
        logger.info(f"Stripe ID: {stripe_id}, Phone: {phone_number}, Address: {address}, Message: {message}")

        # Create a new donation record in the database
        try:
            donation = donation_table.objects.create(
                email_address=email_address,
                phone_number=phone_number,
                address=address,
                donation_amount=donation_amount,
                message=message,
                receive_updates=receive_updates,
                stripe_id=stripe_id,  # Store the Stripe session ID
            )

            logger.info(f"Donation record for {email_address} created successfully")
        except Exception as e:
            logger.error(f"Error creating donation record: {e}")
            return JsonResponse({"message": "Failed to create donation record"}, status=500)

    # Return a success response to Stripe
    return JsonResponse({"message": "Webhook received"}, status=200)