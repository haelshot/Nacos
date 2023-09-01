from django.shortcuts import render
from .models import Photo



def home(request):
    photos = Photo.objects.all()
    photo_sections = {}
    for photo in photos:
        if photo.title in photo_sections:
            photo_sections[photo.title].append(photo)
        else:
            photo_sections[photo.title] = [photo]
    return render(request, 'index.html', {'photo_sections': photo_sections})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')


from django.shortcuts import render
from .models import CourseMaterial

def level_materials(request, level):
    materials = CourseMaterial.objects.filter(level=level)
    return render(request, 'level_materials.html', {'level': level, 'materials': materials})

# views.py
from django.shortcuts import render
from urllib.parse import quote
from django.shortcuts import HttpResponseRedirect


def send_comment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        
        message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nComment: {comment}"
        encoded_message = quote(message)
        whatsapp_number = '+2348059498558'  # Replace with your WhatsApp number
        whatsapp_link = f'https://wa.me/{whatsapp_number}?text={encoded_message}'
        return HttpResponseRedirect(whatsapp_link)
    return render(request, 'contact.html')


from django.shortcuts import render
from .models import Photo

def photo_list(request):
    photos = Photo.objects.all()
    photo_sections = {}
    for photo in photos:
        if photo.title in photo_sections:
            photo_sections[photo.title].append(photo)
        else:
            photo_sections[photo.title] = [photo]
    return render(request, 'album.html', {'photo_sections': photo_sections})
