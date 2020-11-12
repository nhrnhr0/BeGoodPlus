from django.shortcuts import render

from clientLikedImages.models import ClientLikedImage
from catalogImages.models import CatalogImage
from django.http import HttpResponse
import json
# Create your views here.
def add_liked_images(request,  *args, **kwargs):
    if (request.is_ajax()):
        name = request.POST.get('name')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        msg = request.POST.get('message')
        liked_images = request.POST.getlist('selected_image[]')
        images = CatalogImage.objects.filter(pk__in=liked_images)
        print('add_liked_images', name, email, tel, msg, liked_images)
        response_data = {}

        
        if(name == None or email == None or tel == None): 
            #print('error add_liked_images')
            response_data['result'] = 'error'
            response_data['message'] = 'שם מייל או טלפון רייקים'
        else:
            new_record = ClientLikedImage.objects.create(name=name, email=email, tel=tel, msg=msg)
            new_record.images.set(images)
            response_data['result'] = 'sucsses'
            response_data['message'] = str(new_record)
            #print('add_liked_images', t)
        print('add_liked_images res: ', response_data)
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    