from django.urls import path
from . import views

urlpatterns =[
    path("registro", views.Registro, name='registro'),
    path("login", views.Login, name='login'),
    path("nova_loja", views.Cadastro_Loja, name='nova_loja'),
    path("add_produto", views.Add_Produto, name="add_produto"),
    path("home", views.product_list, name="home"),
    path("pesquisa?<str:nome_pesquisado>/", views.pesquisa, name="pesquisa"),
    path("/<str:nome_loja>/", views.pagina_loja, name="loja"),
]