from time import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class InstaBot:
    def __init__(self,browser):
        self.followers = []
        self.followings = []
        if(browser == "firefox"):
            self.driver = webdriver.Firefox()
            self.driver.get("https://www.instagram.com/")    
            sleep(2)
        elif(browser == "chrome"):
            pass #TODO        

    def login(self,username,password):
        # element_user = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        element_user = self.driver.find_element_by_name("username")
        #element_password = WebDriverWait(self,self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        element_password = self.driver.find_element_by_name("password")
        element_user.send_keys(username)
        element_password.send_keys(password)
        button = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
        button.click()
        sleep(4)

    def go_profile(self):
        pic = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img")
        pic.click()
        profilebut = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div")
        profilebut.click()
        sleep(1)

    def scroll_down(self):
        command = """
        driver = document.querySelector(".isgrP");
        driver.scrollTo(0,driver.scrollHeight);
        var window_end = driver.scrollHeight;
        return window_end;
        """
        window_end = self.driver.execute_script(command)
        while(True):
            end = window_end
            sleep(1)
            window_end = self.driver.execute_script(command)
            if(end == window_end):
                break

    def get_followers(self):
        follower_but = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        follower_but.click()
        sleep(3)
        self.scroll_down()
        follower_elems = self.driver.find_elements(By.CLASS_NAME,"FPmhX.notranslate._0imsa")
        for e in follower_elems:
            self.followers.append(e.text)
        print(len(self.followers))
        close_but = self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div[1]/div/div[2]/button")
        close_but.click()

    def get_followings(self):
        following_but = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
        following_but.click()
        sleep(2)
        self.scroll_down()
        following_elems = self.driver.find_elements(By.CLASS_NAME,"FPmhX.notranslate._0imsa")
        for e in following_elems:
            self.followings.append(e.text)
        print(len(self.followings))

    def find_difference(self):
        users_dont_follow_u_back = []
        users_u_dont_follow = []
        for elem in self.followings:
            if not(elem in self.followers):
                users_dont_follow_u_back.append(elem)
        for elem in self.followers:
            if not(elem in self.followings):
                users_u_dont_follow.append(elem)
        return (users_dont_follow_u_back,users_u_dont_follow)
