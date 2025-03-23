from pages.base_page import BasePage
from playwright.async_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.base_page = BasePage(page)
        self.login_url = self.base_page.base_url
        self.user_field = page.locator("#user-name")
        self.password_field = page.locator("#password")
        self.submit_button = page.locator("#login-button")
        self.error_message = page.locator(".error-message-container")
        self.title = page.locator(".login_logo")
        self.error_icons = page.locator(".error_icon")
        self.error_button = page.locator(".error-button")
    
    async def login(self, username: str, password: str)-> None:
        await self.user_field.fill(username)
        await self.password_field.fill(password)
        await self.submit_button.click()
    
    async def browser_title_should_be(self, title_expected: str) -> None:
        browser_title = await self.page.title()
        assert browser_title == title_expected, f"The expected title was {title_expected}, but the obtained is {browser_title}"

    async def inner_title_should_be(self, title_expected: str) -> None:
        await expect(self.title).to_have_text(title_expected), f"The expected title was {title_expected}, but the obtained is {self.title}"

    async def error_message_should_be_visible(self)-> None:
        await expect(self.error_message).to_be_visible(), "The message container is not visible"
    
    async def error_icons_should_be_visible_and_should_be(self, number_of_expected_icons):
        actual_amount = await self.error_icons.count()
        await expect(self.error_icons).to_be_visible()
        assert actual_amount == number_of_expected_icons, f"The expected number of icons was {number_of_expected_icons}, but the obtained is {actual_amount}"

    async def close_error_message(self):
        await self.error_button.click()

    async def error_icons_and_cointainer_should_not_be_visible(self, number_of_expected_icons):
        await expect(self.error_icons).not_to_be_visible()
        await expect(self.error_message).not_to_be_visible()


    async def error_icons_should_be_visible_and_should_be(self, number_of_expected_icons):
        actual_amount = await self.error_icons.count()
        await expect(self.error_icons).to_be_visible()
        assert actual_amount == number_of_expected_icons, f"The expected number of icons was {number_of_expected_icons}, but the obtained is {actual_amount}"


    async def url_is(self, expected_url)->None:
        actual_url = self.page.url
        assert await self.page.url == expected_url, f"The expected url was {expected_url}, but the actual url is {actual_url}"