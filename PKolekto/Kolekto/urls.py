from django.urls import path, include
from . import views


urlpatterns =[
    path("", views.home, name="index"),
    path("registro", views.Registro, name='registro'),
    path("login", views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path("nova_loja", views.Cadastro_Loja, name='nova_loja'),
    path("add_produto", views.Add_Produto, name="add_produto"),
    path("Produto/<int:id_produto>/",views.pagina_produto, name="pagina_produto"),
    path("<str:nome_loja>/", views.pagina_loja, name="loja"),
    path("pesquisa", views.pesquisa, name="pesquisa"),
    path("minha_loja", views.minha_loja, name="minha_loja"),
    path("lista_desejos", views.lista_desejos, name="lista_desejos"),
    path("add_lista_desejos", views.add_lista_desejos, name="add_lista_desejos"),
    path("rem_lista_desejos", views.rem_lista_desejos, name="rem_lista_desejos"),
    path("add_carrinho", views.add_carrinho, name="add_carrinho"),
    path("rem_carrinho", views.rem_carrinho, name="rem_carrinho"),
    path("carrinho", views.carrinho, name="carrinho"),
    path("<str:nome_loja>/denuncia", views.denuncia, name="denuncia")
]