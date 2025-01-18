from registration import RegistrationPage
from tests.user_data import user_for_registration


def test_form():
    user = user_for_registration
    reg_test = RegistrationPage()

    reg_test.open_form()
    reg_test.register_user(user)

    reg_test.assert_user_info(user)
