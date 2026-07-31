import uuid

from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.produto_page import ProdutoPage


def test_cadastrar_produto(page: Page):
    login = LoginPage(page)
    produto = ProdutoPage(page)

    # Login
    login.acessar()

    login.logar(
        "admin",
        "123456"
    )

    # Aguarda o último elemento da tela principal carregar
    expect(
        page.get_by_text("Informações", exact=True)
    ).to_be_visible(timeout=15000)

    # Aguarda o sistema "aquecer" (índices/cache) após o primeiro carregamento
    page.wait_for_load_state("networkidle", timeout=15000)

    # Pesquisa a tela Cadastro de Produto
    produto.acessar_cadastro()

    # Gera uma descrição única para o produto a cada execução
    descricao_produto = f"Produto Teste {uuid.uuid4().hex[:8]}"

    # Preenche os dados básicos
    produto.cadastrar_produto(
        descricao=descricao_produto,
        grupo="1",
        preco_custo="10",
        preco_venda="20"
    )

    # Preenche informações fiscais
    produto.preencher_informacoes_fiscais(
        regra_imposto="CFOP 5102 - CSOSN 0102 - TRIBUTADO",
        ncm="99999999"
    )

    # Grava o produto
    produto.gravar_produto()