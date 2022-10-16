import re
from playwright.sync_api import Page, expect


def test_homepage(page: Page):
    page.goto("http://localhost:8000/")
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Piccolo Theme"))

    # Github Link
    page.locator('#toggle_sidebar').click()
    expect(page.locator('.sphinxsidebar')
           ).to_have_attribute("style", "display: none;")

    # Github Link
    page.locator('#source_link').click()
    expect(page).to_have_url(re.compile(
        'https://github.com/piccolo-orm/piccolo_theme/'))

    # Dark Mode
    page.goto("http://localhost:8000/")
    expect(page.locator('html')).to_have_attribute("data-mode", "light")
    page.locator("#mode_toggle").click()
    expect(page.locator('html')).to_have_attribute("data-mode", "dark")
    page.locator("#mode_toggle").click()
    expect(page.locator('html')).to_have_attribute("data-mode", "darkest")

    # Search for Configuration
    page.goto("http://localhost:8000/")
    page.locator(
        '//*[@id="searchbox"]/div/form/input[1]').fill("Configuration")
    page.locator('//*[@id="searchbox"]/div/form/input[2]').click()
    expect(page).to_have_title(re.compile("Search"))

    # Check external Sphinx Link
    page.goto("http://localhost:8000/")
    link = page.locator('//*[@id="piccolo-theme"]/p/a')
    expect(link).to_have_text("Sphinx")
    expect(link).to_have_attribute(
        "href", "https://www.sphinx-doc.org/en/master/")

    # Link Check Setup
    page.goto("http://localhost:8000/")
    page.locator('//*[@id="piccolo-theme"]/div/ul/li[1]/a').click()
    expect(page).to_have_title(re.compile("Setup"))