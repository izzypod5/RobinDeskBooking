from selenium import webdriver
from time import sleep
from secrets import username, password
from datetime import datetime


class RobinDeskBookingBot():
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path='C:/Users/Aletch/webdrivers/chromedriver.exe')

    def login(self):
        # get the login page to access
        self.driver.get('https://dashboard.robinpowered.com/ai-london/login')

        # pause for the initial page load for 2 second
        sleep(2)

        # input all necessary inputs for login
        email_in = self.driver.find_element_by_xpath('//*[@id="user"]')
        email_in.send_keys(username)

        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(password)

        # click the login button
        login_btn = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/section/form[2]/div[4]/input')
        login_btn.click()

    def book_desk(self):

        # get relevant date input and value to book on
        start_date_input = bot.driver.find_element_by_xpath(
            '//*[@id="content-container"]/div/ui-view/desks-search/div[1]/div[1]/desks-date-time/date-time-selector/calendar-dropdown/input')
        start_date_value = start_date_input.get_attribute('value')
        datetime_object = datetime.strptime(
            start_date_value, '%B %d, %Y')

        # if it is Monday/Saturday/Sunday can just book the current day
        if(datetime_object.weekday() == 0 or datetime_object.weekday() == 5 or datetime_object.weekday() == 6):
            # book current day
            self.select_desk()

        # if it is a day between monday and thursday we can also book the following day
        if(datetime_object.weekday() < 4):
            # increase days until sunday is reached
            datetime_object += datetime.timedelta(days=1)
            datetime_string = '{:%B %d, %Y}'.format(datetime_object)
            start_date_input.setAttribute('value', datetime_string)
            self.select_desk()

    def remove_popup(self):
        # time to get rid of that pesky got it popup
        got_it_popup = bot.driver.find_element_by_xpath(
            '//*[@id="content-container"]/div/workplace-introduction/div/div/button')
        got_it_popup.click()

    # selects my desk using xpath expressions
    def select_desk(self):
        desk_button = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[2]/workplace-people-search/div/div[5]/div[5]/div')
        desk_button.click()
        reserve_desk_btn = self.driver.find_element_by_xpath(
            '//*[@id="content-container"]/div/ui-view/desks-search/div[2]/div[1]/workplace-desks/div/div/div[4]/div[2]/div/div/div/div/div/div[2]/button')
        reserve_desk_btn.click()


# run the bot!!!
bot = RobinDeskBookingBot()
bot.login()
# allow for some time to login before disregarding the annoying popup
sleep(10)
bot.remove_popup()
# another pause to allow for display to render
sleep(5)
# now can remove popup and book desk
bot.book_desk()
