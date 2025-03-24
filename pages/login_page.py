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
    
    async def error_message_should_be(self, expected_error_message)-> None:
        actual_error_message = self.error_message
        await expect(actual_error_message).to_have_text(expected_error_message), f"The expected error message was {expected_error_message}, but the obtained is {actual_error_message}"
    
    async def error_icons_should_be_visible_and_should_be(self, number_of_expected_icons: int) -> None:
        actual_amount = await self.error_icons.count()
        if actual_amount == number_of_expected_icons:
            for i in range(actual_amount):
                assert await self.error_icons.nth(i).is_visible(), f"El ícono {i} no está visible"

    async def close_error_message(self) -> None:
        await self.error_button.click()

    async def error_icons_and_cointainer_should_not_be_visible(self)->None:
        for i in range(await self.error_icons.count()):
                assert not await self.error_icons.nth(i).is_visible() , f"El ícono {i} sigue visible"
        await expect(self.error_message).to_be_visible()

    async def should_be_redirected_to(self, expected_url: str)->None:
        actual_url = self.page.url
        assert self.page.url == expected_url, f"The expected url was {expected_url}, but the actual url is {actual_url}"