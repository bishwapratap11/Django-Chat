from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Message
# Create your views here.


def index(request):
    users = User.objects.all().exclude(username=request.user.username)
    param ={
        'users': users
    }
    return render(request, 'web/index.html', param)


def chat(request, name):
    users = User.objects.all().exclude(username=request.user.username)
    get_user = User.objects.get(username=name)
    my_id = request.user.id
    # if int(my_id) > int(get_user.id):
    #     thread_name = f'chat_{my_id}_{get_user.id}'
    # else:
    #     thread_name = f'chat_{get_user.id}_{my_id}'
    # message = Message.objects.filter(thread_name=thread_name)
    
    param ={
        'users': users,
        'get_user': get_user,
        # 'message': message,
    }
    return render(request, 'web/chat.html', param)