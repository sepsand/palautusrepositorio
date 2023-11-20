*** Settings ***
Resource  resource.robot
Resource  resource_login.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Variables ***
${PASSWORD}  kalle123
${PASSWORD2}  kalle223
${PASSWORD_INVALID}  kallekkk
${USERNAME}  kallee
${USERNAME2}  kallef
${USERNAME3}  kalleg
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

Login After Successful Registration
    Set Username  ${USERNAME2}
    Set Password  ${PASSWORD}
    Set Password Confirmation  ${PASSWORD}
    Submit Register
    Welcome Page Should Be Open
    Continue To Main Page
    Main Page Should Be Open
    Submit Logout
    Login Page Should Be Open
    Set Username  ${USERNAME2}
    Set Password  ${PASSWORD}
    Submit Credentials
    Main Page Should Be Open

Login After Failed Registration
    Set Username  ${USERNAME3}
    Set Password  ${PASSWORD_INVALID}
    Set Password Confirmation  ${PASSWORD_INVALID}
    Submit Register
    Register Page Should be Open
    Go To Login Page
    Login Page Should Be Open
    Set Username  ${USERNAME3}
    Set Password  ${PASSWORD_INVALID}
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Continue To Main Page
    Click Link  Continue to main page

Register Should Fail
    Register Page Should be Open

Register Should Succeed
    Welcome Page Should Be Open

Submit Logout
    Click Button  Logout

Submit Register
    Click Button  Register

Set Password Confirmation
    [Arguments]  ${password}
    Input Text  password_confirmation  ${password}
