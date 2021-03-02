import uuid
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Customer(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A customer with that username already exists."),
        },
    )
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(_('email address'), blank=True)
    cxid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=True,
        help_text=_('Designates whether the customer can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active status'),
        default=True,
        help_text=_('Designates whether the customer account is active'),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    objects = UserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    first_name = None
    last_name = None
    last_login = None

    class Meta(AbstractUser.Meta):
        db_table = 'customer'
