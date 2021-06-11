from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import json
from urllib.request import *
import sys
import time
import re
from mimetypes import guess_extension, guess_type
import time 


def main():
    download_path = os.getcwd() + "\\Downloads\images\\"

    pokemons = ['Pikachu','Squirtle','dfsjdsf9df78d8f8df8df89dfdfdddddddddddd','Charizard']

    path_driver_browser="D:\\projetos\\selenium_drivers\\chromedriver.exe"

    options = Options()
    #options.headless = True #Active mode headless
    driver=webdriver.Chrome(path_driver_browser, options=options)

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    downloaded_img_count = 0
    not_found_img_count = 0

    seq = 0

    for pokemon in pokemons:
        img_count = 0
        seq = seq + 1

        if seq > 20:
            driver.quit()
            driver = webdriver.Firefox(options=options)
            seq = 0     

        print('Searching ...', pokemon)
        url = "https://www.google.co.in/search?q=" + pokemon + " -digimon&source=lnms&tbm=isch&tbs=isz:m"
        driver.get(url)

        elemento = driver.find_elements_by_xpath('//div[contains(@class,"bRMDJf")]')    

        if elemento:
            elemento[0].click()
            time.sleep(3)
            img = driver.find_element_by_class_name("n3VNCb").get_attribute("src") 

            img_count += 1
            img_url = img
            
            if 'base64' in img_url:
                img_type = guess_extension(guess_type(img_url)[0])
            else:
                img_type = '.' + img_url.rsplit('.',1)[1]
                if '?' == img_type:
                    img_type = img_type.split('?')[0]
                    
            try:

                try:
                    req = Request(img_url)
                    print("Found! URL:{}".format(img_url))
                    raw_img = urlopen(req).read()
                    f = open(download_path + pokemon + img_type, "wb")
                    f.write(raw_img)
                    f.close
                    downloaded_img_count += 1
                except Exception as e:
                    print("Download failed: {}:{}".format(e, pokemon))
                finally:
                    print

            except Exception as e:
                print("Download failed: {}:{}".format(e, pokemon))

            print ("Total downloaded: {}/{}".format(downloaded_img_count, len(pokemons)))
        else:
            not_found_img_count += 1
            print("Word '{}' not found".format(pokemon))
            print("Total not founds: {}".format(not_found_img_count))

    print("Total not founds: {}".format(not_found_img_count))
    driver.quit()

if __name__ == "__main__":
	main()
