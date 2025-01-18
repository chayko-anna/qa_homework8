from selene import browser, have, be
import os.path


class RegistrationPage:
    def open_form(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def register_user(self, user):
        browser.element('[id="userEmail"]').type(user.email)
        browser.element('[id="firstName"]').type(user.first_name)
        browser.element('[id="lastName"]').type(user.last_name)

        if user.gender == 'Male':
            browser.element('[for="gender-radio-1"]').click()
        elif user.gender == 'Female':
            browser.element('[for="gender-radio-2"]').click()

        browser.element('[id="userNumber"]').type(user.number).press_tab()

        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(user.birthday_date.get("month"))
        browser.element('.react-datepicker__year-select').type(user.birthday_date.get("year"))
        browser.element(f'.react-datepicker__day--0{user.birthday_date.get("day")}:not(.react-datepicker__day--outside-month)').click()

        browser.element('[id="subjectsInput"]').type(user.subject)
        browser.all('.subjects-auto-complete__menu').element_by(have.text(user.subject)).click()

        match user.hobbies:
            case 'Sports':
                browser.element('[for="hobbies-checkbox-1"]').click()
            case 'Reading':
                browser.element('[for="hobbies-checkbox-2"]').click()
            case 'Music':
                browser.element('[for="hobbies-checkbox-3"]').click()

        browser.element('[id="uploadPicture"]').set_value(os.path.abspath('../res/' f'{user.img}'))

        browser.element('[id="state"]').click()
        browser.element('#react-select-3-input').type(user.state).should(be.visible).press_enter()
        browser.element('[id="city"]').click()
        browser.element('#react-select-4-input').type(user.city).should(be.visible).press_enter()

        browser.element('[id="submit"]').click()

    def assert_user_info(self, user):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.number,
            f'{user.birthday_date.get("day")} {user.birthday_date.get("month")},{user.birthday_date.get("year")}',
            user.subject,
            user.hobbies,
            user.img,
            user.address,
            f'{user.state} {user.city}'
        ))
