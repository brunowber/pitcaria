from django.conf.urls import url
from pitcaria.views import *
from pitcaria import views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    url(r'^$', Index.as_view(), name='index'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^cad_cliente/$', CadastraCliente.as_view(), name='cadastro-cliente'),
    url(r'^cad_pizzaria/$', CadastraPizzaria.as_view(), name='cadastro-pizzaria'),
    #url(r'^perfil_usuario/$', PerfilUsuario.as_view(), name='cadastro-pizzaria'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    #url(r'^cad_livro/$', CadastraLivro.as_view(), name='cadastro-livro'),
    #url(r'^cad_livro/(?P<id>\d+)/$', CadastraLivro.as_view(), name='edita-livro'),
    #url(r'^desativar/$', Alterar_status.as_view(), name='desativar'),
    #url(r'^esconder/(?P<id>\d+)/$', Alterar_status_livro.as_view(), name='esconder_livro'),
    #url(r'^ativar/$', Alterar_status.as_view(), name='ativar'),
    url(r'^perfil_usuario/$', TemplateView.as_view(template_name='perfil_usuario.html'), name='perfil_usuario'),
    url(r'^perfil_pizzaria/$', TemplateView.as_view(template_name='perfil_pizzaria.html'), name='perfil_pizzaria'),
    #url(r'^editar_perfil/$', CadastraPessoa.as_view(), name='editar_perfil'),
    #url(r'^lista_livros/$', DicLivro.as_view(), name='lista_livros'),
    #url(r'^livro/(?P<id>\w+)/$', PerfilLivro.as_view(), name='perfil_livro'),
    #url(r'^emprestimo/(?P<id>\w+)/$', Cad_emprestimo.as_view(), name='emprestimo'),
    #url(r'^procurar/$', Procurar.as_view(), name='procurar_livro'),
    #url(r'^devolver/(?P<id>\w+)/$', views.Devolver, name='devolver_livro'),
    #url(r'', TemplateView.as_view(template_name='404.html'), name='404'),
]
