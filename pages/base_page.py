from configparser import ConfigParser
from playwright.async_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.config = ConfigParser()
        self.base_url = self.config.get("Settings", "base_url", fallback="https://www.saucedemo.com/")
    
    async def go_to_base_page(self):
        await self.page.goto(self.base_url)