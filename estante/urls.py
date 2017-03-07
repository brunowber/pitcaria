from django.conf.urls import url
from estante.views import *
from estante import views

urlpatterns = [
    url(r'^$', Login.as_view(), name='login'),
    url(r'^cad_pessoa/$', CadastraPessoa.as_view(), name='cadastro-pessoa'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^cad_livro/$', CadastraLivro.as_view(), name='cadastro-livro'),
    url(r'^desativar/$', Alterar_status.as_view(), name='desativar'),
    url(r'^ativar/$', Alterar_status.as_view(), name='ativar'),
    url(r'^perfil/$', Perfil.as_view(), name='perfil'),
    url(r'^editar_perfil/$', CadastraPessoa.as_view(), name='editar_perfil'),
    url(r'^lista_livros/$', DicLivro.as_view(), name='lista_livros'),
    url(r'^livro/(?P<id>\d+)/$', PerfilLivro.as_view(), name='perfil_livro'),
]
