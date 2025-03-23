class BasePage:
    def __init__(self, page):
        self.page = page
    async def go_to(self,url):
        await self.page.goto(url)