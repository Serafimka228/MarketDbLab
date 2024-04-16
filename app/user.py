import re
import os
from .sqlRequests import select, insert


class User:
    def __init__(
        self,
        first_name: str = None,
        last_name: str = None,
        phone_number: str = None,
        password: str = None,
    ):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone_number = phone_number
        self.__password = password
        self.__cart = None

    def add_to_cart(self, product_id: str, amount: int) -> None:
        if not self.__cart:
            self.__cart = []
        self.__cart.append((product_id, amount))

    def get_cart(self) -> list[tuple] or None:
        if self.__cart:
            return self.__cart
        return None

    def remove_from_cart(self, index: int) -> None:
        try:
            del self.__cart[int(index)]
        except (IndexError, ValueError, AttributeError, TypeError) as e:
            print("IndexError")

    def clear_cart(self) -> None:
        self.__cart.clear()

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_phone_number(self) -> str:
        return self.__phone_number

    __cart: list[tuple]
    __first_name: str
    __last_name: str
    __phone_number: str
    __password: str


current_user = None


def log_in() -> bool:
    global current_user
    os.system("cls" if os.name == "nt" else "clear")
    phone_number = str(input("Enter phone number: "))
    password = input("Enter password: ")
    user = select(
        "clients", f"WHERE phone_number='{str(phone_number)}' AND password='{password}'"
    )
    if user:
        print("logged in!!!")
        current_user = User(user[0][1], user[0][2], user[0][3], user[0][4])
        return True
    else:
        return False


def register() -> bool:
    global current_user
    os.system("cls" if os.name == "nt" else "clear")
    first_name = str(input("Enter first name: "))
    last_name = str(input("Enter second name: "))
    phone_number = str(input("Enter phone number XXX-XXXX: "))
    correct_phone = re.fullmatch(r"\d{3}-\d{4}", phone_number)
    password = str(input("Enter password: "))
    already_exists = select("clients", f"WHERE phone_number='{phone_number}'")
    if not correct_phone:
        print("Phone number format: XXX-XXXX")
        return False
    if already_exists:
        print("Entered phone number is already registred")
        return False
    else:
        if insert(
            "clients",
            f"{first_name}",
            f"{last_name}",
            f"{phone_number}",
            f"{password}",
        ):
            print("Registred!!!")
            return True
        else:
            return False


def log_out() -> bool:
    global current_user
    current_user = None
    return True
