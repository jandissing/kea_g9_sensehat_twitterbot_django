from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
import mysql.connector as mariadb
from django.http import JsonResponse

# Create your views here.


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['team'] = TeamMember.objects.all()
        context['hatdata'] = HatData.objects.all()
        context['lastseenid'] = LastSeenId.objects.all()
        queryset = HatData.objects.values('DateTime', 'Pressure', 'Temperature', 'Humidity').order_by('-Id')[:15][::-1]
        labels = []
        pres = []
        temp = []
        hum = []
        for x in queryset:
            labels.append(x['DateTime'].strftime('%H:%M:%S'))
            pres.append(float(x['Pressure']))
            temp.append(float(x['Temperature']))
            hum.append(float(x['Humidity']))
        data = {'labels': labels, 'pres': pres, 'temp': temp, 'hum': hum,}
        context['data'] = data
        return context


def graph(request):
    import mysql.connector as mariadb
    import pandas as pd
    import matplotlib.pyplot as plt
    conn = mariadb.connect(user='group09int', password='pass1234',database='DB', host='localhost', port='3306')
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM HatData;")
    myresult = mycursor.fetchall()

    df = pd.DataFrame(myresult)
    df.columns = ['Id', 'DateTime', 'Temperature', 'Humidity', 'Pressure']
    print(df)

    plt.figure()
    
    plt.bar(df['DateTime'].dt.strftime('%H:%M:%S'), df['Temperature'])
    plt.savefig("static/media/lastuser_peichart.png")

    return render(request, 'result1.html')


def tempChart(request):
    labels = []
    data = []

    queryset = HatData.objects.values('DateTime', 'Pressure', 'Temperature', 'Humidity').order_by('-Id')[:10][::-1]
    labels = []
    pres = []
    temp = []
    hum = []
    for x in queryset:
        labels.append(x['DateTime'].strftime('%H:%M:%S'))
        pres.append(float(x['Pressure']))
        temp.append(float(x['Temperature']))
        hum.append(float(x['Humidity']))
    data = {'labels': labels, 'pres': pres, 'temp': temp, 'hum': hum,}
    return JsonResponse(data)


def presChart(request):
    labels = []
    data = []

    queryset = HatData.objects.values('DateTime', 'Pressure', 'Temperature', 'Humidity').order_by('-Id')[:10][::-1]
    labels = []
    pres = []
    temp = []
    hum = []
    for x in queryset:
        labels.append(x['DateTime'].strftime('%H:%M:%S'))
        pres.append(float(x['Pressure']))
        temp.append(float(x['Temperature']))
        hum.append(float(x['Humidity']))
    data = {'labels': labels, 'pres': pres, 'temp': temp, 'hum': hum,}
    return JsonResponse(data)


def humChart(request):
    labels = []
    data = []

    queryset = HatData.objects.values('DateTime', 'Pressure', 'Temperature', 'Humidity').order_by('-Id')[:10][::-1]
    labels = []
    pres = []
    temp = []
    hum = []
    for x in queryset:
        labels.append(x['DateTime'].strftime('%H:%M:%S'))
        pres.append(float(x['Pressure']))
        temp.append(float(x['Temperature']))
        hum.append(float(x['Humidity']))
    data = {'labels': labels, 'pres': pres, 'temp': temp, 'hum': hum,}
    return JsonResponse(data)