from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from views import AutorDelete, AutorUpdate, index, AutorCreate, AutorList, LibroCreate, LibroList, LibroEdit, LibroDelete, autor_create, autor_list, autor_update, autor_delete, libro_create, libro_list, libro_update, libro_delete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^autor/nuevo_cv$', AutorCreate.as_view(), name='autor_crear_c'),
    url(r'^autor/listar_cv$', AutorList.as_view(), name='autor_listar_c'),
    url(r'^autor/editar_cv/(?P<pk>\d+)/$', AutorUpdate.as_view(), name='autor_editar_c'),
    url(r'^autor/eliminar_cv/(?P<pk>\d+)/$', AutorDelete.as_view(), name='autor_eliminar_c'),

    url(r'^autor/nuevo_fv$', autor_create, name='autor_crear_f'),
    url(r'^autor/listar_fv$', autor_list, name='autor_listar_f'),
    url(r'^autor/editar_fv/(?P<id_autor>\d+)/$', autor_update, name='autor_editar_f'),
    url(r'^autor/eliminar_fv/(?P<id_autor>\d+)/$', autor_delete, name='autor_eliminar_f'),

    url(r'^libro/nuevo_cv$', LibroCreate.as_view(), name='libro_crear_c'),
    url(r'^libro/listar_cv$', LibroList.as_view(), name='libro_listar_c'),
    url(r'^libro/editar_cv/(?P<pk>\d+)/$', LibroEdit.as_view(), name='libro_editar_c'),
    url(r'^libro/eliminar_cv/(?P<pk>\d+)/$', LibroDelete.as_view(), name='libro_eliminar_c'),

    url(r'^libro/nuevo_fv$', libro_create, name='libro_crear_f'),
    url(r'^libro/listar_fv$', libro_list, name='libro_listar_f'),
    url(r'^libro/editar_fv/(?P<id_libro>\d+)/$', libro_update, name='libro_editar_f'),
    url(r'^libro/eliminar_fv/(?P<id_libro>\d+)/$', libro_delete, name='libro_eliminar_f'),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)