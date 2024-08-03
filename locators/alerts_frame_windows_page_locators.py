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


class FramePageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    SECOND_FRAME = (By.CSS_SELECTOR, "iframe[id='frame2']")
    TITLE_OF_FRAME = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    PARENT_FRAME_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    CHILD_FRAME_TEXT = (By.CSS_SELECTOR, "p")


class ModelDialogsPageLocators:
    # small button
    SMALL_MODEL_BUTTON = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    BODY_OF_SMALL_MODEL_BUTTON = (By.CSS_SELECTOR, "div[class='modal-body']")
    TITLE_OF_SMALL_MODEL_BUTTON = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-sm']")
    CLOSE_SMALL_MODEL_BUTTON = (By.CSS_SELECTOR, "button[id='closeSmallModal']")

    # large button
    LARGE_MODEL_BUTTON = (By.CSS_SELECTOR, "button[id='showLargeModal']")
    BODY_OF_LARGE_MODEL_BUTTON = (By.CSS_SELECTOR, "div[class='modal-body']")
    TITLE_OF_LARGE_MODEL_BUTTON = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-lg']")
    CLOSE_LARGE_MODEL_BUTTON = (By.CSS_SELECTOR, "button[id='closeLargeModal']")
