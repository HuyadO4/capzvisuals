from django.contrib import admin
from .models import Comment
from .models import Beauty
from .models import Birthday
from .models import Event
from .models import Fashion
from .models import Wedding
# Register your models here.
class PicsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Comment),
admin.site.register(Beauty, PicsAdmin),
admin.site.register(Birthday),
admin.site.register(Event),
admin.site.register(Fashion),
admin.site.register(Wedding),
