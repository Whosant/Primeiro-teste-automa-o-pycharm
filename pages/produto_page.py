from playwright.sync_api import Page, expect


class ProdutoPage:

    def __init__(self, page: Page):
        self.page = page


    def acessar_cadastro(self):

        campo_pesquisa = self.page.locator(
            "[data-test='search-screen-input']"
        )

        expect(campo_pesquisa).to_be_visible()

        campo_pesquisa.click()

        campo_pesquisa.press_sequentially(
            "cadastro de produto",
            delay=100
        )

        resultado = self.page.get_by_role(
            "option",
            name="Cadastro de Produto",
            exact=True
        )

        expect(resultado).to_be_visible(timeout=20000)

        resultado.click()

        expect(
            self.page.locator(
                "[data-test='txtDescricao']"
            )
        ).to_be_visible(timeout=10000)



    def cadastrar_produto(
        self,
        descricao,
        grupo,
        preco_custo,
        preco_venda
    ):

        campo_descricao = self.page.locator(
            "[data-test='txtDescricao']"
        )

        expect(campo_descricao).to_be_visible()

        campo_descricao.fill(
            descricao
        )


        campo_grupo = self.page.locator(
            "[data-test='txtGrupo']"
        )

        campo_grupo.fill(
            grupo
        )

        campo_grupo.press(
            "Enter"
        )


        self.page.locator(
            "[data-test='txtPrecoCusto']"
        ).fill(
            preco_custo
        )


        self.page.locator(
            "[data-test='txtPrecoVenda']"
        ).fill(
            preco_venda
        )



    def preencher_informacoes_fiscais(
        self,
        regra_imposto,
        ncm
    ):

        # Pausa fixa para conferir visualmente os dados preenchidos
        self.page.wait_for_timeout(3000)

        # Aba Informações Fiscais
        self.page.get_by_text(
            "Informações Fiscais",
            exact=True
        ).click()


        # Aguarda a grade carregar (localizada pela classe DevExtreme + texto da coluna)
        grade = self.page.locator(
            ".dx-datagrid"
        ).filter(
            has_text="Tipo de Regra de Imposto"
        )

        expect(grade).to_be_visible(timeout=15000)



        # Clica na célula da regra de imposto
        celula_regra = grade.locator(
            ".dx-data-row"
        ).first


        expect(celula_regra).to_be_visible()

        celula_regra.click()



        # Procura o combobox escopado dentro do tabPanel (evita pegar o campo de pesquisa do topo)
        combo = self.page.locator(
            "[data-test='tabPanel']"
        ).get_by_role(
            "combobox"
        )


        expect(combo).to_be_visible()

        combo.click()

        expect(combo).to_have_attribute(
            "aria-expanded",
            "true"
        )



        # Seleciona a regra (digitação simulada, tecla por tecla)
        combo.press_sequentially(
            regra_imposto,
            delay=100
        )


        # Localiza a opção pela classe do item do dropdown DevExtreme,
        # evitando conflito com <option> nativos escondidos na página
        opcao = self.page.locator(
            ".dx-list-item-content"
        ).get_by_text(
            regra_imposto,
            exact=True
        )


        expect(opcao).to_be_visible()


        opcao.click()



        # Campo NCM
        campo_ncm = self.page.locator(
            "[data-test='txtNCM']"
        )


        campo_ncm.scroll_into_view_if_needed()


        expect(campo_ncm).to_be_visible()


        campo_ncm.fill(
            ncm
        )


        campo_ncm.press(
            "Enter"
        )


    def gravar_produto(self):

        self.page.get_by_role(
            "button",
            name="Gravar",
            exact=True
        ).click()

        # Trata o popup "O produto não possui Código de Barras.
        # Deseja que o sistema gere?", clicando em "Sim" se ele aparecer
        botao_sim = self.page.get_by_role(
            "button",
            name="Sim",
            exact=True
        )

        try:
            botao_sim.click(timeout=3000)
        except Exception:
            pass

        expect(
            self.page.get_by_text(
                "gravado com sucesso"
            )
        ).to_be_visible(
            timeout=5000
        )
