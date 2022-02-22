import pickle
import selenium.webdriver 
# Built-in/Generic Imports
from time import sleep
import logging
import sys
import json
from random import randint
import random
import time

# Library Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from selenium.webdriver.common.action_chains import ActionChains

logging.basicConfig(format='%(levelname)s [%(asctime)s] %(message)s', datefmt='%m/%d/%Y %r', level=logging.INFO)
logger = logging.getLogger()

user='adela.0elxt7'
passw='mIdAEEuA99rv'
proxy = "34.95.31.100:3128" 


cookies_file_path='E:/Marketing/Insta_BOT/Cookies/'+user+'.pkl'
cookies_websites='https://instagram.com'

comment_percentage=100
like_percentage=50
follow_percentage=100

posts_min=40
posts_max=100

wait_min = 4
wait_max = 5

Overall_wait_min = 2
Overall_wait_max = 60

hashtags =[

'smallbusiness',
'supportsmallbusiness',
'handmade',
'shoplocal',
'shopsmall',
'localbusiness',
'etsy',
'etsyshop',
'art',
'homedecor'

]

comment_list =[
u'Great!! '
u'Grow , Promote your profile with 3M Network -- DM @huntplaza',

u'Wonderful!! '
u'Grow , Promote your profile with 3M Network -- DM @huntplaza',

u'This is nice!! '
u'Grow , Promote your profile with 3M Network -- DM @huntplaza',

u'Wonderful!! '
u'Grow , Promote your profile with 3M Network -- DM @huntplaza',

u'Good one!! '
u'Grow , Promote your profile with 3M Network -- DM @huntplaza',

u'This is cool!! '
u'Grow , Promote your profile reach with 3M Network -- DM @huntplaza',

u'Nice!! '
u'Grow , Promote your profile reach with 3M Network -- DM @huntplaza',

u'You deserve more views!! '
u'Grow , Promote your profile reach with 3M Network -- DM @huntplaza',

u'You deserve more followers!! '
u'Grow , Promote your profile with 3M Network -- DM @huntplaza',

u'You deserve more likes!! '
u'Grow , Promote your profile with 3M Network -- DM @huntplaza'
]


