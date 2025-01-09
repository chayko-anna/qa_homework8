from selene import browser, have
from registration import RegistrationPage


def test_form():
    reg_test = RegistrationPage()
    reg_test.open_form()
    reg_test.type_first_name('Anna')
    reg_test.type_last_name('Chayko')
    reg_test.type_email('al.nchko@gmail.com')
    reg_test.select_gender('female')
    reg_test.type_phone_number('9102906632')
    reg_test.select_photo("../tests/shutterstock_2331893385.jpg")
    reg_test.type_address('Улица Пушкина, дом Колотушкина')
    reg_test.choose_hobby(hobbies=['sporst'])
    reg_test.select_subject(subjects=['Arts'])
    reg_test.select_birth_date(13, 0, 2000)
    reg_test.select_city('Dehli')
    reg_test.select_state('NCR')

    reg_test.press_submit()

    browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))

    browser.element('[class="table-responsive"]').should(have.text('Anna Chayko'))
    browser.element('[class="table-responsive"]').should(have.text('al.nchko@gmail.com'))
    browser.element('[class="table-responsive"]').should(have.text('9102906632'))
    browser.element('[class="table-responsive"]').should(have.text('13 January,2000'))
    browser.element('[class="table-responsive"]').should(have.text('Female'))

    browser.element('[class="table-responsive"]').should(have.text('Arts'))
    #browser.element('[class="table-responsive"]').should(have.text('Computer Science'))
    browser.element('[class="table-responsive"]').should(have.text('Sports'))
    browser.element('[class="table-responsive"]').should(have.text('Reading'))

    browser.element('[class="table-responsive"]').should(have.text('shutterstock_2331893385.jpg'))

    browser.element('[class="table-responsive"]').should(have.text('Улица Пушкина, дом Колотушкина'))
    browser.element('[class="table-responsive"]').should(have.text('NCR Gurgaon'))