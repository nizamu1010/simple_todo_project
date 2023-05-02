from django.shortcuts import render, redirect

from .models import Todo
from .forms import TodoForm
# Create your views here.

def home(request):
    todo = Todo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = Todo(name=name, priority= priority, date=date)
        task.save()
        
    return render(request,'index.html',{'todo':todo})


def delete(request,id):
    task = Todo.objects.get(id=id)
    if request.method ==  'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    todo = Todo.objects.get(id=id)
    frm = TodoForm(request.POST or None, instance=todo )
    if frm.is_valid():
        frm.save()
        return redirect('/')   
    return render(request,'edit.html',{'frm':frm,'task':todo})