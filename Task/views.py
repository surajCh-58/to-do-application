from django.shortcuts import *
from . import views
from . models import *
from . forms import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def AddTask(request,pk=None):
    instance_task=get_object_or_404(Task,id=pk) if pk else None
    if request.method=="POST":
        form=TaskForm(request.POST,instance=instance_task)
        if form.is_valid():
            task=form.save(commit=False)
            if task.status=='c' and task.finished_date is None:
                task.finished_date=timezone.now()
            task.user=request.user
            task.save()
            return redirect("Task:alltask")
    else:
        form=TaskForm(instance=instance_task)
    return render(request,"AddTask.html",{'form':form})
@login_required
def DeleteTask(request,pk):
    task=get_object_or_404(Task,id=pk)
    task.delete()
    return redirect("Task:alltask")
@login_required
def AllTask(request):
    tasks=Task.objects.all()
    return render(request,"AllTask.html",{'task':tasks})