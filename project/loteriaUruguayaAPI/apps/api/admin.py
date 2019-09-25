from django.contrib import admin
from .models.games import Game
from .models.results import Result, CincoDeOroResult

# Model registration
admin.site.register(Game)
admin.site.register(Result)
admin.site.register(CincoDeOroResult)
