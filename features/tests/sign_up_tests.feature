# Created by iliapavlov at 0323..2021
Feature: User sigh up
  # Enter feature description here

  Scenario: User sigh up successfully and verify home screen
    Given Tap on button next0
    Then Tap on button next1
    Then Tap on button next2
    Then Tap on button next3
    When Input 9292921324 to phone number field
    Then Tap on picker
    Then Tap on sigh up button
    Then Tap on OK
    When Input 4455 to passcode field
    Then Tap on pop up button
    When Input HuErEdEdd on password filed
    Then Press keycode 69
    Then Tap finish button
    Then Verify home screen by text From Dabbl