from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 

class TwitterBot:
 def __init__(self, username, password):
   self.username = username
   self.password = password
   self.bot = webdriver.Firefox()
   
 def login(self):
   bot = self.bot
   # this is where u are going to put the url of the site that
   # you want to create the bot for 
   bot.get('https://twitter.com')
   time.sleep(6)
   email = bot.find_element_by_class_name('email-input')
   password = bot.find_element_by_name('session[password]')
   email.clear()
   password.clear()
   email.send_keys(self.username)
   password.send_keys(self.password)
   password.send_keys(Keys.RETURN)
   time.sleep(5)
 def like_tweet(self,hashtag):
  bot = self.bot
  bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
  time.sleep(3)
  # for i in range(1,3):
    # bot.execute_script('window.scrollTo(0,docudment.body.scrollHeight)')
    # time.sleep(3)
  tweets = bot.find_element_by_class_name('tweet')
  links = [elem.get_attribute('data-permalink-path') 
            for elem in tweets]
  for link in links:
    bot.get('https://twitter.com' + link)
    try:
        bot.find_element_by_class_name('HeartAnimation').click()
        time.sleep(10)
        
    except Exception as ex:
      time.sleep(60)
        
    
ed = TwitterBot('your username' , 'your password')  
ed.login()
time.sleep(5)
ed.like_tweet('webdevelopment')
