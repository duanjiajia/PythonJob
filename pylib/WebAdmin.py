# coding:utf8
from  selenium  import  webdriver
from selenium.webdriver.support.ui  import Select
from cfg import *
import time


class WebAdmin():

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def OpenBrowser(self):


        self.driver = webdriver.Chrome()



    def Closebrowser (self):
        self.driver.quit()

    def Login (self):
        self.driver.get(loginUrl)
        self.driver.find_element_by_id('username').send_keys(adminuser['name'])
        self.driver.find_element_by_id('password').send_keys(adminuser['pw'])
        self.driver.find_element_by_tag_name('button').click()
        self.driver.implicitly_wait(10)



    def ClearAllcourse(self):
        self.driver.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()
        time.sleep(1)
        self.driver.implicitly_wait(2)
        while True:
            deletecourse = self.driver.find_elements_by_css_selector("button[ng-click='delOne(one)']")
            if deletecourse == []:
                break
            deletecourse[0].click()
            self.driver.find_element_by_css_selector('button.btn.btn-primary').click()
            time.sleep(1)
        self.driver.implicitly_wait(10)

    def Clearallteacher(self):
        self.driver.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()
        time.sleep(1)
        self.driver.implicitly_wait(2)
        while True:
            deletecourse = self.driver.find_elements_by_css_selector("button[ng-click='delOne(one)']")
            if deletecourse == []:
                break
            deletecourse[0].click()
            self.driver.find_element_by_css_selector('button.btn.btn-primary').click()
            time.sleep(1)
        self.driver.implicitly_wait(10)
    def ClearAllclass(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector("ul.nav > li a[ui-sref='training']").click()
        self.driver.implicitly_wait(2)
        while True:
            deleteclass = self.driver.find_elements_by_css_selector(" button[ng-click='delOne(one)']")
            if deleteclass == []:
                break
            deleteclass[0].click()
            self.driver.find_element_by_css_selector(".bootstrap-dialog-footer-buttons >button:nth-child(2)").click()
            time.sleep(1)
        self.driver.implicitly_wait(5)








    def AddCourse(self,coursename,coursedels,coursenum):
        self.driver.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()
        self.driver.find_element_by_css_selector("button[ng-click='showAddOne=true']").click()
        ele = self.driver.find_element_by_css_selector("input[ng-model='addData.name']")
        ele.clear()
        ele.send_keys(coursename)
        ele = self.driver.find_element_by_css_selector("textarea[ng-model='addData.desc']")
        ele.clear()
        ele.send_keys(coursedels)
        ele = self.driver.find_element_by_css_selector("input[ng-model='addData.display_idx']")
        ele.clear()
        ele.send_keys(coursenum)
        self.driver.find_element_by_css_selector("button[ng-click='addOne()']").click()
        time.sleep(1)

    def AddTeacher(self,tname,lname,tdels,tnum,lesson):
        self.driver.find_element_by_css_selector("ul.nav a[ui-sref='teacher']").click()
        self.driver.find_element_by_css_selector("button[ng-click='showAddOne=true']").click()
        ele = self.driver.find_element_by_css_selector("input[ng-model='addEditData.realname']")
        ele.clear()
        ele.send_keys(tname)
        ele = self.driver.find_element_by_css_selector("input[ng-model='addEditData.username']")
        ele.clear()
        ele.send_keys(lname)
        ele = self.driver.find_element_by_css_selector("textarea[ng-model='addEditData.desc']")
        ele.clear()
        ele.send_keys(tdels)
        ele = self.driver.find_element_by_css_selector("input[ng-model='addEditData.display_idx']")
        ele.clear()
        ele.send_keys(tnum)
        select = Select(self.driver.find_element_by_css_selector("select[ng-model='$parent.courseSelected']"))
        select.select_by_visible_text(lesson)
        self.driver.find_element_by_css_selector("button[ng-click='addEditData.addTeachCourse()']").click()
        self.driver.find_element_by_css_selector("button[ng-click='addOne()']").click()
        self.driver.find_element_by_css_selector("button[ng-click='addEditData.delTeachCourse(course)']").click()
        time.sleep(1)

    def AddClass(self,Cname,Cdels,Cnum,Lesson):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector("ul.nav > li a[ui-sref='training']").click()
        self.driver.find_element_by_css_selector("button[ng-click='showAddOne=true']").click()
        ele = self.driver.find_element_by_css_selector("input[ng-model='addEditData.name']")
        ele.clear()
        ele.send_keys(Cname)
        ele = self.driver.find_element_by_css_selector("textarea[ng-model='addEditData.desc']")
        ele.clear()
        ele.send_keys(Cdels)
        ele = self.driver.find_element_by_css_selector("input[ng-model='addEditData.display_idx']")
        ele.clear()
        ele.send_keys(Cnum)
        select = Select(self.driver.find_element_by_css_selector("select[ng-model='$parent.courseSelected']"))

        for one in Lesson:

            select.select_by_visible_text(one)
            self.driver.find_element_by_css_selector("button[ng-click='addEditData.addTeachCourse()']").click()
            # time.sleep(5)
        self.driver.find_element_by_css_selector("button[ng-click='addOne()']").click()
        eles = self.driver.find_elements_by_css_selector("button[ng-click='addEditData.delTeachCourse(course)']")
        for ele in eles :
            ele.click()






    def Getcourselist(self):
        self.driver.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()
        eles = self.driver.find_elements_by_css_selector("tr>td:nth-child(2)")
        return [ele.text for ele in eles]

    def Getteacherlist(self):
        self.driver.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()
        eles = self.driver.find_elements_by_css_selector("tr >td:nth-child(2)")
        return [ele.text for ele in eles]
    def Getclasslist(self):
        self.driver.find_element_by_css_selector("ul.nav  a[ui-sref='training']").click()
        eles= self.driver.find_elements_by_css_selector("tr[current-page='$parent.currentPage']>td:nth-child(2)")
        return [ele.text for ele in eles]




# a= WebAdmin()
# a.Openbrowser()
# a.Login()




