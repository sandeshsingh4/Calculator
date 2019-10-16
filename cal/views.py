from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    try:
        v_1 = int(request.POST.get('value_1','0'))
        v_2 = int(request.POST.get('value_2','0'))
        Value=0

        add = request.POST.get('add','off')
        sub = request.POST.get('sub','off')
        div = request.POST.get('div','off')
        mul = request.POST.get('mul','off')


        if add=='on':
            Value = v_1+v_2

        elif sub=='on':
            Value = v_1-v_2

        elif div=='on':
            Value = v_1/v_2

        elif mul=='on':
            Value = v_1*v_2

        params = {'Value': Value}
        return render(request,'cal/cal.html',params)

    except:
        params = {'Value': "Please Enter valid input"}    
        return render(request,'cal/cal.html',params)

    
# def c(request):
#     equations = request.POST.get('text','default')
#     print(equations)
#     params = {'equation': equations}
#     print(params)
#     print(params['equation'])
#     return render(request,'cal/c.html', params)
