from django.shortcuts import render_to_response, RequestContext
from rosters.models import *
from rosters.forms import *

def view_all_rosters(request):
    return render_to_response('view_all_rosters.html', RequestContext(request, locals()))
    
def create_roster(request):
    new_player_form = PlayerForm()
    return render_to_response('create_roster.html', RequestContext(request, locals()))
