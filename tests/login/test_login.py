from playwright.async_api import async_playwright, Page
import pytest
from utilities.browser_manager import BrowserManager
from utilities.csv_parser import CsvParser


login_data = CsvParser("data/login_cases.csv")


@pytest.mark.asyncio(loop_scope= "session")
async def test_navigate_to_login_page(page, base_page):
    await base_page.go_to_base_page()