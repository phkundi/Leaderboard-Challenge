from django.shortcuts import redirect
import stripe

def create_charge(amount, token):

    donation_amount = amount
    donation_amount = round(float(donation_amount),2)

    donation_amount = int(donation_amount*100)

    if donation_amount >= 100:
        try:
            charge = stripe.Charge.create(
                amount=donation_amount,
                currency='usd',
                description='Waste your money',
                source=token
            )

        except:
            return redirect('homepage')


def add_donations(donation_list):
    total_amount = 0
    for d in donation_list:
        total_amount = total_amount + d.amount
    return total_amount

def create_intent(amount):
    donation_amount = amount
    donation_amount = round(float(donation_amount),2)
    donation_amount = int(donation_amount*100)

    if donation_amount >= 100:
        try:
            intent = stripe.PaymentIntent.create(
                amount=donation_amount,
                currency='usd',
                description='Waste of money'
            )

            return intent

        except:
            return redirect('homepage')