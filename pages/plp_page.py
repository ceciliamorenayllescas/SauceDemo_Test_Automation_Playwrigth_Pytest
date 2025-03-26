from pages.base_page import BasePage
from playwright.async_api import Page, expect

class PLP:
    def __init__(self, page: Page):
        self.page = page
        self.base_page = BasePage(page)
        self.url = self.base_page.base_url + "/inventory.html"
        self.app_logo_title = self.page.locator(".app_logo")
        self.container_tile = self.page.locator(".title")
        self.inventory_container = self.page.locator("#inventory_container")
        self.inventory_list = self.page.locator(".inventory_list")
        self.inventory_items = self.page.locator(".inventory_item")
        self.inventory_items_name_link = self.page.locator(".inventory_item_name")
        self.inventory_items_description = self.page.locator(".inventory_item_desc")
        self.inventory_intes_price = self.page.locator(".inventory_item_price")
        self.inventory_add_to_cart_button = self.page.locator('button:has-text("Add to cart")')
        self.inventory_remove_button = self.page.locator('button:has-text("Remove")')
        self.shopping_cart_link = self.page.locator(".shopping_cart_link")
        self.shopping_cart_number = self.page.locator(".shopping_cart_badge")
        self.sort_container = self.page.locator(".product_sort_container")
        self.name_a_to_z_option = self.page.get_by_text("Name (A to Z)")
        self.name_z_to_a_option = self.page.get_by_text("Name (Z to A)")
        self.price_low_to_high_option = self.page.get_by_text("Price (low to high)")
        self.price_high_to_low_opcion = self.page.get_by_text("Price (high to low)")
        self.footer = self.page.locator(".footer_copy") #© 2025 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy

    async def container_title_is(self, expected_title: str):
        await expect(self.container_title).to_have_text(expected_title)

    async def page_title_is(self, expected_title: str):
        await expect(self.app_logo_tile).to_have_text(expected_title)
    
    async def footer_have_text(self, expected_footer: str):
        await expect(self.footer).to_have_text(expected_footer)
    
    async def get_number_of_items_in_cart(self):
        if await self.shopping_cart_number.is_visible():
            number = int(await self.shopping_cart_number.text_content())
        else:
            number = 0
        return number
    
    async def add_an_item_to_cart(self, product_name: str):
        number_of_items_in_cart = await self.get_number_of_items_in_cart()

        product = await self.page.locator(f'.inventory_item:has-text("{product_name}")')
        add_to_cart_button= await product.locator('button:has-text("Add to cart")')
        await add_to_cart_button.click()

        actual_number_of_items_in_cart = await self.get_number_of_items_in_cart()

        assert actual_number_of_items_in_cart == (number_of_items_in_cart + 1), "The number of items in cart doesn't match with the expected"
    
    async def add_items_to_cart(self, products_names: list):
        number_of_items_in_cart = await self.get_number_of_items_in_cart()
        items_number = len(products_names)

        for i in items_number:
            product = await self.page.locator(f'.inventory_item:has-text("{products_names[i]}")')
            add_to_cart_button = await product.locator('button:has-text("Add to cart")')
            await add_to_cart_button.click()

        actual_number_of_items_in_cart = await self.get_number_of_items_in_cart()

        assert actual_number_of_items_in_cart == (number_of_items_in_cart + items_number), "The number of items in cart doesn't match with the expected"
    
    async def remove_button_is_visible(self, products_names:list):
        items_number = len(products_names)

        for i in items_number:
            product = await self.page.locator(f'.inventory_item:has-text("{products_names[i]}")')
            remove_button = await product.locator('button:has-text("Remove")')
            await expect(remove_button).to_be_visible(), "The remove button is not visible for item " + i

    async def add_to_cart_button_is_visible(self, products_names:list):
        items_number = len(products_names)

        for i in items_number:
            product = await self.page.locator(f'.inventory_item:has-text("{products_names[i]}")')
            add_to_cart_button = await product.locator('button:has-text("Add to cart")')
            await expect(add_to_cart_button).to_be_visible(), "The Add to cart button is not visible for item " + i
    
    async def remove_item_from_cart(self, product_name:str):
        product = await self.page.locator(f'.inventory_item:has-text("{product_name}")')
        remove_button = await product.locator('button:has-text("Remove")')
        await expect(remove_button).to_be_visible(), "The remove button is not visible for item "
        await remove_button.click()


    async def remove_items_from_cart(self, products_names:list):
        number_of_items_in_cart = await self.get_number_of_items_in_cart()
        items_number = len(products_names)

        for i in items_number:
            product = await self.page.locator(f'.inventory_item:has-text("{products_names[i]}")')
            remove_button = await product.locator('button:has-text("Remove")')
            await expect(remove_button).to_be_visible(), "The remove button is not visible for item " + i

        actual_number_of_items_in_cart = await self.get_number_of_items_in_cart()

        assert actual_number_of_items_in_cart == (number_of_items_in_cart - items_number), "The number of items in cart doesn't match with the expected"

    async def go_to_cart(self):
        await self.shopping_cart_link.click()

    async def open_product_detail(self, product_name):
        product = self.page.locator(f'.inventory_item_name:has-text("{product_name}")')
        await product.click()
    
    async def sort_list_by(self, filter: str):
        pass