def send_keys_delay_random(keys,element):
    for key in keys:
        actions = ActionChains(driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys(key)
        logger.info(key)
        actions.perform()
        sleep(random.uniform(0.1,0.3)) 
                  

def start_driver():
    
    options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--proxy-server=%s' % proxy)
    
    driver = webdriver.Chrome(executable_path=CM().install(), options=options)
    driver.get("https://freegeoip.app/json")
    sleep(10)
    pre = driver.find_element_by_tag_name("pre").text
    logger.info("---------> Connected " + pre)
    
    return driver

def login():
    try:
        driver.get(cookies_websites)
        sleep(randint(wait_min, wait_max))
        cookies = pickle.load(open(cookies_file_path, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        logger.info("---------> Cookie loaded")
        driver.refresh()
        sleep(randint(wait_min, wait_max))
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//button[text()='Not Now']").click()


    except:
        logger.info("---------> Cookies Not loaded")
        logger.info("---------> Try Login Again")
        login_to_instagram()
                
 
def save_cookies():
    try:
        pickle.dump( driver.get_cookies() , open(cookies_file_path,"wb"))
        logger.info('---------> Cookies saved')

    except:
        logger.info("---------> cookies Not saved")


def login_to_instagram():

    
    driver.implicitly_wait(30)
    username = driver.find_element_by_name('username')

    send_keys_delay_random(user,username)
    sleep(randint(wait_min, wait_max))


    driver.implicitly_wait(30)
    password = driver.find_element_by_name('password')
    send_keys_delay_random(passw,password)
    sleep(randint(wait_min, wait_max))

  
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()
    driver.implicitly_wait(30)
    try:
        if driver.find_element_by_xpath("//*[@id='slfErrorAlert']"):
            driver.close()
            sys.exit('Error: Login information is incorrect')
        else:
            pass
    except:
        pass

    driver.implicitly_wait(30)
    logger.info('---------> Logged in to ' + user)

    # Save your login info? Not now
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
    sleep(randint(wait_min, wait_max))

    # Turn on notifications? Not now
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
    sleep(randint(wait_min, wait_max))
    save_cookies()


def automate_instagram():
    # Keep track of how many you like and comment
    likes = 0
    comments = 0
    try:
        
        follow = (randint(0, 100) <= follow_percentage)
        sleep(10)

        if(follow):
            logger.info("--------->")
            logger.info("---------> trying to follow ")
            driver.implicitly_wait(30)
            driver.find_elements_by_xpath("//div[@class='_7UhW9  PIoXz         qyrsm           uL8Hv         ']")[1].click()
            sleep(randint(wait_min, wait_max))
            logger.info("---------> Followed ")
        else:
            logger.info("--------->")
            logger.info("---------> Skip Follow ")


    except:
        logger.info("---------> Unable to follow ")
        pass
            
    rand_hashtag = randint(0,len(hashtags)-1)
    logger.info(rand_hashtag)
    for hashtag in hashtags:
        driver.implicitly_wait(30)
        driver.get(f'https://www.instagram.com/explore/tags/{hashtags[rand_hashtag]}/')
        logger.info("--------->")
        logger.info(f'---------> Exploring #{hashtags[rand_hashtag]}')
        sleep(randint(wait_min, wait_max))

        # Click first thumbnail to open
        driver.implicitly_wait(30)
        first_thumbnail = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]")
        first_thumbnail.click()
        sleep(randint(wait_min, wait_max))

        # Go through x number of photos per hashtag
        for post in range(posts_min, posts_max):
            sleep(randint(Overall_wait_min, Overall_wait_max))
            
            logger.info("---------> Opening Post")
            get_url = driver.current_url
            logger.info("---------> " +get_url)
            

            logger.info("---------> Checking Already Comments from Leech")
            driver.implicitly_wait(30)
            leech_comments = driver.find_elements_by_xpath("//*[contains(text(),'send it') or contains(text(),'send pic') or contains(text(),'DM us') or contains(text(),'DM iT') or contains(text(),'DM IT') or contains(text(),'DM it') or contains(text(),'Promote it' ) and //a[contains(text(),'@')]]")
            if not len(leech_comments) > 1:
                logger.info("--------->")
                logger.info("---------> No Leech")
            
                #like
                try:
                    liking = (randint(0, 100) <= like_percentage)
                    do_i_like = liking
                    if do_i_like:
                        logger.info("--------->")
                        logger.info("---------> Going to Like")
                        driver.implicitly_wait(30)
                        likeButton = driver.find_elements_by_xpath("//*[contains(@class, 'fr66n')]/button/div/*[*[local-name()='svg']/@aria-label='Like']/*")
                        if len(likeButton) > 0:
                            likeButton[0].click()
                            sleep(randint(wait_min, wait_max))
                            logger.info("--------->")                       
                        else:
                            logger.info("--------->")
                            
                        logger.info("---------> Liked")
                        likes += 1
                    else:
                        logger.info("--------->")
                        logger.info("---------> Skipping Like")         
                    sleep(randint(wait_min, wait_max))
                except Exception:
                    logger.info("--------->")
                    logger.info("---------> Like Failed , Going to Next") 
                    pass    

                # Comment
                try:
                    driver.implicitly_wait(30)
                    driver.find_element_by_xpath("//form").click()
                    sleep(randint(wait_min, wait_max))
                    commenting = (randint(0, 100) <= comment_percentage)
                    do_i_comment =  commenting
                    if do_i_comment:
                        logger.info("--------->")
                        logger.info("---------> Going to Comment")
                        driver.implicitly_wait(30)
                        sleep(randint(wait_min, wait_max))
                        comment_area = driver.find_elements_by_xpath("//textarea[@Placeholder = 'Add a comment…']")
                        comment_button = driver.find_elements_by_xpath("//button[text()='Post']")
                        if len(comment_area) > 0:

                            rand_comment_index = randint(0, len(comment_list))
                            send_keys_delay_random(comment_list[rand_comment_index],comment_area[0])
                            # (
                            # ActionChains(driver)
                            # .move_to_element(comment_area[0])
                            # .click()
                            # .send_keys(comment_list[rand_comment_index])
                            # .pause(3)
                            # .move_to_element(comment_button[0])
                            # .click()
                            # .perform()
                            # )   
                            comments += 1
                            sleep(randint(wait_min, wait_max))
                        else:
                            logger.info("--------->")
                        logger.info("--------->")
                        logger.info("---------> Commented")

                    else:
                        logger.info("--------->")
                        logger.info("---------> Skipping Comment")    
                except Exception:
                    logger.info("--------->")
                    logger.info("---------> Comment Failed , Going to Next") 
                    pass
            else:
                logger.info("--------->")
                logger.info("---------> Skipping Leech")            
       

            # Go to next post
            
            try:
                driver.implicitly_wait(30)
                sleep(randint(wait_min, wait_max))
                logger.info("--------->")
                logger.info('---------> Getting next post')
                nextPost = driver.find_element_by_xpath("//*[@aria-label= 'Next']")
                (
                ActionChains(driver)
                .move_to_element(nextPost)
                .click()
                .perform()
                )   
                sleep(randint(wait_min, wait_max))
                
            except:
                logger.info("--------->")
                logger.info('----------> Unable to Click Next Post')

        sleep(randint(wait_min, wait_max))


    logger.info("==============================")   
    logger.info(f'---------> Liked {likes} posts')
    logger.info(f'---------> Commented on {comments} posts')

    # Close driver when done
    logger.info('---------> Closing chrome driver...')
    #driver.close()


driver=start_driver()
login()
automate_instagram()













