# ============================================
# Title: Mobile Auth Flow (Appium + pytest)
# Requirements:
# - Python 3.10+
# - pytest
# - Appium-Python-Client >= 3.x
# - Appium Server running (Appium 2.x recommended)
# Behavior:
# - Login success (valid creds)
# - Login failure (invalid password)
# - Optional OTP hook for 2FA (stubbed)
# Android Capabilities (env-driven):
#   APPIUM_URL=http://127.0.0.1:4723
#   PLATFORM_NAME=Android
#   DEVICE_NAME=emulator-5554
#   APP_PACKAGE=com.example.app
#   APP_ACTIVITY=.MainActivity
#   USER_EMAIL=qa@example.com
#   USER_PASSWORD=correct-horse-battery-staple
# iOS Notes:
#   - Use platformName=iOS, automationName=XCUITest, bundleId, udid
#   - Replace Android-specific locator strategies with iOS ones (accessibility id)
# ============================================

import os
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ---------- Fixtures ----------

@pytest.fixture
def mobile_driver():
    caps = {
        "platformName": os.environ.get("PLATFORM_NAME", "Android"),
        "automationName": os.environ.get("AUTOMATION_NAME", "UiAutomator2"),
        "deviceName": os.environ.get("DEVICE_NAME", "emulator-5554"),
        # For real app testing, either provide `app` path or use package/activity
        "appPackage": os.environ.get("APP_PACKAGE", "com.example.app"),
        "appActivity": os.environ.get("APP_ACTIVITY", ".MainActivity"),
        # Prevents session dying on app background/foreground
        "newCommandTimeout": 180,
        # Speeds up interactions if using WebView (toggle if needed)
        "autoGrantPermissions": True,
    }
    server = os.environ.get("APPIUM_URL", "http://127.0.0.1:4723")
    drv = webdriver.Remote(server, caps)
    drv.implicitly_wait(0)
    yield drv
    drv.quit()


# ---------- Page Objects (Android) ----------

class LoginScreen:
    # Prefer accessibility ids if your app sets them (content-desc / testID)
    EMAIL = (By.ID, "com.example.app:id/input_email")
    PASSWORD = (By.ID, "com.example.app:id/input_password")
    SUBMIT = (By.ID, "com.example.app:id/btn_login")
    ERROR = (By.ID, "com.example.app:id/text_error")

    def __init__(self, d):
        self.d = d
        self.wait = WebDriverWait(d, 20)

    def wait_loaded(self):
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


class HomeScreen:
    AVATAR = (By.ID, "com.example.app:id/home_avatar")  # post-login sentinel
    MENU = (By.ID, "com.example.app:id/home_menu")
    LOGOUT = (By.ID, "com.example.app:id/menu_logout")

    def __init__(self, d):
        self.d = d
        self.wait = WebDriverWait(d, 20)

    def wait_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.AVATAR))

    def logout(self):
        self.d.find_element(*self.MENU).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT)).click()


# ---------- Optional OTP Hook (stub) ----------

def get_test_otp(email: str) -> str:
    """
    Stub showing where you’d fetch a one-time password:
      - Read from test mailbox
      - Query a testing-only backend endpoint
      - Pull last SMS via emulator or gateway
    For demo, return a fixed OTP used by a test backend.
    """
    return os.environ.get("TEST_OTP", "000000")


# ---------- Tests ----------

@pytest.fixture(scope="session")
def mobile_creds():
    return {
        "email": os.environ.get("USER_EMAIL", "user@example.com"),
        "password": os.environ.get("USER_PASSWORD", "password123"),
    }

def test_mobile_login_success(mobile_driver, mobile_creds):
    """Happy-path: valid creds lead to Home screen; handles optional OTP."""
    login = LoginScreen(mobile_driver)
    login.wait_loaded()
    login.login(mobile_creds["email"], mobile_creds["password"])

    # If your flow conditionally shows OTP screen, handle it here:
    # Example locators for OTP (replace with your app’s ids)
    try:
        otp_input = WebDriverWait(mobile_driver, 3).until(
            EC.visibility_of_element_located((By.ID, "com.example.app:id/input_otp"))
        )
        otp_input.send_keys(get_test_otp(mobile_creds["email"]))
        mobile_driver.find_element(By.ID, "com.example.app:id/btn_otp_submit").click()
    except Exception:
        # No OTP shown (e.g., testing build disables it) -> continue
        pass

    home = HomeScreen(mobile_driver)
    home.wait_loaded()
    # If deep-linking is supported, you could also assert current activity/intent
    assert home.d.find_element(*home.AVATAR).is_displayed()

def test_mobile_login_invalid_password(mobile_driver, mobile_creds):
    """Negative: invalid pwd shows an error label."""
    login = LoginScreen(mobile_driver)
    login.wait_loaded()
    login.login(mobile_creds["email"], "wrong-password")
    msg = login.error_text()
    assert "invalid" in msg.lower() or "incorrect" in msg.lower()

def test_mobile_logout(mobile_driver, mobile_creds):
    """User can log out and is returned to Login."""
    login = LoginScreen(mobile_driver)
    login.wait_loaded()
    login.login(mobile_creds["email"], mobile_creds["password"])

    home = HomeScreen(mobile_driver)
    home.wait_loaded()
    home.logout()

    # Verify we’re back to the login screen
    WebDriverWait(mobile_driver, 10).until(
        EC.visibility_of_element_located(LoginScreen.EMAIL)
    )
