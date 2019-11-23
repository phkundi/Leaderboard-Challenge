from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic.base import TemplateView

from .functions import add_donations
from .models import Entry

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe_public_key = settings.STRIPE_PUBLIC_KEY

# Create your views here.

def homepage(request):
    
    donation_list = Entry.objects.all().filter(paid=True).order_by('amount').reverse()
    donation_count = len(donation_list)

    return render(
                    request, 
                    'web/index.html', 
                    {
                        'key':stripe_public_key, 
                        'list':donation_list,
                        'donation_count':donation_count

                    }
                )
    
def ranking(request):
    
    if request.method == 'POST':
        donation_id = request.POST.get('don_id')

        user_donation = Entry.objects.get(pk=donation_id)
        user_donation.paid = True
        user_donation.save()

        msg = f'Thank you for participating with'
        donation_list = Entry.objects.all().filter(paid=True).order_by('amount').reverse()

        donation_total = add_donations(donation_list)
        donation_count = len(donation_list)

        # Calculate User Rank
        rank = 1
        user_rank = None
        for d in donation_list:
            if d.id == int(donation_id):
                user_rank = rank
                break
            rank += 1
        
        # redirect to ranking
        return render(
                        request, 
                        'web/ranking.html', 
                        {
                            'list':donation_list, 
                            'msg':msg, 
                            'donation_amount': user_donation.amount,
                            'donation_total': donation_total,
                            'donation_count': donation_count,
                            'user_rank': user_rank
                        }
                    )

    else:
        # for production
        if request.user.is_superuser:
            donation_list = Entry.objects.all().filter(paid=True).order_by('amount').reverse()

            donation_total = add_donations(donation_list)
            donation_count = len(donation_list)

            return render(
                            request, 
                            'web/ranking.html', 
                            {
                                'donation_total': donation_total, 
                                'donation_count': donation_count, 
                                'list': donation_list
                            }
                        )
        else:
            return redirect('homepage')


def payment_view(request):
    if request.method == 'POST':
        # get form data
        donation_amount = request.POST.get('amount')
        donation_name = request.POST.get('name')
        donation_message = request.POST.get('message')

        # change name to anonymous if not provided
        if not donation_name:
            donation_name = 'Anonymous'

        # format donation amount for ranking & database
        donation_amount_display = donation_amount.replace(',','.')

        # format donation amount for stripe processing
        donation_amount = donation_amount.replace(',','.')
        donation_amount = round(float(donation_amount),2)
        donation_amount = int(donation_amount*100)
        donation_amount_display = donation_amount/100

        # create payment intent
        intent = stripe.PaymentIntent.create(
            amount=donation_amount,
            currency='usd',
            payment_method_types=['card']
        )

        # add donation to database
        new = Entry(
            name = donation_name,
            amount = round((float(donation_amount_display)),2),
            message = donation_message
        )
        new.save()
                
        return render(
                        request, 
                        'web/payment.html', 
                        {
                            'client_secret':intent.client_secret, 
                            'key':stripe_public_key,
                            'donation_id':new.id,
                            'amount':donation_amount_display
                        }
                    )
    
    else:
        return redirect('homepage')

class PrivacyView(TemplateView):
    template_name = 'web/privacy.html'