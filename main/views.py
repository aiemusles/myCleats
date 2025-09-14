from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import CleatsForm
from main.models import Cleats

# views disini
def show_main(request):
    cleats_list = Cleats.objects.all()

    context = {
        'npm' : '2406411824',
        'name': 'Marco Imanuel',
        'class': 'PBP C',
        'cleats_list': cleats_list
    }

    return render(request, "main.html", context)

#Forms
def add_cleats(request):
    form = CleatsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "add_cleats.html", context)

def show_cleats(request, id):
    cleats = get_object_or_404(Cleats, pk=id)

    context = {
        'cleats': cleats
    }

    return render(request, "cleats_detail.html", context)

# xml helper
def show_xml(request):
    cleats_list = Cleats.objects.all()
    xml_data = serializers.serialize("xml", cleats_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_xml_by_id(request, cleats_id):
   try:
       cleats_item = Cleats.objects.filter(pk=cleats_id)
       xml_data = serializers.serialize("xml", cleats_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Cleats.DoesNotExist:
       return HttpResponse(status=404)

# json helper
def show_json(request):
    cleats_list = Cleats.objects.all()
    json_data = serializers.serialize("json", cleats_list)
    return HttpResponse(json_data, content_type="application/json")

def show_json_by_id(request, cleats_id):
   try:
       cleats_item = Cleats.objects.get(pk=cleats_id)
       json_data = serializers.serialize("json", [cleats_item])
       return HttpResponse(json_data, content_type="application/json")
   except Cleats.DoesNotExist:
       return HttpResponse(status=404)