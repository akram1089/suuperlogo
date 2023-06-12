from django.contrib import admin

# Register your models here.
from.models import User
from.models import ChartData
from.models import ChartOI
from.models import ChartGainerData
from.models import Top_Gainer



admin.site.register(User)
admin.site.register(ChartData)
admin.site.register(ChartOI)
admin.site.register(ChartGainerData)
admin.site.register(Top_Gainer)




