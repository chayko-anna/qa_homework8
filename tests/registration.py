from selene import browser, have
import os.path


class RegistrationPage:
    def open_form(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def type_email(self, param):
        browser.element('[id="userEmail"]').type(param)

    def type_first_name(self, param):
        browser.element('[id="firstName"]').type(param)

    def type_last_name(self, param):
        browser.element('[id="lastName"]').type(param)

    def select_gender(self, gender):
        if gender == 'male':
            browser.element('[for="gender-radio-1"]').click()
        elif gender == 'female':
            browser.element('[for="gender-radio-2"]').click()

    def type_phone_number(self, param):
        browser.element('[id="userNumber"]').type(param).press_tab()

    def select_birth_date(self, day, month, year):
        browser.element('[class="react-datepicker__month-select"]').element('[value="0"]').click()
        browser.element('[class="react-datepicker__year-select"]').element('[value="2000"]').click()
        browser.element('[class="react-datepicker__day react-datepicker__day--013"]').click()

    def select_photo(self, filename):
        browser.element('[id="uploadPicture"]').set_value(os.path.abspath(filename))

    def select_subject(self, subjects):
        for subject in subjects:
            browser.element('[id="subjectsInput"]').type(subject)
            browser.all('.subjects-auto-complete__menu').element_by(have.text(subject)).click()

    def choose_hobby(self, hobbies):
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-2"]').click()

    def type_address(self, address):
        browser.element('[id="currentAddress"]').type(address)

    def select_state(self, state):
        browser.element('[id="state"]').click()
        browser.element('#react-select-3-option-0').click()

    def select_city(self, city):
        browser.element('[id="city"]').click()
        browser.element('#react-select-4-option-1').click()

    def press_submit(self):
        browser.element('[id="submit"]').click()