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
    url(r'^cad_pizzas/$', CadastraPizzas.as_view(), name='cadastro-pizzas'),
    url(r'^cardapio/$', Cardapio.as_view(), name='cardapio'),
    url(r'^fazer_pedido/(?P<id>\d+)/$', FazerPedido.as_view(), name='fazer-pedido'),
    url(r'^cardapio/(?P<id>\d+)/$', Cardapio.as_view(), name='cardapio-cliente'),
    url(r'^def_pedido/$', DefPedido.as_view(), name='def-pedido'),
    url(r'^historico/$', Historico.as_view(), name='historico'),
    url(r'^historico_pizzaria/$', HistoricoPizzaria.as_view(), name='historico-pizzaria'),
    #url(r'^pedido/$', Pedido.as_view(), name='pedido'),
    url(r'^procurar_pizzaria/$', ProcurarPizzaria.as_view(), name='procurar_pizzaria'),

    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),

    url(r'^pesquisa/(?P<id>\d+)/$', Pesquisa.as_view(), name='pesquisa'),

    url(r'^perfil_usuario/$', TemplateView.as_view(template_name='perfil_usuario.html'), name='perfil_usuario'),
    url(r'^perfil_pizzaria/$', TemplateView.as_view(template_name='perfil_pizzaria.html'), name='perfil_pizzaria'),

]
