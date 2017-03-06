from django.conf.urls import url
from estante.views import CadastraPessoa
from estante.views import CadastraLivro
from estante.views import Login, Desativar

urlpatterns = [
    url(r'^cad_pessoa/', CadastraPessoa.as_view(), name='cadastro-pessoa'),
    url(r'^cad_livro/', CadastraLivro.as_view(), name='cadastro-livro'),
    url(r'^cad_livro/()', CadastraLivro.as_view(), name='cadastro-livro'),
    url(r'^index/', Login.as_view(), name='index'),
    url(r'^perfil/', Desativar.as_view(), name='desativar'),

]