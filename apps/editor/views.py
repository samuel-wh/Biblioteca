from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from ..editor.forms import EditorForm

from ..editor.models import Editor
# Create your views here.
def index(request):
    return render(request, 'editor/index.html')

# Clases
class EditorCreate(CreateView):
    model = Editor
    form_class = EditorForm
    template_name = 'editor/view_class/editor_form.html'
    success_url = reverse_lazy('editor_listar_c')

class EditorList(ListView):
    model = Editor
    template_name = 'editor/view_class/editor_list.html'
    
class EditorDelete(DeleteView):
    model = Editor
    template_name = 'editor/view_class/editor_delete.html'
    success_url = reverse_lazy('editor_listar_c')

class EditorUpdate(UpdateView):
    model = Editor
    form_class = EditorForm
    template_name = "editor/view_class/editor_form.html"
    success_url = reverse_lazy('editor_listar_c')

# Funciones
def editor_create(request):
    if request.method == 'POST':
        form = EditorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('editor_listar_f')
    else:
        form = EditorForm()
    return render(request, 'editor/view_functions/editor_form.html', {'form':form})

def editor_list(request):
    editor = Editor.objects.all().order_by('id')
    contexto = {'editores':editor}
    return render(request, 'editor/view_functions/editor_list.html', contexto)

def editor_update(request, id_editor):
    editor = Editor.objects.get(id=id_editor)
    if request.method == 'GET':
        form = EditorForm(instance=editor)
    else:
        form = EditorForm(request.POST, instance=editor)
        if form.is_valid():
            form.save()
        return redirect('editor_listar_f')
    return render(request, 'editor/view_functions/editor_form.html', {'form':form})
    
def editor_delete(request, id_editor):
    editor = Editor.objects.get(id=id_editor)
    if request.method == 'POST':
        editor.delete()
        return redirect('editor_listar_f')
    return render(request, 'editor/view_functions/editor_delete.html', {'editor':editor})