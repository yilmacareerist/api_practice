import re
from playwright.sync_api import Page, expect

def test_homepage_title(page: Page):
    """Verify that the home page loads with the expected title."""
    page.goto("https://automationexercise.com/")
    expect(page).to_have_title(re.compile("Automation Exercise", re.IGNORECASE))

def test_navigate_to_contact_us(page: Page):
    """Verify navigation to the Contact Us page and check a header."""
    page.goto("https://automationexercise.com/")
    
    # Click the 'Contact us' link using accessible role
    page.get_by_role("link", name="Contact us").click()
    
    # Assert the URL and heading
    expect(page).to_have_url(re.compile(r"/contact_us"))
    heading = page.get_by_role("heading", name="Get In Touch")
    expect(heading).to_be_visible()