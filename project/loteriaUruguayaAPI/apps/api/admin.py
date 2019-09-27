from django.contrib import admin
from .models.games import Game
from .models.results import CincoDeOroResult

# Model registration
admin.site.register(Game)
admin.site.register(CincoDeOroResult)
