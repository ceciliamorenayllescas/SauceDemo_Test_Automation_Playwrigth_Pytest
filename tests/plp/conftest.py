import pytest
from utilities.browser_manager import BrowserManager
from pages.base_page import BasePage
import os

SESSION_PATH = "data/session_data.json"

@pytest.fixture(scope="session")
async def browser():
    browser_manager = BrowserManager()
    browser = await browser_manager.launch_browser()
    yield browser
    await browser_manager.close_browser()
    if os.path.exists(SESSION_PATH):
        os.remove(SESSION_PATH)

@pytest.fixture(scope="function")
async def auth_context(browser):
    if os.path.exists(SESSION_PATH):
        context = await browser.new_context(storage_state=SESSION_PATH)
    else:
        context = await browser.new_context()
        page = await context.new_page()
    try:
            await page.goto("https://saucedemo.com/", timeout=30000)
            await page.locator("#user-name").fill("standard_user")
            await page.locator("#password").fill("secret_sauce")
            await page.locator("#login-button").click()
            await page.wait_for_selector(".inventory_list", timeout=5000)
            
            await context.storage_state(path=SESSION_PATH)  # Guarda sesión
        
    except Exception as e:
        await context.close()
        pytest.fail(f"Error durante la autenticación: {str(e)}")
    
    yield context
    await context.close()
    

@pytest.fixture(scope="function")
async def page(auth_context):
    pages = auth_context.pages
    if pages:
        page = pages[-1]
    else:
        page = await auth_context.new_page()

    yield page
    await page.close()


@pytest.fixture
async def base_page(page):
    return BasePage(page)