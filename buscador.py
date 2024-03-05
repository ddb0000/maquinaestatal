# scraper that gets data from the web and stores it in a file, using selenium to blaze through the pages and pandas to store the data in a csv file.
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import logging
