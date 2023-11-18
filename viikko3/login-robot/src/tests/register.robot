*** Settings ***
Resource  resource.robot
#Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  dummy  pass1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  dummy  pass1234
    Input New Command
    Input Credentials  dummy  pass2134
    Output Should Contain   User with username dummy already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  d  pass1234
    Output Should Contain  Invalid username
    Input New Command
    Input Credentials  du  pass1234
    Output Should Contain  Invalid username


Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input Credentials  du1  pass1234
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  dum  pass123
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  dum  password
    Output Should Contain  Invalid password