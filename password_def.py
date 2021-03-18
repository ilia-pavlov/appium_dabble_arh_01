import random
import string


def random_email_generator(length):
    letters = string.ascii_lowercase
    upper_case_letters = string.ascii_uppercase
    numbers = str(random.randint(100, 999))

    result_str = ''.join(random.choice(letters) for i in range(length))
    first_letters = ''.join(random.choice(upper_case_letters) for i in range(length))
    return first_letters + result_str + numbers


print(random_email_generator(5))
