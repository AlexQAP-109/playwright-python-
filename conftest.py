from Pages.page_metod import PageMetod
import pytest

@pytest.fixture()
def start(page):
    page = PageMetod(page)
    page.open_msk_rt_ru()
    return page