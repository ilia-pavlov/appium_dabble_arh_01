from behave import given, when, then


@given('Tap on button next0')
def tap_button(context):
    context.constructor.launch_page.tap_button_create_account()


@then('Tap on button next1')
def tap_button(context):
    context.constructor.launch_page.tap_button_create_account()


@then('Tap on button next2')
def tap_button(context):
    context.constructor.launch_page.tap_button_create_account()


@then('Tap on button next3')
def tap_button(context):
    context.constructor.launch_page.tap_button_create_account()


@when('Input {text} to phone number field')
def input_phone_number(context, text):
    context.constructor.sign_up_page.input_phone_number(text)


@then('Tap on picker')
def choose_date_of_birth(context):
    context.constructor.sign_up_page.tap_date_of_birth_picker()


@then('Tap on sigh up button')
def tap_sign_up(context):
    context.constructor.sign_up_page.tap_button_sign_up()


@then('Tap on OK')
def tap_pop_up_confirm_phone(context):
    context.constructor.sign_up_page.tap_pop_up_confirm_phone


@when('Input {text} to passcode field')
def input_passcode(context, text):
    context.constructor.sign_up_page.input_passcode(text)


@then('Tap on pop up button')
def tap_on_pop_up_password_terms(context):
    context.constructor.sign_up_page.tap_pop_up_password_terms()


@when('Input {text} on password filed')
def input_password(context, text):
    context.constructor.sign_up_page.input_password(text)


@then('Press keycode {number}')
def press_enter_on_keyboard(context, number):
    context.constructor.sign_up_page.tap_enter_on_keyboard(number)


@then('Tap finish button')
def tap_finish_button(context):
    context.constructor.sign_up_page.tap_finish_button()


@then('Verify home screen by text {title}')
def verify_title_on_home_screen(context, title):
    context.constructor.sign_up_page.verify_title_on_home_screen(title)
