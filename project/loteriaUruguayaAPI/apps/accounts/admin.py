from django.contrib import admin
from .models.histories import History
from .models.requestlogs import RequestLog
from .models.subscriptions import Subscription
from .models.users import User

# Model registration
admin.site.register(History)
admin.site.register(RequestLog)
admin.site.register(Subscription)
admin.site.register(User)