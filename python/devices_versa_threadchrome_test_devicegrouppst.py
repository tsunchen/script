# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#import selenium.webdriver.remote.webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import threading, os, time

import pyversa_preset as pyv

from selenium.webdriver.support.select import Select


#继承thread.Thread类
class LarrThread(threading.Thread):
    #初始化方法 对func, orgs, name参数进行初始化
    def __init__(self, func, args, name = ''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


# 关联模板的功能2019.6.28
def create_ini_args():
    ROOT = '..\\Devices'
    ini_suite = []
    dirs = os.listdir(ROOT)
    print (dirs)
    for d in dirs:
        if d.startswith('config_devices_test'):
            #print (d)
            import configparser
            cf = configparser.ConfigParser()
            pathd = ".\\" + ROOT + "\\" + d
            #print(pathd)
            cf.read(pathd)
            ini_args = ""
            organization = cf.get("Basic", "organization")
            ini_args += organization + "~"
            name = cf.get("Basic", "Name")
            ini_args += name + "~"
            serialnumber = cf.get("Basic", "serialnumber")
            ini_args += serialnumber + "~"
            devicegroup = cf.get("Basic", "devicegroup")
            ini_args += devicegroup + "~"
            devicegrouppst = cf.get("Basic", "devicegrouppst")
            ini_args += devicegrouppst + "~"
            latitude = cf.get("LocationInformation", "latitude")
            ini_args += latitude + "~"
            longitude = cf.get("LocationInformation", "longitude")
            ini_args += longitude + "~"
            city = cf.get("LocationInformation", "city")
            ini_args += city + "~"
            country = cf.get("LocationInformation", "country")
            ini_args += country + "~"
            ini_suite.append(ini_args)
    return ini_suite


#
def super_player(keystr, times):
    for i in range(times):
        # 获取驱动
        path = "E:\\ProgramData\\Anaconda3\\chromedriver.exe"
        driver = webdriver.Chrome(path)
        #driver = selenium.webdriver.remote.webdriver.WebDriver(command_executor="http://192.168.1.51:5555/wd/hub", desired_capabilities=DesiredCapabilities.CHROME)
        print('start playing: %s ---- %s' % (keystr, time.ctime()))
        #
        login_versa(driver)
        # 验证登陆元素
        # login_status > ul > li:nth-child(1) > a:nth-child(1)
        # login_status > ul > li:nth-child(1) > a:nth-child(1) > strong
        user_name_element = driver.find_element_by_css_selector("#top-nav > div > div.top-bar.span12 > div.pull-right > div > div > ul > li.dropdown > a")
        print(user_name_element.text)
        name = user_name_element.text
        if u"shct ( shct )" == name:
            print("login pass")
        else:
            print("login of non-official")
        #
        dlydevices_act(driver, keystr)
        '''
        path = "E:\\ProgramData\\Anaconda3\\chromedriver.exe"
        driver = webdriver.Chrome(path)
        driver.get('https://www.baidu.com/')
        driver.find_element_by_id('kw').send_keys(keystr)
        driver.find_element_by_id('su').click()
        time.sleep(2)
        driver.quit()
        '''


def login_versa(driver):
    # 跳转网页
    driver.get(pyv.versa_https_url)
    print(driver.title)

    driver.maximize_window()

    # 睡眠时间
    driver.implicitly_wait(4)

    # 登录框
    ##login_ele = driver.find_element_by_css_selector("#login-wechat > div.userPassLogin.back_account > a")
    # 触发点击事件
    ##ActionChains(driver).click(login_ele).perform()

    # 查找输入框，输入帐号密码，输入框提前清理
    try:
        logpassword = WebDriverWait(driver, 4, 0.1).until(EC.presence_of_element_located((By.ID, "inputPassword")))
        logpassword.clear()
        logpassword.send_keys(pyv.versa_https_passtest)
        print("password资源加载成功")
    except:
        print("password资源加载失败，发送告警邮件或短信")
    finally:
        print("无论是否加载成功，都将响应用于password资源清理")

    try:
        # logform-username
        logusername = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, "inputEmail")))
        logusername.clear()
        logusername.send_keys(pyv.versa_https_usertest)
        print("username资源加载成功")
    except:
        print("username资源加载失败，发送告警邮件或短信")
    finally:
        print("无论是否加载成功，都将响应用于username资源清理")

    # 查找登陆按钮并点击
    button = driver.find_element_by_css_selector("body > div > div > div > section > div > form > div.control-group.margin-b > div > button")
    button.click()
    #
    driver.implicitly_wait(60)
    #



