import pytest
from selenium import webdriver
from time import sleep
import os
import allure


if __name__ == '__main__':
    pytest.main(['-s', '-q', 'tests/test_login.py', '--alluredir', 'outFiles/reports/allure-results'])
    os.system(r"allure generate outFiles/reports/allure-results -o outFiles/reports/allure-result --clean")
