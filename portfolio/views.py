from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'index.html')

def my_cv(request):
    return render(request, 'my_cv.html')

def send_mail(request):
    if request.method == 'POST':
        Message_name = request.POST['my-name']
        Message_email = request.POST['my-email']
        Message_subject = request.POST['my-subject']
        Message = request.POST['my-message']

        send_mail(
            f'{Message_subject} from {Message_name}',
            Message,
            Message_email,
           ['info@nelsonsakhile.co.za'],
        )
        return render(request, 'index.html', {})
    return render(request, 'index.html', {})