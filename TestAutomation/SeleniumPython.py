# ============================================
# Title: Web Auth Flow (Selenium + pytest)
# Requirements:
# - Python 3.10+
# - pytest
# - selenium 4.x
# - Chrome/Chromedriver (or swap to Firefox/Gecko)
# Behavior:
# - Login success (valid creds)
# - Login failure (invalid password)
# - Logout success
# - Explicit waits, Page Object Model, env-based secrets
# Env Vars:
#   BASE_URL=https://your-app.example.com
#   USER_EMAIL=qa@example.com
#   USER_PASSWORD=correct-horse-battery-staple
# ============================================

import os
import time
from dataclasses import dataclass

import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ---------- Config & Fixtures ----------

@dataclass
class Creds:
    email: str
    password: str

@pytest.fixture(scope="session")
def base_url() -> str:
    url = os.environ.get("BASE_URL", "http://localhost:3000")
    return url.rstrip("/")

@pytest.fixture(scope="session")
def creds() -> Creds:
    return Creds(
        email=os.environ.get("USER_EMAIL", "user@example.com"),
        password=os.environ.get("USER_PASSWORD", "password123"),
    )

@pytest.fixture
def driver():
    opts = ChromeOptions()
    if os.environ.get("HEADLESS", "1") == "1":
        opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1400,1000")
    opts.add_argument("--disable-gpu")
    d = webdriver.Chrome(options=opts)
    d.set_page_load_timeout(30)
    d.implicitly_wait(0)  # rely on explicit waits
    yield d
    d.quit()


# ---------- Page Objects ----------

class LoginPage:
    # Use test-friendly data-test attributes when possible
    EMAIL = (By.CSS_SELECTOR, '[data-test="email"]')
    PASSWORD = (By.CSS_SELECTOR, '[data-test="password"]')
    SUBMIT = (By.CSS_SELECTOR, '[data-test="login-submit"]')
    ERROR = (By.CSS_SELECTOR, '[data-test="login-error"]')

    def __init__(self, driver):
        self.d = driver
        self.wait = WebDriverWait(self.d, 15)

    def load(self, base_url: str):
        self.d.get(f"{base_url}/login")
        self.wait.until(EC.visibility_of_element_located(self.EMAIL))

    def login(self, email: str, password: str):
        self.d.find_element(*self.EMAIL).clear()
        self.d.find_element(*self.EMAIL).send_keys(email)
        self.d.find_element(*self.PASSWORD).clear()
        self.d.find_element(*self.PASSWORD).send_keys(password)
        self.d.find_element(*self.SUBMIT).click()

    def error_text(self) -> str:
        el = self.wait.until(EC.visibility_of_element_located(self.ERROR))
        return el.text.strip()


class DashboardPage:
    AVATAR = (By.CSS_SELECTOR, '[data-test="avatar"]')      # post-login sentinel
    MENU = (By.CSS_SELECTOR, '[data-test="menu"]')
    LOGOUT = (By.CSS_SELECTOR, '[data-test="logout"]')

    def __init__(self, driver):
        self.d = driver
        self.wait = WebDriverWait(self.d, 15)

    def wait_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.AVATAR))

    def logout(self):
        self.d.find_element(*self.MENU).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT)).click()


# ---------- Tests ----------

def test_web_login_success(driver, base_url, creds):
    """Happy-path: user logs in and sees dashboard avatar."""
    lp = LoginPage(driver)
    lp.load(base_url)
    lp.login(creds.email, creds.password)

    dash = DashboardPage(driver)
    dash.wait_loaded()
    assert "/dashboard" in driver.current_url

def test_web_login_invalid_password(driver, base_url, creds):
    """Negative: invalid password shows error banner."""
    lp = LoginPage(driver)
    lp.load(base_url)
    lp.login(creds.email, "wrong-password")
    msg = lp.error_text()
    assert "invalid" in msg.lower() or "incorrect" in msg.lower()

def test_web_logout(driver, base_url, creds):
    """User can log out from dashboard and is sent back to /login."""
    lp = LoginPage(driver)
    lp.load(base_url)
    lp.login(creds.email, creds.password)

    dash = DashboardPage(driver)
    dash.wait_loaded()
    dash.logout()
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
