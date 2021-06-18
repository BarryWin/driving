from django.contrib import admin

from .models import Ucheniki
from .models import Documenti
from .models import DrivingCard
from .models import Sotrudniki
from .models import Rasp_teor
from .models import Zurnal
from .models import PosZurnal


admin.site.register(Ucheniki)

admin.site.register(Documenti)

admin.site.register(DrivingCard)

admin.site.register(Sotrudniki)

admin.site.register(Rasp_teor)

admin.site.register(Zurnal)

admin.site.register(PosZurnal)
