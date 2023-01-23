def handle_uploaded_file(f):  
    with open('/library/static/media/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)