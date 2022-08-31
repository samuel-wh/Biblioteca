from django.conf.urls import url
from views import EditorDelete, EditorUpdate, editor_create, editor_delete, editor_update, index,EditorCreate, EditorList, editor_list

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^editor/nuevo_cv$', EditorCreate.as_view(), name='editor_crear_c'),
    url(r'^editor/listar_cv$', EditorList.as_view(), name='editor_listar_c'),
    url(r'^editor/eliminar_cv/(?P<pk>\d+)/$', EditorDelete.as_view(), name='editor_eliminar_c'),
    url(r'^editor/editar_cv/(?P<pk>\d+)/$', EditorUpdate.as_view(), name='editor_editar_c'),

    url(r'^editor/nuevo_fv$', editor_create, name='editor_crear_f'),
    url(r'^editor/listar_fv$', editor_list, name='editor_listar_f'),
    url(r'^editor/editar_fv/(?P<id_editor>\d+)/$', editor_update, name='editor_editar_f'),
    url(r'^editor/eliminar_fv/(?P<id_editor>\d+)/$', editor_delete, name='editor_eliminar_f'),

    
]