import pytest
from utilities.browser_manager import BrowserManager
from pages.base_page import BasePage

@pytest.fixture(scope="session")
async def browser():
    browser_manager = BrowserManager()
    browser = await browser_manager.launch_browser()
    yield browser
    await browser_manager.close_browser()

@pytest.fixture(scope="function")
async def context(browser):
    context = await browser.new_context()
    yield context
    await context.close()

@pytest.fixture(scope="function")
async def page(context):
    page = await context.new_page()
    yield page
    await page.close()


@pytest.fixture
async def base_page(page):
    return BasePage(page)