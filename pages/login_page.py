import re
from playwright.sync_api import expect

class loginPage:
    def __init__(self, page) -> None:
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.username_block= page.get_by_role("textbox", name="Username")
        self.password_block= page.get_by_role("textbox", name="Password")
        self.login = page.get_by_role("button",  name="Login")

    def add_username(self, username:str):
        self.username_block.fill(username)

    def add_password(self, password:str):
        self.password_block.fill(password)
    
    def loginSetup(self, username:str, password:str):
        self.add_username(username)
        self.add_password(password)
        self.login.click()