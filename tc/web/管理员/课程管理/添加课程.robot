*** Settings ***

Library    SeleniumLibrary
Library   pylib/WebAdmin.py
Library     Collections



*** Test Cases ***
用例1：添加课程
    [Setup]  ClearAllcourse
    AddCourse   初中语文      这是语文课        1
    AddCourse   初中数学      这是数学课        2
    ${coursename}=  Getcourselist
    log to console  ${coursename}
    sleep   1
    Should Be True   $coursename == [u'初中语文',u'初中数学']
    [Teardown]  ClearAllcourse



