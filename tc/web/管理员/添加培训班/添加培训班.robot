*** Settings ***
Library   SeleniumLibrary
Library   Collections
Library   pylib/WebAdmin.py


*** Test Cases ***

添加培训班 001：
    [Setup]  run keywords    ClearAllclass
    ...  AND    ClearAllcourse
    ...   AND   AddCourse   初中语文   这是语文   1
    ...   AND   AddCourse   初中数学    这是数学    2

    ${Lesson}=   create list    初中语文   初中数学
    ${Lesson2}=   create list    初中语文

    AddClass   初中班     这是初中班    1    ${Lesson}
    AddClass   小学     这是初中班    1    ${Lesson2}
    ${classlists}=     Getclasslist
    log to console    ${classlists}
    sleep   1
    should be true  ${classlists} == ['初中班','小学']

    [Teardown]  run keywords  ClearAllclass
    ...  AND   ClearAllcourse

