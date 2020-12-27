from django.contrib import admin
from .models import Food
from .models import Paleo
from .models import Vegetarian
from .models import Vegan
from .models import Ketogenic
from .models import Mediterranean
from .models import review
from .models import drop

# Register your models here.
admin.site.register(Food)
admin.site.register(Paleo)
admin.site.register(Vegetarian)
admin.site.register(Vegan)
admin.site.register(Ketogenic)
admin.site.register(Mediterranean)
admin.site.register(review)
admin.site.register(drop)