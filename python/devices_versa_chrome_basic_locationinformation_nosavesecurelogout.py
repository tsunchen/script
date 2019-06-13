# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#import selenium.webdriver.remote.webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#针对Organization的动态定位，获取所有租户组并根据本地ini配置文件的setting，判别後选定
#针对Organization的动态定位，获取所有租户组de设备组并根据本地ini配置文件的setting，判别後选定
#暂时不保存安全退出後关闭驱动（20190613）

#配置源文件（20190612)
import pyversa_preset as pyv


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
        logpassword.send_keys(pyv.versa_https_password)
        print("password资源加载成功")
    except:
        print("password资源加载失败，发送告警邮件或短信")
    finally:
        print("无论是否加载成功，都将响应用于password资源清理")

    try:
        # logform-username
        logusername = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, "inputEmail")))
        logusername.clear()
        logusername.send_keys(pyv.versa_https_username)
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

    

'''
    # 处理最上层弹框 body > div:nth-child(20) > a:nth-child(2)
    driver.find_element_by_css_selector("body > div:nth-child(20) > a:nth-child(2)").click()

    # hover事件#login_status > ul > li.hovercur > a
    # #login_status > ul > li.hovercur > a
    community_element = driver.find_element_by_link_text("社区")
    ActionChains(driver).move_to_element(community_element).perform()
    sleep(4)
'''


