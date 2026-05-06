from django.contrib import admin
from .models import Logo
from .models import WhatOurClientsSay
from .models import NewOnOurReel
from .models import TeamMember
from .models import DigitalImpactStory
from .models import CreativeContentPortfolio
from .models import AddYourWords
from .models import SuccessStories
from .models import OurBlog

 

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



admin.site.register(OurBlog)
list_display = ('title', 'author', 'date')
prepopulated_fields = {"slug": ("title",)}




admin.site.site_header = "Two Dots Film Admin"
admin.site.site_title = "Two Dots Film Dashboard"
admin.site.index_title = "Welcome to Two Dots Film Panel"

from .models import ReadBlog
@admin.register(ReadBlog)
class ReadBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')
    search_fields = ('title', 'category', 'author')

    prepopulated_fields = {"slug": ("title",)}