#
def dlydevices_act(driver, keystr):
    print(driver.find_elements_by_css_selector('.ui-menu.ui-widget.ui-widget-content.ui-autocomplete.ui-front'))
    elem = driver.find_elements_by_css_selector('.ui-menu.ui-widget.ui-widget-content.ui-autocomplete.ui-front')
    for el in elem:
        print(type(el))
    print(keystr)
    device_org, device_nm, device_sn, device_grp, device_grppst, device_lat, device_lng, device_cty, device_ctry, device_etc = keystr.split("~")
    print (device_org, device_nm, device_sn, device_grp, device_grppst, device_lat, device_lng, device_cty, device_ctry, device_etc)
    #
    workflows_xpath = '//*[@id="menuContainer"]/li[3]/a'
    WebDriverWait(driver, 60, 0.1).until(EC.presence_of_element_located((By.XPATH, workflows_xpath)))
    # 点选 Workflows
    workflows_ele = driver.find_element_by_xpath('//*[@id="menuContainer"]/li[3]/a')
    workflows_ele.click()
    # 修改睡眠等待时延 2019.6.26
    # 点选 Devices ,#left-nav-sdwan > li:nth-child(2) > a, #left-nav-sdwan > li:nth-child(2) > a > span
    # #left-nav-templates > li:nth-child(1) > a > span
    #
    sleep(2) # selenium.common.exceptions.ElementNotVisibleException: Message: element not interactable
    # #left-nav-devices > li > a > span
    driver.find_element_by_css_selector("#left-nav-sdwan > li:nth-child(3) > a > span").click()
    left_nav_sdwan = '#left-nav-sdwan > li:nth-child(3) > a > span'
    # 修改睡眠等待时延 2019.6.26
    # #left-nav-devices > li > a > span
    left_nav_devices = '#left-nav-devices > li > a > span'
    WebDriverWait(driver, 60, 0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR, left_nav_devices)))
    driver.find_element_by_css_selector(left_nav_devices).click()
    # 进入 create devices 界面, 修改睡眠等待时延 2019.6.26
    create_onboard_device = '#CREATE_onboard-device'
    WebDriverWait(driver, 60, 0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR, create_onboard_device)))
    driver.find_element_by_css_selector(create_onboard_device).click()
    # 
    # driver.implicitly_wait(3)
    # 输入 用户组，下拉框仍需用户实际操作时再点击激活JS代码
    #
    # 修改睡眠等待时延 2019.6.24
    WebDriverWait(driver, 60, 0.1).until(EC.presence_of_element_located((By.ID, pyv.versa_organization_ul_elementid)))
    #
    # Organization 自动复选後再选择
    # 2019.6.6 升级 下拉框自动激活JS代码 
    driver.find_element_by_css_selector("#tab-1 > div:nth-child(2) > div:nth-child(3) > div > span").click()
    print(pyv.versa_organization_ul_elementid)
    # ui-menu ui-widget ui-widget-content ui-autocomplete ui-front
    organization_ul = organization_ul = driver.find_element_by_id(pyv.versa_organization_ul_elementid)
    organization_lis = organization_ul.find_elements_by_xpath('li')
    #
    print("Device Basic Organizations : ", len(organization_lis))
    for i in range(len(organization_lis)):
        print("  `-", organization_lis[i].text)
    #
    # 选定某项租户
    device_organization = device_org # cf.get("Basic", "organization")
    for j in range(len(organization_lis)):
        li_n = "li:nth-child(" + str(j+1) + ")"
        print(li_n)
        the_index_organization_lis = organization_ul.find_element_by_css_selector(li_n)
        print(the_index_organization_lis.text)
        if (device_organization == the_index_organization_lis.text):
            the_index_organization_lis.click() #针对Organization的动态定位，获取所有租户组并根据本地ini配置文件的setting，判别後选定
    #
    # Device Groups 在organization选取後出现可选下拉框
    # 修改睡眠等待时延 2019.6.26
    WebDriverWait(driver, 60, 0.1).until(EC.presence_of_element_located((By.ID, pyv.versa_devicegroup_ul_elementid)))
    #
    driver.find_element_by_css_selector("#tab-1 > div:nth-child(3) > div:nth-child(3) > div > span").click()
    print(pyv.versa_devicegroup_ul_elementid)
    devicegroup_ul = driver.find_element_by_id(pyv.versa_devicegroup_ul_elementid)
    devicegroup_lis = devicegroup_ul.find_elements_by_xpath('li')
    #
    len_devicegroup_lis = len(devicegroup_lis)
    print("Device Basic Groups : ", len_devicegroup_lis)
    for i in range(len_devicegroup_lis):
        print("  `--", devicegroup_lis[i].text)
    #
    # 选定某项租户de设备组
    device_group = device_grp # cf.get("Basic", "devicegroup")
    len_devicegroup_lis = len(devicegroup_lis)
    j_cnt = 0
    for j in range(len_devicegroup_lis):
        li_n = "li:nth-child(" + str(j+1) + ")"
        print (li_n)
        the_index_devicegroup_lis = devicegroup_ul.find_element_by_css_selector(li_n)
        print(the_index_devicegroup_lis)
        print(the_index_devicegroup_lis.text)
        if (device_group == the_index_devicegroup_lis.text):
            the_index_devicegroup_lis.click() #针对Organization的动态定位，获取所有租户组de设备组并根据本地ini配置文件的setting，判别後选定
        else:
            j_cnt += 1
    j_cnt += 1
    if (j_cnt == len_devicegroup_lis):
        print("hit the existed device group")
        #
        device_name = device_nm # cf.get("Basic", "name")
        driver.find_element_by_id("onboard-new-organisation-form-name").send_keys(device_name)
        #
        device_snum = device_sn # cf.get("Basic", "serialnumber")
        driver.find_element_by_id("onboard-new-organisation-form-serialNumber").send_keys(device_snum)
        #
        sleep(2)
        # 按下一步continue，跳转Location Information
        driver.find_element_by_css_selector("#form_continue_add-device").click()
        #
        sleep(2)
        # latitude
        device_LI_latitude = device_lat # cf.get("LocationInformation", "latitude")
        driver.find_element_by_css_selector("#onboard-new-organisation-form-latitude").send_keys(device_LI_latitude)
        # longitude
        device_LI_longitude = device_lng # cf.get("LocationInformation", "longitude")
        driver.find_element_by_css_selector("#onboard-new-organisation-form-longitude").send_keys(device_LI_longitude)
        # city
        device_city = device_cty # cf.get("LocationInformation", "city")
        driver.find_element_by_css_selector("#onboard-new-organisation-form-city").send_keys(device_city)
        # country
        device_country = device_ctry # cf.get("LocationInformation", "country")
        driver.find_element_by_css_selector("#onboard-new-organisation-form-country").send_keys(device_country)
        #
        sleep(2)
        # 按下一步continue，跳转Bind_Data
        ##driver.find_element_by_css_selector("#form_continue_add-device").click()
        ##sidePopupFor-workflow-onboard-device > div > div.wizard-body.clearfix > div > div > div > div > div.wrapper > div > div > ul > li.bind_data.active > a
        driver.find_element_by_css_selector('#sidePopupFor-workflow-onboard-device > div > div.wizard-body.clearfix > div > div > div > div > div.wrapper > div > div > ul > li.bind_data > a').click()
        #
        sleep(30)
        #
    else:
        print("to create device group")
        driver.find_element_by_id("onboard-new-organisation-form-name").send_keys("toCreateDeviceGroupFirst")
        driver.find_element_by_css_selector("#sidePopupFor-workflow-onboard-device > div > div.wizard-body.clearfix > div > div > div > div > div.wrapper > div > div > ul > li.active > a").click()
        driver.find_element_by_css_selector("#tab-1 > div:nth-child(3) > div:nth-child(3) > div > button").click()
        sleep(2)
        crtdevicegroup(driver, keystr)
    # cancel the form
    driver.find_element_by_id("form_cancel_add-device").click()
    #
    # save the form
    #driver.find_element_by_id("form_ok_add-device").click()
    #
    # logout
    #top-nav > div > div.top-bar.span12 > div.pull-right > div > div > ul > li.dropdown.open > a
    #top-nav > div > div.top-bar.span12 > div.pull-right > div > div > ul > li.dropdown > a
    driver.find_element_by_css_selector("#top-nav > div > div.top-bar.span12 > div.pull-right > div > div > ul > li.dropdown > a").click()
    sleep(2)
    driver.find_element_by_id("user-logout").click()
    #
    #driver.quit()
    #
    #("#top-nav > div > div.top-bar.span12 > div.pull-right > div > div > ul > li.dropdown.open > ul")
    '''
    return
    '''

