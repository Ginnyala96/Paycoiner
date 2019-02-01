from behave import *
from selenium import webdriver

use_step_matcher('re')


@given('I am on the hompage')
def step_impl(context):
    browser = webdriver.Chrome('/Users/alicjazyla/Documents/chromedriver')
    browser.get('demo.paycoiner.com')