from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
import time

langDict = {"python":"https://tio.run/#python3", "java":"https://tio.run/#java-jdk", "C++": "https://tio.run/#cpp-clang", "rust":"https://tio.run/#rust", "lua":"https://tio.run/#lua", "bash": "https://tio.run/#bash"}

def execStmt(lang, code):
    #Initialize driver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(langDict[lang])
    try:
      #Find input field
      input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"code\"]")))
      input.send_keys(code)
      #Find run and click run button
      runButton = driver.find_element_by_id("run-button")
      runButton.click()
      #Wait for code to finish running
      debug = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"debug\"]")))
      while(debug.get_attribute("value") == "" or debug.get_attribute("value") == None):
          time.sleep(1)
      #Get output value
      output = driver.find_element_by_xpath("//*[@id=\"output\"]")
      value = output.get_attribute("value") #Assign value first so driver can be closed
      #If there is no value, get the debug field instead
      if value == "" or value is None:
          debug = debug.get_attribute("value")
          driver.close()
          if(len(debug) < 2000):
              return debug
          else:
              return "Output over 2000 characters."
      driver.close()
      #Otherwise return the value
      if(len(value) < 2000):
          return value
      else:
          return "Output over 2000 characters."
    except Exception as e:
      #Close driver
      driver.close()
      #Catch exceptions
      return repr(e)

def getHelloWorld(lang):
    #Initialize driver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(langDict[lang])
    try:
      #Get hello world
      hwButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"lang-example\"]")))
      hwButton.click()
      time.sleep(1)
      code = driver.find_element_by_xpath("//*[@id=\"code\"]")
      codeText = code.get_attribute("value")
      driver.close()
      return codeText
    except Exception as e:
      driver.close()
      return repr(e)

def getLanguages():
    languages = []
    for lang in langDict:
        languages.append(lang)
    return languages
