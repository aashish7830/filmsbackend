from django.urls import path
from . import views
from .views import review_page
from .views import blog
from .views import contact_page
from .views import submit_contact



urlpatterns = [
    path('', views.home, name='home'),
     path('services/', views.services, name='services'),
      path('team/', views.team, name='team'),
      path('recognition/', views.recognition, name='recognition'),
      path('portfolio/', views.portfolio, name='portfolio'),
      path('reviews/', review_page, name='reviews'),
       path('blog/', blog, name='blog'),
       path('contact/', contact_page, name='contact'),
        path('submit-contact/', submit_contact, name='submit_contact'),
        # path('read-blog/', views.read_blog, name='read_blog'),
        path('read_blog/<slug:slug>/', views.read_blog, name='read_blog')

]