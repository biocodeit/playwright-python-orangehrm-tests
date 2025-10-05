import pytest
from pages.login_page import loginPage
from playwright.sync_api import expect


@pytest.mark.parametrize("username, password, locator",
                         [("","", "Required"),
                          ("","invalid1","Required"),
                          ("","admin123","Required"),
                          ("Admin","","Required"),
                          ("Admin","invalid1","Invalid credentials"),
                          ("Admin","admin123","Dashboard"),
                          ("admin","","Required"),
                          ("admin","invalid1","Invalid credentials"),
                          ("admin","admin123","Invalid credentials")])
def test_Case(page, username, password, locator):
        client = loginPage(page)
        client.loginSetup(username, password)
        if locator =="Dashboard":
            expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
        elif locator == "Invalid credentials":
            expect(page.get_by_text("Invalid credentials")).to_be_visible()
        else:
            expect(page.get_by_text("Required").first).to_be_visible()
