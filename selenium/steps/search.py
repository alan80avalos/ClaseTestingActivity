# -*- coding: utf-8 -*-

"""
Exercise test using Behavior-Driven Development (BDD) with Behave (Gherkin) and Selenium.´
"""

from behave import given, then, when  # pylint: disable=no-name-in-module
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver


@given("I am on the Google homepage")  # pylint: disable=not-callable
def open_browser(context):
    """Opens Google in Chrome."""
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    context.driver = webdriver.Chrome(options=options)
    context.driver.get("https://www.google.com") 


@when('I search for "{query}"')  # pylint: disable=not-callable
def search(context, query):
    """Searches something in Google."""
    search_box = context.driver.find_element("id", "APjFqb")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    delay = 5  # seconds
    wait = WebDriverWait(context.driver, delay)
    wait.until(EC.presence_of_element_located((By.ID, "rcnt")))

@when('I open the first results')
def openFirstResult(context):
    wait = WebDriverWait(context.driver, 10)
    first_result = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//a[.//h3])[1]"))
    )
    first_result.click()

@then(  # pylint: disable=not-callable
    'I should be on a page with domain "{query}"'
)
def verify_domain(context, query):
    """j"""
    wait = WebDriverWait(context.driver, 10)
    wait.until(lambda driver: query in driver.current_url)
    assert query in context.driver.current_url

    context.current_domain = query

@when('I search "{query}" in the current university site')
def search_in_current_university_site(context, query):
    """Busca dentro del sitio de la universidad actual."""

    wait = WebDriverWait(context.driver, 10)
    domain = context.current_domain
    if "iteso.mx" in domain:
        #Es necesario primero click en la lupa 
        search_icon = wait.until(
            EC.element_to_be_clickable((By.ID, "icon-search"))
        )
        context.driver.execute_script("arguments[0].click();", search_icon)

        search_box = wait.until(
            EC.element_to_be_clickable((By.ID, "ipt-search"))
        )
    elif "cucei.udg.mx" in domain:
        search_box = wait.until(
            EC.element_to_be_clickable((By.ID, "edit-search-block-form--2"))
        )
    elif "uvm.mx" in domain:
        #Tambien es necesario primero click en lupa
        search_icon = wait.until(
            EC.element_to_be_clickable((By.ID, "icon-search"))
        )
        search_icon.click()

        search_box = wait.until(
            EC.element_to_be_clickable((By.ID, "buscartxt"))
        )
    else:
        raise ValueError(f"No hay buscador configurado para el dominio: {domain}")

    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

@then('I should see results related to "{query}"')
def verify_expected_result(context, query):
    """aaa"""
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    page_text = context.driver.find_element(By.TAG_NAME, "body").text.lower()

    try:
        assert query.lower() in page_text
    finally:
        context.driver.quit()
