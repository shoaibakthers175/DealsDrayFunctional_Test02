import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from pynput.keyboard import Key, Controller
import os


browser = 'edge'
url = 'https://demo.dealsdray.com/'
Usernames = 'prexo.mis@dealsdray.com'
passwords = 'prexo.mis@dealsdray.com'

def start_browser(browser_name):
    if browser_name == 'chrome':
        options = ChromeOptions()
        driver = webdriver.Chrome()
    elif browser_name == 'edge':
        options = EdgeOptions()
        driver = webdriver.Edge()
    elif browser_name == 'firefox':
        options = FirefoxOptions()
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    driver.maximize_window()
    return driver



def run_tests02():
    # starting the browser
    driver = start_browser(browser)
    # getting the url
    driver.get(url)
    # Wait for the page to load completely
    time.sleep(5)
    Username = driver.find_element(By.CLASS_NAME, "MuiOutlinedInput-input")
    Username.send_keys(Usernames)
    Password = driver.find_element(By.CLASS_NAME, "css-r71t31")
    Password.send_keys(passwords)
    Login = driver.find_element(By.CLASS_NAME, "css-1usxxvf")
    Login.click()
    time.sleep(5)

    # Checking the page is navigated to the home page or not
    act_title = 'Prexo'
    expected_title = driver.title
    if act_title == expected_title:
        print("Home page Opened")

    # Clicking on Order button
    order_button = driver.find_element(By.CLASS_NAME, "css-46up3a")
    order_button.click()

    # click on Order page
    orders = driver.find_element(By.CLASS_NAME, "css-1cl20sq")
    orders.click()
    time.sleep(5)

    # click on add bulk order
    Bulk_order = driver.find_element(By.CLASS_NAME, "css-vwfva9")
    Bulk_order.click()
    time.sleep(5)

    # Choose a file
    Choose_file = driver.find_element(By.CLASS_NAME, "MuiOutlinedInput-root")
    Choose_file.click()
    time.sleep(5)

    # Send the file path to the file input
    keyboard = Controller()
    keyboard.type("C:\\Users\\shoai\\Downloads\\demo-data.xlsx")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # Wait till file upload
    time.sleep(5)

    # Import the file
    import_button = driver.find_element(By.CLASS_NAME, "css-6aomwy")
    import_button.click()
    time.sleep(5)

    # Validate the file
    Validate_button = driver.find_element(By.CLASS_NAME, "css-6aomwy")
    Validate_button.click()
    time.sleep(5)

    # Switch to the alert
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(5)



    # Take a screenshot right after the validation process
    screenshots_dir = "./Screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    screenshot_path = os.path.join(screenshots_dir, "validate_page_screenshot.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved successfully at {screenshot_path}!")

    driver.quit()

if __name__ == "__main__":
    run_tests02()
