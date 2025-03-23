from configparser import ConfigParser

class BasePage:
    def __init__(self, page):
        self.page = page
        self.config = ConfigParser()
        self.base_url = self.config.get("Settings", "base_url", fallback="https://www.saucedemo.com/")
    
    async def go_to_base_page(self):
        await self.page.goto(self.base_url)