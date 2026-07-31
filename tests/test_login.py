from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


def test_login(page: Page):

    login = LoginPage(page)

    login.acessar()

    login.logar(
        "admin",
        "123456"
    )

    # Assertion explícita: confirma que o login foi bem-sucedido
    expect(
        page.locator("[data-test='search-screen-input']")
    ).to_be_visible()