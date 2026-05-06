from django.shortcuts import render
from django.http import HttpResponse
from .models import Logo
from .models import WhatOurClientsSay
from .models import NewOnOurReel
from .models import TeamMember
from .models import DigitalImpactStory
from .models import CreativeContentPortfolio
from .models import AddYourWords
from .models import SuccessStories
import csv
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import ContactLead
from django.conf import settings
from .models import OurBlog
from django.shortcuts import render, get_object_or_404
from .models import ReadBlog
 
 




# Create your views here.

# def home(request):
#     def home(request):
#     logos = Logo.objects.all()
#     return render(request, 'index.html', {'logos': logos})

def home(request):
    logos = Logo.objects.all()
    clients = WhatOurClientsSay.objects.all()
    return render(request, 'index.html', {
        'logos': logos,
        'clients': clients
    })


# def services(request):
#     return render(request, 'services.html')





def services(request):
    reels = NewOnOurReel.objects.all()

    context = {
        'reel1': reels[0] if len(reels) > 0 else None,
        'reel2': reels[1] if len(reels) > 1 else None,
    }

    return render(request, 'services.html', context)


def team(request):
    members = TeamMember.objects.all()
    return render(request, 'team.html', {'members': members})



def recognition(request):
    return render(request, 'reco.html')


def portfolio(request):
    stories = DigitalImpactStory.objects.all()
    items = CreativeContentPortfolio.objects.all()
    return render(request, 'Portfolio.html', {
        'stories': stories,
        'items': items
         
        })




def review_page(request):
    reviews = AddYourWords.objects.all()
    stories = SuccessStories.objects.all()
    return render(request, 'review.html',
                   {
                     'reviews': reviews,
                     'stories': stories
                   })


def blog(request):
      blogs = OurBlog.objects.all().order_by('-date')
      return render(request, 'blog.html',{'blogs': blogs})
    



def contact_page(request):
    return render(request, 'contact.html')





def submit_contact(request):
    if request.method == "POST":
        name = request.POST.get('name') or request.POST.get('Name')
        email = request.POST.get('email') or request.POST.get('Email')
        mobile = request.POST.get('mobile') or request.POST.get('Mobile')
        subject = request.POST.get('subject') or ""
        message = request.POST.get('message') or request.POST.get('message')

        # ✅ Save to DB
        ContactLead.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            subject=subject,
            message=message
        )

        # ✅ Save to CSV
        with open('contacts.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, mobile, subject, message])




        if not name:
          return HttpResponse("Name is required ❌")      
        # ✅ Send Email
        send_mail(
            subject=f"New Contact: {name}",
            message=f"Name: {name}\nEmail: {email}\nMobile: {mobile}\nSubject: {subject}\nMessage: {message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

        return redirect('/contact/?success=1')

    return redirect('/contact/')





def read_blog(request, slug):
    blog = get_object_or_404(ReadBlog, slug=slug)
     
    return render(request, 'read_blog.html', {'blog': blog})