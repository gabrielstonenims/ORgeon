from django.contrib import admin

from .models import (Volunteer, Events, JoinTrip, Partnership, NewsLetter, NewsUpdate, Report, Post, Comments, Gallery,
                     LoginCode, Online_user, MessageD, Message, ContactUs, ClientInfoProgress)

admin.site.register(Volunteer)
admin.site.register(Events)
admin.site.register(JoinTrip)
admin.site.register(Partnership)
admin.site.register(NewsLetter)
admin.site.register(NewsUpdate)
admin.site.register(Report)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Gallery)
admin.site.register(LoginCode)
admin.site.register(Online_user)
admin.site.register(MessageD)
admin.site.register(Message)
admin.site.register(ContactUs)
admin.site.register(ClientInfoProgress)
