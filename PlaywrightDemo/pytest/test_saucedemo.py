
import pytest

def test_title(page):
    page.goto("https://www.saucedemo.com/")
    assert page.title() == "Swag Labs"

def test_inventory_site(page):
    page.goto("https://www.saucedemo.com/inventory.html")
    assert page.inner_text('h3') =="Epic sadface: You can only access '/inventory.html' when you are logged in."