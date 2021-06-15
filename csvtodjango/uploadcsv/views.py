import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Data



@permission_required('admin.can_add_log_entry')
def info_upload(request):
    template = "info_upload.html"
    prompt = {
        'order' : 'CSV file must be in the right order'
    }

    if request.method == "GET":
        return render(request, template, prompt)


    csv_file = request.FILES['file', 'default value']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This is not a CSV file")

    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=','):
        _, created = Data.objects.update_or_create(
            num = column[0],
            symbol = column[1],
            date = column[2],
            opening = column[3],
            high = column[4],
            low = column[5],
            close = column[6],
            volume = column[7],
            adjclose = column[8]
        )
        

        context = {}
        return render(request, template, context)