def dlydevices(driver):
    # deploy devices
    # monitor_ele = driver.find_element_by_xpath('//*[@id="menuContainer"]/li[1]/a')
    # monitor_ele.click()
    #administration_ele = driver.find_element_by_xpath('//*[@id="menuContainer"]/li[5]/a')
    #administration_ele.click()
    #driver.implicitly_wait(3)
    sleep(2)
    # 点选 Workflows
    workflows_ele = driver.find_element_by_xpath('//*[@id="menuContainer"]/li[3]/a')
    workflows_ele.click()
    driver.implicitly_wait(3)
    #
    # 点选 Devices ,#left-nav-sdwan > li:nth-child(2) > a, #left-nav-sdwan > li:nth-child(2) > a > span
    # #left-nav-templates > li:nth-child(1) > a > span
    sleep(2)
    # #left-nav-devices > li > a > span
    driver.find_element_by_css_selector("#left-nav-sdwan > li:nth-child(3) > a > span").click()
    #
    sleep(2)
    driver.find_element_by_css_selector("#left-nav-devices > li > a > span").click()
    #driver.find_element_by_css_selector("#left-nav-templates > li:nth-child(1) > a").click()
    # 进入 create devices 界面
    driver.find_element_by_css_selector("#CREATE_onboard-device").click()
    #
    driver.implicitly_wait(3)
    # 输入 用户组，下拉框仍需用户实际操作时再点击激活JS代码
    ##driver.find_element_by_id("onboard-new-organisation-form-orgName").send_keys("shct")
    ##from selenium.webdriver.common.by import By
    ##from selenium.webdriver.support.ui import WebDriverWait
    ##from selenium.webdriver.support import expected_conditions as EC
    ##driver.find_element_by_xpath('//*[@id="template-object-providerTenant"]')
    ##WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="template-object-providerTenant"]'))).send_keys('Your Value')
    ##print("placeholder_v", placeholder_v)
    #
    import configparser
    cf = configparser.ConfigParser()
    cf.read(pyv.versa_config_devices_test_file)
    #
    device_organization = cf.get("Basic", "organization")
    driver.find_element_by_id("onboard-new-organisation-form-orgName").send_keys(device_organization)
    sleep(2)
    # Organization 手工复选後再选择
    #device_group = cf.get("Basic", "devicegroup")
    #driver.find_element_by_id("onboard-new-organisation-form-deviceGroup").send_keys(device_group)
    # 2019.6.6 升级 下拉框自动激活JS代码 
    driver.find_element_by_css_selector("#tab-1 > div:nth-child(2) > div:nth-child(3) > div > span").click()
    organization_ul = driver.find_element_by_id(pyv.versa_organization_ul_elementid)
    organization_lis = organization_ul.find_elements_by_xpath('li')
    #
    print("Device Basic Organizations : ", len(organization_lis))
    for i in range(len(organization_lis)):
        print("  `-", organization_lis[i].text)
    #
    # 选定某项租户
    device_organization = cf.get("Basic", "organization")
    for j in range(len(organization_lis)):
        li_n = "li:nth-child(" + str(j+1) + ")"
        print (li_n)
        the_index_organization_lis = organization_ul.find_element_by_css_selector(li_n)
        print(the_index_organization_lis.text)
        if (device_organization == the_index_organization_lis.text):
            the_index_organization_lis.click() #针对Organization的动态定位，获取所有租户组并根据本地ini配置文件的setting，判别後选定
    #
    #Device Groups 在organization选取後出现可选下拉框
    sleep(2)
    #
    driver.find_element_by_css_selector("#tab-1 > div:nth-child(3) > div:nth-child(3) > div > span").click()
    devicegroup_ul = driver.find_element_by_id(pyv.versa_devicegroup_ul_elementid)
    devicegroup_lis = devicegroup_ul.find_elements_by_xpath('li')
    #
    print("Device Basic Groups : ", len(devicegroup_lis))
    for i in range(len(devicegroup_lis)):
        print("  `--", devicegroup_lis[i].text)
    #
    # 选定某项租户de设备组
    device_group = cf.get("Basic", "devicegroup")
    for j in range(len(devicegroup_lis)):
        li_n = "li:nth-child(" + str(j+1) + ")"
        print (li_n)
        the_index_devicegroup_lis = devicegroup_ul.find_element_by_css_selector(li_n)
        print(the_index_devicegroup_lis.text)
        if (device_group == the_index_devicegroup_lis.text):
            the_index_devicegroup_lis.click() #针对Organization的动态定位，获取所有租户组de设备组并根据本地ini配置文件的setting，判别後选定
    #
    device_name = cf.get("Basic", "name")
    driver.find_element_by_id("onboard-new-organisation-form-name").send_keys(device_name)
    #
    device_snum = cf.get("Basic", "serialnumber")
    driver.find_element_by_id("onboard-new-organisation-form-serialNumber").send_keys(device_snum)
    #
    sleep(2)
    # 按下一步continue，跳转Location Information
    driver.find_element_by_css_selector("#form_continue_add-device").click()
    #
    sleep(2)
    # latitude
    device_LI_latitude = cf.get("LocationInformation", "latitude")
    driver.find_element_by_css_selector("#onboard-new-organisation-form-latitude").send_keys(device_LI_latitude)
    # longitude
    device_LI_longitude = cf.get("LocationInformation", "longitude")
    driver.find_element_by_css_selector("#onboard-new-organisation-form-longitude").send_keys(device_LI_longitude)
    #
    sleep(8)
    # cancel the form
    driver.find_element_by_id("form_cancel_add-device").click()
    #
    # save the form
    #driver.find_element_by_id("form_ok_add-device").click()
    #
    # logout
    driver.find_element_by_css_selector("#top-nav > div > div.top-bar.span12 > div.pull-right > div > div > ul > li:nth-child(6) > a").click()
    sleep(2)
    driver.find_element_by_id("user-logout").click()
    #
    driver.quit()
    #
    #("#top-nav > div > div.top-bar.span12 > div.pull-right > div > div > ul > li.dropdown.open > ul")
    '''
    from selenium.webdriver.support.select import Select
    #template-object-solutionTier, 输入 Advance SDWAN NGFW
    Select(driver.find_element_by_id('template-object-solutionTier')).select_by_index(7)
    # 输入默认分析器 VA
    Select(driver.find_element_by_id('template-object-analyticsCluster')).select_by_index(1)
    #sleep(2)
    '''



if __name__ == '__main__':
    # 获取驱动
    path = "E:\\ProgramData\\Anaconda3\\chromedriver.exe"
    driver = webdriver.Chrome(path)
    #driver = selenium.webdriver.remote.webdriver.WebDriver(command_executor="http://192.168.1.51:5555/wd/hub", desired_capabilities=DesiredCapabilities.CHROME)
    login_versa(driver)
    # 验证登录元素
    # login_status > ul > li:nth-child(1) > a:nth-child(1)
    # login_status > ul > li:nth-child(1) > a:nth-child(1) > strong
    user_name_element = driver.find_element_by_css_selector("#top-nav > div > div.top-bar.span12 > div.pull-right > div > div > ul > li.dropdown > a")
    print(user_name_element.text)
    name = user_name_element.text
    if u"shct ( shct )" == name:
        print("login pass")
    else:
        print("login name is not shct")
    dlydevices(driver)


    #driver.quit()
