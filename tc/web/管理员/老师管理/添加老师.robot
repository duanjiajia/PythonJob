*** Settings ***
Library   pylib/WebAdmin.py
Library   SeleniumLibrary
Library   Collections


*** Test Cases ***

用例2：添加老师操作
       [Setup]   run keywords   Clearallteacher
       ...   AND  ClearAllcourse

       ...   AND  AddCourse   初中语文      这是语文课       1
       ...   AND  AddCourse   初中数学      这是数学课        2



       AddTeacher   王老师     wang    这是王老师    2    初中语文
       AddTeacher   李老师     Li      这是李老师    1    初中数学
       ${Tname}=   Getteacherlist
       log to console   ${Tname}
       should be true  　$Tname == ['李老师','王老师']

       [Teardown]  run keywords   Clearallteacher   AND   ClearAllcourse