#
def crtdevicegroup(driver, keystr):
    #
    print(keystr)
    device_org, device_nm, device_sn, device_grp, device_grppst, device_lat, device_lng, device_cty, device_ctry, device_etc = keystr.split("~")
    print (device_org, device_nm, device_sn, device_grp, device_grppst, device_lat, device_lng, device_cty, device_ctry, device_etc)
    #
    # devicegroupobjname
    devicegroupobjectname = device_grp
    driver.find_element_by_id("device-group-object-name").send_keys(devicegroupobjectname)
    # deviceorg
    device_organization = device_org
    Select(driver.find_element_by_id('device-group-object-organization')).select_by_value(device_organization)
    sleep(10) # WebDriverWait(driver, 60, 0.1).until(EC.presence_of_element_located((By.ID, pyv.versa_devicegrouppst_ul_elementid)))
    # devicegrouppoststagingtemplate
    devicegrouppst = device_grppst
    driver.find_element_by_css_selector('#sidePopupFor-device-group-object > div > div > div.wizard-body.clearfix > div > div > div:nth-child(6) > div:nth-child(2) > div > span').click()
    #ui-menu ui-widget ui-widget-content ui-autocomplete ui-front
    #                 driver.find_element_by_css_selector('.ui-menu.ui-widget.ui-widget-content.ui-autocomplete.ui-front')
    devicegrouppst_ul = driver.find_element_by_id(pyv.versa_devicegrouppst_ul_elementid)
    ##driver.find_element_by_css_selector('.ui-menu.ui-widget.ui-widget-content.ui-autocomplete.ui-front') #driver.find_element_by_css_selector('ui-menu ui-widget ui-widget-content ui-autocomplete ui-front')
    devicegrouppst_lis = devicegrouppst_ul.find_elements_by_xpath('li')
    #
    print("Device Group Post Staging Templates : ", len(devicegrouppst_lis))
    for i in range(len(devicegrouppst_lis)):
        print("  `-", devicegrouppst_lis[i].text)
    # 选定设备de属组
    devicegrouppoststagingtemplate = device_grppst
    for j in range(len(devicegrouppst_lis)):
        li_n = "li:nth-child(" + str(j+1) + ")"
        print(li_n)
        the_index_devicegrouppst_lis = devicegrouppst_ul.find_element_by_css_selector(li_n)
        print(the_index_devicegrouppst_lis.text)
        if (devicegrouppoststagingtemplate == the_index_devicegrouppst_lis.text):
            the_index_devicegrouppst_lis.click() #针对Organization的动态定位，获取所有租户组并根据本地ini配置文件的setting，判别後选定
    #
    #
    print(driver.find_elements_by_css_selector('.ui-menu.ui-widget.ui-widget-content.ui-autocomplete.ui-front'))
    elem = driver.find_elements_by_css_selector('.ui-menu.ui-widget.ui-widget-content.ui-autocomplete.ui-front')
    for el in elem:
        print(type(el))
    #
    sleep(2)
    # save the device group
    driver.find_element_by_css_selector('#sidePopupFor-device-group-object > div > div > div.popup-footer.clearfix > div > button.btn-green.saveForm').click()
    #  #sidePopupFor-device-group-object > div > div > div.popup-footer.clearfix > div > button.btn-black
    #  cancel the device group
    # #driver.find_element_by_css_selector('#sidePopupFor-device-group-object > div > div > div.popup-footer.clearfix > div > button.btn-black').click()


