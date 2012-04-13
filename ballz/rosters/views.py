import json
from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.http import HttpResponse
from rosters.models import *
from rosters.forms import *


def view_all_rosters(request):
    return render_to_response('view_all_rosters.html', RequestContext(request, locals()))


def create_roster(request):
    if request.method == 'POST':
        name = request.POST['team_name']
        sport, created = Sport.objects.get_or_create(name=request.POST['sport'])
        if created:
            sport.save()
        team = Team.objects.create(name=name, sport=sport)
        team.save()
        return manage_roster(request, team.id)
    return view_all_rosters(request)


def manage_roster(request, team_id):
    team = Team.objects.get(id=team_id)
    return render_to_response('manage_roster.html', RequestContext(request, locals()))


def add_player(request):
    if request.is_ajax():
    # TODO: setup image upload for photo
        zipcode = request.POST['zipcode']
        if type(zipcode) != int:
            zipcode = None

        age = request.POST['age']
        if type(age) != int:
            age = None

        contact_info, created = ContactInfo.objects.get_or_create(
            phone=request.POST['phone'],
            email=request.POST['email'],
            address=request.POST['address'],
            city=request.POST['city'],
            state=request.POST['state'],
            zipcode=zipcode
        )
        if created:
            contact_info.save()

        player = Player.objects.create(
            name=request.POST['name'],
            age=age,
            position=request.POST['position'],
            contact_info=contact_info,
            created_by=request.user
        )
        player.save()

        # add player to team
        team = Team.objects.get(id=request.POST['team'])
        team.players.add(player)
        team.save()

        data = json.dumps({
            'player_name':  player.name,
            'player_id':    player.id,
            'age':          player.age,
            'position':     player.position,
            'phone':        player.contact_info.phone,
            'email':        player.contact_info.email,
            'address':      player.contact_info.address,
            'city':         player.contact_info.city,
            'state':        player.contact_info.state,
            'zipcode':      player.contact_info.zipcode
        })

    return HttpResponse(data, mimetype='application/json')


def remove_player(request):
    if request.is_ajax:
        player = Player.objects.get(id=request.POST['player_id'])
        team = Team.objects.get(id=request.POST['team_id'])
        team.players.remove(player)
        team.save()
        data = json.dumps({
            'player_id': player.id
        })
        return HttpResponse(data, mimetype='application/json')
