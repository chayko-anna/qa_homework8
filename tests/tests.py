import allure
from selene import have, by


@allure.title("Successful fill form")
def test_successful(browser_settings):
    browser = browser_settings
    first_name = "Anna"
    last_name = "Chayko"

    with allure.step("Open registrations form"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Fill form"):
        browser.element("#firstName").set_value(first_name)
        browser.element("#lastName").set_value(last_name)
        browser.element("#userEmail").set_value("al.nchko@gmail.com")
        browser.element("#genterWrapper").element(by.text("Female")).click()
        browser.element("#userNumber").set_value("1231231231")
        # browser.element("#dateOfBirthInput").click()
        # browser.element(".react-datepicker__month-select").s("13")
        # browser.element(".react-datepicker__year-select").selectOption("2000")
        # browser.element(".react-datepicker__day--013:not(.react-datepicker__day--outside-month)").click()
        browser.element("#subjectsInput").send_keys("Arts")
        browser.element("#subjectsInput").press_enter()
        browser.element("#hobbiesWrapper").element(by.text("Sports")).click()
        # browser.element("#uploadPicture").uploadFromClasspath("img/1.png")
        browser.element("#currentAddress").set_value("Улица Пушкина, дом Колотушкина")
        browser.element("#state").click()
        browser.element("#stateCity-wrapper").element(by.text("NCR")).click()
        browser.element("#city").click()
        browser.element("#stateCity-wrapper").element(by.text("Delhi")).click()
        browser.element("#submit").click()

    with allure.step("Check form results"):
        browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
        # browser.element(".table-responsive").should(
        #     have.texts(first_name, last_name, "alex@egorov.com", "Some street 1"))
