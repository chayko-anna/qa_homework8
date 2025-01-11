from registration import RegistrationPage


def test_form():
    reg_test = RegistrationPage()
    reg_test.open_form()

    reg_test.type_first_name('Anna')
    reg_test.type_last_name('Chayko')

    reg_test.type_email('al.nchko@gmail.com')
    reg_test.select_gender('female')
    reg_test.type_phone_number('9102906632')

    reg_test.select_birth_date('13', 'January', '2000')
    reg_test.select_subject(subjects=['Computer Science'])
    reg_test.choose_hobby(hobbies=['Sports'])

    reg_test.select_photo("../tests/shutterstock_2331893385.jpg")

    reg_test.type_address('Улица Пушкина, дом Колотушкина')
    reg_test.select_state('NCR')
    reg_test.select_city('Delhi')

    reg_test.press_submit()

    reg_test.assert_user_info(
        'Anna Chayko',
        'al.nchko@gmail.com',
        '13 January,2000',
        'Female',
        '9102906632',
        'Computer Science',
        'Sports',
        'shutterstock_2331893385.jpg',
        'Улица Пушкина, дом Колотушкина',
        'NCR',
        'Delhi'
    )
