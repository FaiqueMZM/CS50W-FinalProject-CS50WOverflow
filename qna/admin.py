from django.contrib import admin

from .models import User, Issue, Reply, Vote

# Register your models here.
admin.site.register(Issue)
admin.site.register(Reply)
admin.site.register(Vote)

