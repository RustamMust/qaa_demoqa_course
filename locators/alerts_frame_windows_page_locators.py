from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    TITLE_OF_NEW_OPENED_PAGE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    NEW_WINDOW_TAB = (By.CSS_SELECTOR, "button[id='windowButton']")


class AlertsPageLocators:
    ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    TIME_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    CONFIRM_RESULT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    PROMT_RESULT = (By.CSS_SELECTOR, "span[id='promptResult']")


