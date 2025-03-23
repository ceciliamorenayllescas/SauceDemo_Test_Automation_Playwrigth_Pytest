from playwright.async_api import async_playwright, Page
import pytest
from utilities.browser_manager import BrowserManager
from utilities.csv_parser import CsvParser

login_data = CsvParser("data/login_cases.csv")

@pytest.mark.asyncio(loop_scope= "session")
async def test_navigate_to_login_page(base_page, login_page):
    #When I go to the base page
    await base_page.go_to_base_page()
    #Then the browser title is Swag Labs
    await login_page.browser_title_should_be("Swag Labs")
    #And the inner title of the page body is also "Swag Labs"
    await login_page.inner_title_should_be("Swag Labs")

@pytest.mark.asyncio(loop_scope="session")
async def test_correct_username_and_correct_password(base_page, login_page):
    username, password, expected_message = await login_data.filter_on_test_case_id("TC-1")
    #Given I'm in the base page
    await base_page.go_to_base_page()
    #When I login with valid credentials
    await login_page.login(username, password)
    #Then I'm redirected to the Product list page
    await login_page.should_be_redirected_to(base_page.base_url + "inventory.html") 

@pytest.mark.asyncio(loop_scope="session")
async def test_incorrect_username_and_correct_password(base_page, login_page):
    username, password, expected_message = await login_data.filter_on_test_case_id("TC-4")
    #Given I'm in the base page
    await base_page.go_to_base_page()
    #When I login with valid credentials
    await login_page.login(username, password)
    #Then Should produce an error message "Epic sadface: Username and password do not match any user in this service"
    await login_page.error_message_should_be_visible()
    await login_page.error_message_should_be(expected_message)
    #And there are 2 icons of error
    await login_page.error_icons_should_be_visible_and_should_be(2)

@pytest.mark.asyncio(loop_scope="session")
async def test_correct_username_and_incorrect_password(base_page, login_page):
    username, password, expected_message = await login_data.filter_on_test_case_id("TC-5")
    #Given I'm in the base page
    await base_page.go_to_base_page()
    #When I login with valid credentials
    await login_page.login(username, password)
    #Then Should produce an error message "Epic sadface: Username and password do not match any user in this service"
    await login_page.error_message_should_be_visible()
    await login_page.error_message_should_be(expected_message)
    #And there are 2 icons of error
    await login_page.error_icons_should_be_visible_and_should_be(2)

@pytest.mark.asyncio(loop_scope="session")
async def test_incorrect_username_and_incorrect_password(base_page, login_page):
    username, password, expected_message = await login_data.filter_on_test_case_id("TC-6")
    #Given I'm in the base page
    await base_page.go_to_base_page()
    #When I login with valid credentials
    await login_page.login(username, password)
    #Then Should produce an error message "Epic sadface: Username and password do not match any user in this service"
    await login_page.error_message_should_be_visible()
    await login_page.error_message_should_be(expected_message)
    #And there are 2 icons of error
    await login_page.error_icons_should_be_visible_and_should_be(2)

@pytest.mark.asyncio(loop_scope="session")
async def test_locked_out_user(base_page, login_page):
    username, password, expected_message = await login_data.filter_on_test_case_id("TC-7")
    #Given I'm in the base page
    await base_page.go_to_base_page()
    #When I login with valid credentials
    await login_page.login(username, password)
    #Then Should produce an error message "Epic sadface: Sorry, this user has been locked out"
    await login_page.error_message_should_be_visible()
    await login_page.error_message_should_be(expected_message)
    #And there are 2 icons of error
    await login_page.error_icons_should_be_visible_and_should_be(2)

@pytest.mark.asyncio(loop_scope="session")
async def test_empty_username(base_page, login_page):
    username, password, expected_message = await login_data.filter_on_test_case_id("TC-8")
    #Given I'm in the base page
    await base_page.go_to_base_page()
    #When I login with valid credentials
    await login_page.login(username, password)
    #Then Should produce an error message "Epic sadface: Username is required"
    await login_page.error_message_should_be_visible()
    await login_page.error_message_should_be(expected_message)
    #And there are 2 icons of error
    await login_page.error_icons_should_be_visible_and_should_be(2)

@pytest.mark.asyncio(loop_scope="session")
async def test_empty_password(base_page, login_page):
    username, password, expected_message = await login_data.filter_on_test_case_id("TC-9")
    #Given I'm in the base page
    await base_page.go_to_base_page()
    #When I login with valid credentials
    await login_page.login(username, password)
    #Then Should produce an error message "Epic sadface: Password is required"
    await login_page.error_message_should_be_visible()
    await login_page.error_message_should_be(expected_message)
    #And there are 2 icons of error
    await login_page.error_icons_should_be_visible_and_should_be(2)

@pytest.mark.asyncio(loop_scope="session")
async def test_empty_username_and_password(base_page, login_page):
    username, password, expected_message = await login_data.filter_on_test_case_id("TC-10")
    #Given I'm in the base page
    await base_page.go_to_base_page()
    #When I login with valid credentials
    await login_page.login(username, password)
    #Then Should produce an error message "Epic sadface: Username is required"
    await login_page.error_message_should_be_visible()
    await login_page.error_message_should_be(expected_message)
    #And there are 2 icons of error
    await login_page.error_icons_should_be_visible_and_should_be(2)

@pytest.mark.asyncio(loop_scope="session")
async def test_close_error_message(base_page, login_page):
    username, password, expected_message = await login_data.filter_on_test_case_id("TC-11")
    #Given I'm in the base page
    await base_page.go_to_base_page()
    #When login and I get an error message
    await login_page.login(username, password)
    await login_page.error_message_should_be_visible()
    await login_page.error_icons_should_be_visible_and_should_be(2)
    #And I close the container
    await login_page.close_error_message()
    #Then The error message and the error icons should no visible anymore
    await login_page.error_icons_and_cointainer_should_not_be_visible()
    