from django.urls import path, include
from . import views


urlpatterns =[
    path("", views.home, name="index"),
    path("registro", views.Registro, name='registro'),
    path("login", views.Login, name='login'),
    path("nova_loja", views.Cadastro_Loja, name='nova_loja'),
    path("add_produto", views.Add_Produto, name="add_produto"),
    path("Produto/<int:id_produto>/",views.pagina_produto, name="pagina_produto"),
    path("/<str:nome_loja>/", views.pagina_loja, name="loja"),
    path("pesquisa/<str:nome_pesquisado>/", views.pesquisa, name="pesquisa"),
]