from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

from eventmodul.models import Participant, Invitee

def invitation_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the user is an invitee.
    """
    actual_decorator = user_passes_test(
        lambda u: isinstance(u,Invitee),
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def registration_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the user is an invitee.
    """
    actual_decorator = user_passes_test(
        lambda u: isinstance(u,Participant),
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
