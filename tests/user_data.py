from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    birthday_date: dict[str:str]
    subject: str
    hobbies: str
    img: str
    address: str
    state: str
    city: str


user_for_registration = User(
    first_name='Anna',
    last_name='Chayko',
    email='al.nchko@gmail.com',
    birthday_date={'year': '2000', 'month': 'January', 'day': '13'},
    gender='Female',
    number='9102906632',
    subject="Computer Science",
    hobbies="Sports",
    img='shutterstock_2331893385.jpg',
    address='Улица Пушкина, дом Колотушкина',
    state='NCR',
    city='Delhi'
)
