from playwright.async_api import async_playwright
import configparser

class BrowserManager:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.config = configparser.ConfigParser()
        self.config.read('config/config.properties')
        self.base_url = self.config.get('Settings', 'base_url', fallback="https://www.saucedemo.com/")
        self.browser_type = self.config.get('Settings', 'browser', fallback='chromium')
        self.headless = self.config.getboolean("Settings", "headless", fallback="true")

    async def launch_browser(self):
        if self.playwright is None:
            self.playwright = await async_playwright().start()
        if self.browser is None:
            self.browser = await getattr(self.playwright, self.browser_type).launch(headless = self.headless)
            return self.browser
    
    async def close_browser(self):
        if self.browser:
            await self.browser.close()
            self.browser = None
        if self.playwright:
            await self.playwright.stop()
            self.playwright = None