from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def driver():
    """Setup Chrome in headless mode for Codespaces (no GUI)."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

def test_google_title(driver):
    """Test 1: Check Google homepage title."""
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    print(f"Test 1 Passed - Page title is: {driver.title}")

def test_google_search_box_exists(driver):
    """Test 2: Check that the Google search box exists."""
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    assert search_box is not None
    print("Test 2 Passed - Search box found on Google homepage")

def test_google_search(driver):
    """Test 3: Perform a Google search and verify results."""
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Jenkins CI/CD")
    search_box.submit()
    assert "Jenkins" in driver.title or "jenkins" in driver.page_source.lower()
    print(f"Test 3 Passed - Search results page title: {driver.title}")

def test_python_org(driver):
    """Test 4: Test Python.org website."""
    driver.get("https://www.python.org")
    assert "Python" in driver.title
    print(f"Test 4 Passed - Python.org title: {driver.title}")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
