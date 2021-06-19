from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DateInfo


def hello(request):
    text = """<h>Hello World!!!</h>"""
    return HttpResponse(text)

def display(request, month):
    text = "The month is: %s" % month
    return HttpResponse(text)

def calendar_view(request, month, year):
    content = DateInfo.objects.all()

    contentOrdered = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19],[20],[21],[22],[23],[24],[25],[26],[26],[28],[29],[30],[31]]
    monthNames = ['January','Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November']

    for x in content:
        if(monthNames[x.date_month-1] == month and x.date_year == year):
            temp = []
            temp.append(x.date_day)
            temp.append(x.date_month)
            temp.append(x.date_year)
            newContent = ""

            try:
                newContent = "*" + x.date_content + "\n" + contentOrdered[x.date_day-1][3]
                temp.append(newContent)
            except:
                temp.append("*"+x.date_content)

            contentOrdered.insert(x.date_day,temp)
            contentOrdered.pop((x.date_day)-1)

    return render(request, "calendar_display.html", {"month_name": month, "content": contentOrdered, "year": year})

def add_new_view(request, month, year):

    fmonth = request.POST.get('fname')
    fday = request.POST.get('fday')
    fyear = request.POST.get('fyear')
    fcontent = request.POST.get('fcontent')

    monthNames = ['January','Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November']
    try:
        dateNew = DateInfo(
            date_month = monthNames.index(fmonth)+1, date_day = fday, date_year= fyear, date_content= fcontent
        )
        dateNew.save()
        return redirect(calendar_view, month = month, year = year)
        #return render(request, "calendar_display.html", {"month_name": month, "content": contentOrdered, "year": year})
    except:
        pass
    return render(request, "add_new_date.html", {"month_name": month, "year": year})

def delete_old_view(request, month, year):
    didDelete = False
    content = DateInfo.objects.all()
    #print(request.POST)
    # Loop through all of the selected items and delete them
    for x in request.POST:
        # We will have an error for the first one because it is a Django security thing I had to add
        # FIX: I need to fix this to run smoother. Kind of sloppy/lazy with how I handle the problem.
        try:
            toDelete = content.filter(date_content = x)
            toDelete.delete()
            didDelete = True
        except:
            pass
    if didDelete:
        return redirect(calendar_view, month = month, year = year)
    return render(request, "delete_old_date.html", {"month_name": month, "year": year, "cal_content": content})