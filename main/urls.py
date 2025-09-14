from django.urls import path
from main.views import show_main, add_cleats, show_cleats, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-cleats/', add_cleats, name='add_cleats'),
    path('cleats/<str:id>/', show_cleats, name='show_cleats'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:cleats_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:cleats_id>/', show_json_by_id, name='show_json_by_id'),
]