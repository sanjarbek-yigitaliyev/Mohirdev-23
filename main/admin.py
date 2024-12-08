from django.contrib  import admin
from django.contrib.auth.models import Group,User

from .models import *

admin.site.unregister(Group)
admin.site.unregister(User)




admin.site.register(Profil)
admin.site.register(Kurs)
admin.site.register(Izoh)
admin.site.register(Tanlangan)
admin.site.register(Xarid)
