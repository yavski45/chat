from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Message
from accounts.models import User

@login_required
def inbox(request):
    # select_related to avoid N+1 queries on profile access
    users = User.objects.exclude(id=request.user.id).select_related('profile')
    return render(request, 'chat/inbox.html', {'users': users})

@login_required
def chat_room(request, user_id):
    other_user = get_object_or_404(User.objects.select_related('profile'), id=user_id)

    messages = Message.objects.filter(
        Q(sender=request.user, receiver=other_user) |
        Q(sender=other_user, receiver=request.user)
    ).select_related('sender')

    return render(request, 'chat/room.html', {
        'other_user': other_user,
        'messages': messages,
    })

