from django.shortcuts import render, get_object_or_404, redirect
from .models import UploadedFile
from .forms import FileForm

from rest_framework import viewsets
from .models import UploadedFile
from .serializers import UploadedFileSerializer

# Create your views here.

def file_list(request):
    files = UploadedFile.objects.all() #все файлы с бд
    return render(request, 'fileapp/file_list.html', {'files': files})


def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('file_list')  
    else:
        form = FileForm()
        
    return render(request, 'fileapp/upload_file.html', {'form': form})


def delete_file(request, pk):
    file = get_object_or_404(UploadedFile, pk=pk)
    
    if request.method == 'POST':
        file.delete()
        return redirect('file_list')
    
    return render(request, 'fileapp/delete_file.html', {'file': file})


class UploadedFileViewSet(viewsets.ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer
    