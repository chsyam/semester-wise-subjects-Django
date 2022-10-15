from django.shortcuts import redirect, render
from django.http import FileResponse
from .forms import semForm
from .models import semestersModel
from django.db.models import Sum
# Create your views here.

def cse_r19(request):
    form = semForm()
    if request.method == "POST":
        form = semForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    sem1 = semestersModel.objects.filter(semester=1)
    sem2 = semestersModel.objects.filter(semester=2)
    sem3 = semestersModel.objects.filter(semester=3)
    sem4 = semestersModel.objects.filter(semester=4)
    sem5 = semestersModel.objects.filter(semester=5)
    sem6 = semestersModel.objects.filter(semester=6)
    sem7 = semestersModel.objects.filter(semester=7)
    sem8 = semestersModel.objects.filter(semester=8)
    total_1 = semestersModel.objects.filter(semester=1).aggregate(total=Sum('subject_credits'))
    total_2 = semestersModel.objects.filter(semester=2).aggregate(total=Sum('subject_credits'))
    total_3 = semestersModel.objects.filter(semester=3).aggregate(total=Sum('subject_credits'))
    total_4 = semestersModel.objects.filter(semester=4).aggregate(total=Sum('subject_credits'))
    total_5 = semestersModel.objects.filter(semester=5).aggregate(total=Sum('subject_credits'))
    total_6 = semestersModel.objects.filter(semester=6).aggregate(total=Sum('subject_credits'))
    total_7 = semestersModel.objects.filter(semester=7).aggregate(total=Sum('subject_credits'))
    total_8 = semestersModel.objects.filter(semester=8).aggregate(total=Sum('subject_credits'))
    sem_subs = {
            'form':semForm,
            'sem1': sem1,
            'sem2': sem2,
            'sem3': sem3,
            'sem4': sem4,
            'sem5': sem5,
            'sem6': sem6,
            'sem7': sem7,
            'sem8': sem8,
            't1': total_1['total'],
            't2': total_2['total'],
            't3': total_3['total'],
            't4': total_4['total'],
            't5': total_5['total'],
            't6': total_6['total'],
            't7': total_7['total'],
            't8': total_8['total'],
        }
    return render(request,"cse(2020-2021).html",sem_subs)

def allSubjects(request):
    sem1 = semestersModel.objects.filter(semester=1)
    sem2 = semestersModel.objects.filter(semester=2)
    sem3 = semestersModel.objects.filter(semester=3)
    sem4 = semestersModel.objects.filter(semester=4)
    sem5 = semestersModel.objects.filter(semester=5)
    sem6 = semestersModel.objects.filter(semester=6)
    sem7 = semestersModel.objects.filter(semester=7)
    sem8 = semestersModel.objects.filter(semester=8)
    total_1 = semestersModel.objects.filter(semester = 1).aggregate(total = Sum('subject_credits'))
    total_2 = semestersModel.objects.filter(semester = 2).aggregate(total = Sum('subject_credits'))
    total_3 = semestersModel.objects.filter(semester = 3).aggregate(total = Sum('subject_credits'))
    total_4 = semestersModel.objects.filter(semester = 4).aggregate(total = Sum('subject_credits'))
    total_5 = semestersModel.objects.filter(semester = 5).aggregate(total = Sum('subject_credits'))
    total_6 = semestersModel.objects.filter(semester = 6).aggregate(total = Sum('subject_credits'))
    total_7 = semestersModel.objects.filter(semester = 7).aggregate(total = Sum('subject_credits'))
    total_8 = semestersModel.objects.filter(semester = 8).aggregate(total = Sum('subject_credits'))
    sem_subs = {
                 'sem1': sem1,
                 'sem2': sem2,
                 'sem3': sem3,
                 'sem4': sem4,
                 'sem5': sem5,
                 'sem6': sem6,
                 'sem7': sem7,
                 'sem8': sem8,
                 't1' : total_1['total'],
                 't2' : total_2['total'],
                 't3' : total_3['total'],
                 't4' : total_4['total'],
                 't5' : total_5['total'],
                 't6' : total_6['total'],
                 't7' : total_7['total'],
                 't8' : total_8['total'],
                }
    return render(request,"index.html",sem_subs)

def redirect_pdf(request,id):
    file_details = semestersModel.objects.filter(id = id)
    return FileResponse(open(file_details[0].document.path, 'rb'))


def delete(request,id):
    item = semestersModel.objects.get(id=id)
    item.delete()
    return redirect(cse_r19)

def update(request, id):
    subject = semestersModel.objects.get(id = id)
    form = semForm(instance=subject)
    if request.method == 'POST':
        form = semForm(request.POST,request.FILES, instance=subject)
        if form.is_valid():
            form.save()
            return redirect(cse_r19)
    return render(request,'update.html',{'subject':subject})