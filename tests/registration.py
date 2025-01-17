from selene import browser, have, be
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
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def select_photo(self, filename):
        browser.element('[id="uploadPicture"]').set_value(os.path.abspath(filename))

    def select_subject(self, subjects):
        for subject in subjects:
            browser.element('[id="subjectsInput"]').type(subject)
            browser.all('.subjects-auto-complete__menu').element_by(have.text(subject)).click()

    def choose_hobby(self, hobbies):
        for hobby in hobbies:
            match hobby:
                case 'Sports':
                    browser.element('[for="hobbies-checkbox-1"]').click()
                case 'Reading':
                    browser.element('[for="hobbies-checkbox-2"]').click()
                case 'Music':
                    browser.element('[for="hobbies-checkbox-3"]').click()

    def type_address(self, address):
        browser.element('[id="currentAddress"]').type(address)

    def select_state(self, state):
        browser.element('[id="state"]').click()
        browser.element('#react-select-3-input').type(state).should(be.visible).press_enter()

    def select_city(self, city):
        browser.element('[id="city"]').click()
        browser.element('#react-select-4-input').type(city).should(be.visible).press_enter()

    def press_submit(self):
        browser.element('[id="submit"]').click()

    def assert_user_info(self, full_name, email, bday, gender, number, sub1, hob1, img, address,
                         state, city):
        browser.element('.table').all('td').even.should(have.exact_texts(
            full_name, email, gender, number, bday, sub1, hob1, img, address,
            f'{state} {city}'
        ))
