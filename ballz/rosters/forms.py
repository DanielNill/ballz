from django.forms import ModelForm
from rosters.models import *

class PlayerForm(ModelForm):
    class Meta:
        model=Player
    