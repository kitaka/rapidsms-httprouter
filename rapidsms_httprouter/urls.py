#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.conf.urls import *
from .views import receive, outbox, delivered, console, relaylog, alert, status
from .textit import textit_webhook
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
   ("^router/status", status),
   ("^router/receive", receive),
   ("^router/outbox", outbox),
   ("^router/relaylog", relaylog),
   ("^router/alert", alert),
   ("^router/delivered", delivered),
   ("^router/console", staff_member_required(console), {}, 'httprouter-console'),
   ("^router/textit", textit_webhook),
]
