from playwright.sync_api import Page, expect


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def acessar(self):
        self.page.goto(
            "http://localhost/Login",
            wait_until="networkidle"
        )

    def logar(self, usuario, senha):

        campo_usuario = self.page.locator(
            "[data-test='username']"
        )

        expect(campo_usuario).to_be_visible(timeout=10000)

        campo_usuario.fill(usuario)

        self.page.get_by_role(
            "textbox",
            name="Digite aqui a sua senha"
        ).fill(senha)

        self.page.locator(
            "[data-test='login-btn']"
        ).click()

        expect(
            self.page.locator(
                "[data-test='search-screen-input']"
            )
        ).to_be_visible(timeout=10000)