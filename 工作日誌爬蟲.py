from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cv2
from PIL import Image
from io import BytesIO
import pytesseract
import pyautogui
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
import tkinter as tk





# 配置WebDriver路径
driver_path = Service("E:\\TA\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_path)

base_url = "https://web085004.adm.ncyu.edu.tw/NewSite/Login.aspx?Language=zh-TW"
driver.get(base_url)

wait = WebDriverWait(driver, 10)

def login():
    account_input = driver.find_element(By.ID, 'TbxAccountId')
    account_input.clear()
    #輸入你的帳號
    account_input.send_keys('')

    password_input = driver.find_element(By.ID, 'TbxPassword')

    password_input.clear()
    #輸入你的密碼
    password_input.send_keys('')

    
    captcha_image = wait.until(EC.presence_of_element_located((By.ID, 'Image1')))
    location = captcha_image.location
    size = captcha_image.size


    left = location['x'] 
    top = location['y']
    right = location['x'] + size['width'] 
    bottom = location['y'] + size['height'] 


    screenshot = driver.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))


    captcha_screenshot = screenshot.crop((left, top, right, bottom))


    captcha_screenshot.save('E:\\TA\\captcha.png')

    image =cv2.imread('E:\\TA\\captcha.png', cv2.IMREAD_GRAYSCALE)
    ret, img = cv2.threshold(image, 175, 255, cv2.THRESH_BINARY_INV)

    result = pytesseract.image_to_string(img)
    print(result.replace(" ", ""))
    captcha_input = driver.find_element(By.ID, 'TbxCaptcha')
    captcha_input.send_keys(result.replace(" ", ""))


def main_2():
    menu = wait.until(EC.element_to_be_clickable((By.ID, 'BtnMenu')))
    menu.click()
    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, '工作日誌維護(學生)')))
    link.click()
    frame_element = driver.find_element(By.ID, "application-frame-main")

    driver.switch_to.frame(frame_element)
    
def main(m,d,bt,et,w):
    
    time.sleep(2)
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "newBtn")))

    button.click()



    bugetno = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "bugetno_idno"))
    )
    #計畫編號
    bugetno.send_keys("")

    emp = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'emp_id'))
    )
    #承辦人
    emp.send_keys("") 


    month_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "month"))
    )
    
    month = Select(month_element)
    month.select_by_value(m)
    time.sleep(2)
    day_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//select[@id='date']"))
    )
    day = Select(day_element)
    day.select_by_value(d)

    b_time_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//select[@id='b_time']"))
    )
    b_time = Select(b_time_element)
    b_time.select_by_value(bt)

    e_time_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//select[@id='e_time']"))
    )
    e_time = Select(e_time_element)
    e_time.select_by_value(et)

    work_content = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'work_content'))
    )
    work_content.send_keys(w)
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary' and @data-dismiss='modal']"))
    )
    button.click()


def run_subprogram():
    try:
        print('START')
        main_2()
        m = m1.get()
        d = int(d1.get())
        days=int(day.get())
        bt = int(bt1.get())
        et = int(et1.get())
        w = w1.get()
        temp=days//5
        days=days+temp
        for i in range(days):
            if i%5==0 and i!=0:
                continue
            else:
                str_day="{:02d}".format(d+i)
                "{:02d}".format(bt+i)
                print(str_day)
                main(m,str_day,"{:02d}".format(bt),"{:02d}".format(bt+4),w)
                main(m,str_day,"{:02d}".format(et),"{:02d}".format(et+4),w)
        app.quit()
        
    except ValueError:
        print("請輸入一個有效的數值")
def cflash():
    driver.refresh()
    login()

app = tk.Tk()
app.title("Checkbutton Example")
app.geometry("500x500")

m1 = tk.Label(app, text="請輸入幾月(01~12):")
m1.pack(pady=5)
m1 = tk.Entry(app)
m1.pack(pady=5)

d1 = tk.Label(app, text="請輸入開始的日期(01~30):")
d1.pack(pady=5)
d1 = tk.Entry(app)
d1.pack(pady=5)

day = tk.Label(app, text="請輸入總共幾天:")
day.pack(pady=5)
day = tk.Entry(app)
day.pack(pady=5)

bt1 = tk.Label(app, text="請輸入第一個開始的時段:")
bt1.pack(pady=5)
bt1 = tk.Entry(app)
bt1.pack(pady=5)

et1 = tk.Label(app, text="請輸入第二個開始的時段:")
et1.pack(pady=5)
et1 = tk.Entry(app)
et1.pack(pady=5)
w1 = tk.Label(app, text="請輸入w:")
w1.pack(pady=5)
w1 = tk.Entry(app)
w1.pack(pady=5)
error_button = tk.Button(app, text="開始驗證", command=cflash)
error_button.pack(pady=10)
start_button = tk.Button(app, text="開始填寫", command=run_subprogram)
start_button.pack(pady=10)


app.mainloop()





driver.quit()
