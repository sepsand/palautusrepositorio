*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Variables ***
${PASSWORD}  kalle123
${PASSWORD2}  kalle223
${PASSWORD_INVALID}  kallekkk
${USERNAME}  kalle
${USERNAME_SHORT}  ka

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ${USERNAME}
    Set Password  ${PASSWORD}
    Set Password Confirmation  ${PASSWORD}
    Submit Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ${USERNAME_SHORT}
    Set Password  ${PASSWORD}
    Set Password Confirmation  ${PASSWORD}
    Submit Register
    Register Should Fail

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  ${USERNAME}
    Set Password  ${PASSWORD_INVALID}
    Set Password Confirmation  ${PASSWORD_INVALID}
    Submit Register
    Register Should Fail

Register With Nonmatching Password And Password Confirmation
    Set Username  ${USERNAME}
    Set Password  ${PASSWORD}
    Set Password Confirmation  ${PASSWORD2}
    Submit Register
    Register Should Fail

*** Keywords ***
Register Should Fail
    Register Page Should be Open

Register Should Succeed
    Welcome Page Should Be Open

Submit Register
    Click Button  Register

Set Password Confirmation
    [Arguments]  ${password}
    Input Text  password_confirmation  ${password}
