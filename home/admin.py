from django.contrib import admin

# Register your models here.
from.models import User
from.models import ChartData

from.models import Top_Gainer
from.models import Top_Loser
from.models import TradedVolume
from.models import SecurityBan



admin.site.register(User)
admin.site.register(ChartData)


admin.site.register(Top_Gainer)
admin.site.register(Top_Loser)
admin.site.register(TradedVolume)
admin.site.register(SecurityBan)




