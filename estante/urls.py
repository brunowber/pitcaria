from django.conf.urls import url
from estante.views import CadastraPessoa
from estante.views import CadastraLivro
from estante.views import Logar

urlpatterns = [
    url(r'^cad_pessoa/', CadastraPessoa.as_view(), name='cadastro-pessoa'),
    url(r'^cad_livro/', CadastraLivro.as_view(), name='cadastro-livro'),
    url(r'^logar/', Logar.as_view(), name='index'),
]