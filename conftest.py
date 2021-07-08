import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language',\
                    action='store',\
                    default="chrome",\
                    help="Choose language:")
    parser.addoption('--browser_name', \
                    action='store',\
                    default=None,\
                    help="Choose browser(chrome or firefox):")

@pytest.fixture(scope="function")
def browser(request):
    browser_name=request.config.getoption("browser_name")
    language_name=request.config.getoption("language")
    if(browser_name=="chrome"):
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
        print("Starting chrome for test...")
        browser = webdriver.Chrome(options=options)
    elif(browser_name=="firefox"):
        fp=webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages",language_name)
        print("Starting firefox for test...")
        browser=webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--Check all needed flags that had to be specified")
    yield browser
    print("\nquit browser..")
    browser.quit()