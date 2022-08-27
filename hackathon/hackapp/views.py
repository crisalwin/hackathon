from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import openpyxl


# Create your views here.
def dis(request):
    return render(request, 'excel.html')


def index(request):
    if "GET" == request.method:
        return render(request, 'excel.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        wb = openpyxl.load_workbook(excel_file)

        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()

        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:

                    row_data.append(str(cell.value))


            excel_data.append(row_data)
            for i in excel_data:

                if i[0]==('ctc'):
                    print(i[0],i[1])
                    a=i[1]
                    b=(float(a)*47.3484) / 100
                    c=(float(a) * 23.6742) / 100
                    d=(float(a) * 21.6289) / 100
                    e=(float(a) * 2.04545) / 100
                    print('basic salary:',b,'\nHRA:',c,'\nSP:',d,'\nPF:',e)



        return render(request, 'excel.html', {"excel_data": excel_data})