threads=[]
if __name__ == '__main__':
    ini = create_ini_args()
    print(ini)
    ini_constv = [1 for i in range(len(ini))]
    inival = dict(zip(ini, ini_constv))
    print(inival)

    #创建线程
    for keystr, times in inival.items():
        t = LarrThread(super_player, (keystr, times), super_player.__name__)
        threads.append(t)

    files = range(len(inival))
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

    delay_seconds = len(inival) * 10
    sleep(delay_seconds)
    print('all finish ---- %s' % time.ctime())

    '''
    # 获取驱动
    path = "E:\\ProgramData\\Anaconda3\\chromedriver.exe"
    driver = webdriver.Chrome(path)
    #driver = selenium.webdriver.remote.webdriver.WebDriver(command_executor="http://192.168.1.51:5555/wd/hub", desired_capabilities=DesiredCapabilities.CHROME)
    login_versa(driver)
    # 验证登陆元素
    # login_status > ul > li:nth-child(1) > a:nth-child(1)
    # login_status > ul > li:nth-child(1) > a:nth-child(1) > strong
    user_name_element = driver.find_element_by_css_selector("#top-nav > div > div.top-bar.span12 > div.pull-right > div > div > ul > li.dropdown > a")
    print(user_name_element.text)
    name = user_name_element.text
    if u"shct ( shct )" == name:
        print("login pass")
    else:
        print("login fail")
    dlydevices(driver)
    '''
    #driver.quit()









