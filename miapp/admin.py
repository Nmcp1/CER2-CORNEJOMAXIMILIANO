from django.contrib import admin
from .models import Entidad, Comunicador
from django.core.exceptions import PermissionDenied

# Register your models here.
class comunicados(admin.ModelAdmin):
    list_display = ("titulo","tipo","fecha_publicacion","entidad","publicado_por","modificado_por", "visible")
    list_filter = [("publicado_por",admin.RelatedOnlyFieldListFilter),]



    def save_model(self, request, obj, form, change):
        if change:
            obj.modificado_por = request.user
            if ((request.user != obj.entidad.administrador) and (request.user.is_superuser == False)):
                raise PermissionDenied
        else:
            obj.publicado_por = request.user     
            for ent in Entidad.objects.all():
                if ent.administrador == request.user:
                    obj.entidad = ent
        super().save_model(request, obj, form, change)
    
    def delete_model(self, request, object):
        if ((request.user != object.entidad.administrador) and (request.user.is_superuser == False)):
            raise PermissionDenied
        else:
            object.delete()

admin.site.register(Entidad)
admin.site.register(Comunicador,comunicados)