# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Suspect_names,Suspect_detects

admin.site.register(Suspect_names)
admin.site.register(Suspect_detects)

# Register your models here.
