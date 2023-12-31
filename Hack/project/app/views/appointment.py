from django.shortcuts import render,redirect
from app.models import Appointment,User
import random

from django.contrib.auth.decorators import login_required

def appointment_unique_number(name):
    name=name
    while(True):  
        uq=random.randint(1000,9999)
        uq=name+str(uq)
        try:
            n=Appointment.objects.get(appointment_id=uq)
        except:
            return uq

@login_required(login_url='signin')
def appointment(request,slug):
    if request.method == 'POST':
        slug=slug
        date=request.POST['date']
        time=request.POST['time']
        age=request.POST['age']
        weight=request.POST['weight']
        gender=request.POST['gender']
        blood_group=request.POST['blood_group']
        contact=request.POST['contact']
        patient_name=request.POST['name']
        relation=request.POST['relation']
        doctor_name=request.POST['doctor_name']
        symptoms=request.POST['symptoms']
        consultation=request.POST['consultation']
        # ran = random.randint(999,9999)
        appointment_ref=request.user
        appointment_id=appointment_unique_number("appoint")


        try:
            predicted_file=request.FILES['predicted_file']
            df=Appointment.objects.create(appointment_ref=appointment_ref,appointment_id=appointment_id,date=date,slot_time=time,patient_name=patient_name,contact=contact,relation=relation,age=age,weight=weight,blood_group=blood_group,gender=gender,doctor=doctor_name,symptoms=symptoms,consultation=consultation,predicted_file=predicted_file)        
        except:
            df=Appointment.objects.create(appointment_ref=appointment_ref,appointment_id=appointment_id,date=date,slot_time=time,patient_name=patient_name,contact=contact,relation=relation,age=age,weight=weight,blood_group=blood_group,gender=gender,doctor=doctor_name,consultation=consultation,symptoms=symptoms)        

        return redirect('dasboard')
    # try:
    #     doctor_data = User.object.filter(user_type = "doctor")
    #     context = {
    #         'doctor_data' :doctor_data
    #     }
    # except:
    #     context = {
    #         'doctor_data' :"Data Not Found"
    #     }

    doctor_data = User.object.get(phone = slug)

    context={
        'doctor_data':doctor_data,
    }
    return render(request,'dasboard/user/appointment.html',context)
