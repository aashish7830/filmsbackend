from django.contrib import admin
from .models import Logo
from .models import WhatOurClientsSay
from .models import NewOnOurReel
from .models import TeamMember
from .models import DigitalImpactStory
from .models import CreativeContentPortfolio
from .models import AddYourWords
from .models import SuccessStories

 

# Register your models here.
admin.site.register(Logo)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

admin.site.register(WhatOurClientsSay, ClientAdmin)


admin.site.register(NewOnOurReel)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
admin.site.register(TeamMember, TeamAdmin)



class DigitalStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

admin.site.register(DigitalImpactStory, DigitalStoryAdmin)



 

@admin.register(CreativeContentPortfolio)
class CreativeContentPortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title', 'category')



@admin.register(AddYourWords)
class AddYourWordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'created_at')
    search_fields = ('name', 'review')





@admin.register(SuccessStories)
class SuccessStoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'created_at')
    search_fields = ('name', 'designation')