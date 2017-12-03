from selenium import webdriver
import time


def main():
    browser = webdriver.Firefox()
    # Change this with your password
    password = 'password'
    print('Initializing restart loop...')
    running = True

    while running:
        try:
            # Login
            print('Entering login password...')
            # Change the website to your router address
            browser.get('https://192.168.1.254/cgi-bin/login.ha')

            login = browser.find_element_by_name('password')
            login.send_keys(password)
            continue_b = browser.find_element_by_name('Continue')
            continue_b.click()

            # Click restart button
            print('Restarting...')
            browser.get('http://192.168.1.254/cgi-bin/home.ha')

            restart = browser.find_element_by_name('Broadband')
            restart.click()

            time.sleep(30)
        except Exception as e:
            browser.quit()
            with open('error.log', 'w') as w:
                w.write(str(e))
            running = False


if __name__ == '__main__':
    main()
