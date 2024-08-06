from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_SECTION_HEADING = (By.CSS_SELECTOR, "div[id='section1Heading']")
    FIRST_SECTION_TEXT = (By.CSS_SELECTOR, "div[id='section1Content']")
    SECOND_SECTION_HEADING = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECOND_SECTION_TEXT = (By.CSS_SELECTOR, "div[id='section2Content']")
    THIRD_SECTION_HEADING = (By.CSS_SELECTOR, "div[id='section3Heading']")
    THIRD_SECTION_TEXT = (By.CSS_SELECTOR, "div[id='section3Content']")


class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    MULTI_VALUE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value']")
    SINGLE_MULTI_VALUE_REMOVE = (
        By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value'] svg path")
    REMOVE_ALL_MULTI_VALUES_BUTTON = (By.CSS_SELECTOR, "div[class='auto-complete__indicators css-1wy0on6'] svg")
    SINGLE_VALUE = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")
    SINGLE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")


class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")
    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item ']")
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")


class SliderPageLocators:
    INPUT_VALUE = (By.CSS_SELECTOR, "input[id='sliderValue']")
    SLIDER = (By.CSS_SELECTOR, "input[class='range-slider range-slider--primary']")


class ProgressBarLocators:
    START_STOP_BUTTON = (By.CSS_SELECTOR, "button[id='startStopButton']")
    PROGRESS_BAR_LINE = (By.CSS_SELECTOR, "div[id='progressBar']")


class TabsPageLocators:
    WHAT_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-what']")
    WHAT_TAB_TEXT = (By.CSS_SELECTOR, "div[id='demo-tabpane-what']")
    ORIGIN_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-origin']")
    ORIGIN_TAB_TEXT = (By.CSS_SELECTOR, "div[id='demo-tabpane-origin']")
    USE_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-use']")
    USE_TAB_TEXT = (By.CSS_SELECTOR, "div[id='demo-tabpane-use']")
    MORE_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-more']")
    MORE_TAB_TEXT = (By.CSS_SELECTOR, "div[id='demo-tabpane-more']")


class ToolTipsPageLocators:
    HOVER_ME_TO_SEE_BUTTON = (By.CSS_SELECTOR, "button[id='toolTipButton']")
    TOOLTIP_BUTTON = (By.CSS_SELECTOR, "button[aria-describedby='buttonToolTip']")

    HOVER_ME_TO_SEE_INPUT = (By.CSS_SELECTOR, "input[id='toolTipTextField']")
    TOOLTIP_INPUT = (By.CSS_SELECTOR, "input[aria-describedby='textFieldToolTip']")

    CONTRARY_LINK = (By.XPATH, "//*[.='Contrary']")
    TOOLTIP_CONTRARY = (By.CSS_SELECTOR, "a[aria-describedby='contraryTexToolTip']")

    SECTION_LINK = (By.XPATH, "//*[.='1.10.32']")
    TOOLTIP_SECTION = (By.CSS_SELECTOR, "a[aria-describedby='sectionToolTip']")
    TOOLTIP_TEXT = (By.CSS_SELECTOR, "div[class='tooltip-inner']")


class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, "ul[id='nav'] li a")


class SelectMenuPageLocators:
    SELECT_OPTION = (By.CSS_SELECTOR, "div[id='withOptGroup']")
    SELECT_OPTION_INPUT = (By.CSS_SELECTOR, "input[id='react-select-2-input']")

    SELECT_ONE = (By.CSS_SELECTOR, "div[id='selectOne']")
    SELECT_ONE_INPUT = (By.CSS_SELECTOR, "input[id='react-select-3-input']")

    OLD_STYLE_SELECT = (By.CSS_SELECTOR, "select[id='oldSelectMenu']")

    MULTI_SELECT_INPUT = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    MULTI_VALUE_SINGLE_DELETE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue'] svg")

    STANDARD_MULTI_SELECT = (By.CSS_SELECTOR, "select[id='cars']")

