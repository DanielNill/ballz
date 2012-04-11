from field_reservation.models import Field
from django.shortcuts import render_to_response
from django.http import HttpResponse

def list_fields(request):
    fields = Field.objects.all();
    return render_to_response('list_fields.html', {'fields': fields})

def create_field(request):
    return HttpResponse('Nothing here yet');
