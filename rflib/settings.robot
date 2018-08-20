*** Settings ***
Library    SeleniumLibrary
Library    Collections
Variables     cfg.py

*** Keywords ***
TestSuit
    Open browser   about:blank    chrome

TestTeardown
    close browser


Longin
    go to     ${loginUrl}
    input text   id=username     &{adminuser}[name]
    input text   id=password     &{adminuser}[pw]
    click element  css=button[onclick="postLoginRequest()"]

ClearAllCourse
#    Longin
    set browser implicit wait   2
    click element  css=a[ui-sref="course"]
    :FOR  ${one}   IN RANGE   99
    \    ${elements}=   Get WebElements   css=button[ng-click="delOne(one)"]
    \    exit for loop if    $elements==[]
    \    click element   @{elements}[0]
    \    click element  css=button.btn.btn-primary
    \    sleep  1
    set browser implicit wait    10

ClearAllTeacher
#    Longin
    set browser implicit wait   2
    click element  css=a[ui-sref="teacher"]
    :FOR  ${one}   IN RANGE  99
    \    ${elements}=   Get WebElements   css=button[ng-click="delOne(one)"]
    \    exit for loop if    $elements==[]
    \    click element   @{elements}[0]
    \    click element  css=button.btn.btn-primary
    \    sleep  1
    set browser implicit wait    10

AddCourse
    click element  css=a[ui-sref="course"]
    [Arguments]     ${CourseName}     ${CourseDels}   ${CourseNum}
    click element  css=button[ng-click="showAddOne=true"]
    input text   css=input[ng-model="addData.name"]    ${CourseName}
    input text   css=textarea[ng-model="addData.desc"]    ${CourseDels}
    input text   css=input[ng-model="addData.display_idx"]   ${CourseNum}
    click element  css=button[ng-click="addOne()"]
    sleep   1

CheckCourseName
    ${eles}=      Get Webelements   css=tr.ng-scope > td:nth-child(2) >span
    ${Cnames}=  create list
    :FOR   ${ele}   IN   @{eles}
    \   append to list   ${Cnames}    ${ele.text}
    \   log to console     ${Cnames}
    [Return]      ${Cnames}
CheckCoursenum
    ${eles}=      Get Webelements   css=tr.ng-scope > td:nth-child(1) >span
    ${Cnums}=  create list
    :FOR   ${ele}   IN   @{eles}
    \   append to list   ${Cnums}    ${ele.text}
    \   log to console     ${Cnums}
    [Return]      ${Cnums}

AddTeacher
    click element  css=a[ui-sref="teacher"]
    [Arguments]    ${tname}   ${lname}   ${teacherdel}    ${tnum}    ${lesson}
    click element   css=button[ng-click="showAddOne=true"]
    input text    css= input[ng-model="addEditData.realname"]    ${tname}
    input text    css= input[ng-model="addEditData.username"]    ${lname}
    input text    css= textarea[ng-model="addEditData.desc"]    ${teacherdel}
    input text    css= input[ng-model="addEditData.display_idx"]    ${tnum}
    Select From List By Label   css=select[ng-model="$parent.courseSelected"]    ${lesson}
    Click element  css=button[ng-click="addEditData.addTeachCourse()"]
    click element   css=button[ng-click="addOne()"]
    click element   css=button[ng-click="addEditData.delTeachCourse(course)"]
    sleep   1

CheckteacherName
    ${eles}=      Get Webelements   css=tr[total-items="totalNum"] > td:nth-child(2) >span
    ${Tnames}=  create list
    :FOR   ${ele}   IN   @{eles}
    \   append to list   ${Tnames}    ${ele.text}
#    \   log to console     ${Tnames}
    [Return]      ${Tnames}