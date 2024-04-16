import os
import sys
from .user import log_in, log_out, register
from .sqlRequests import select, update, delete

starting_options_list = {"1": log_in, "2": register, "3": sys.exit}


def execute_option(option: str, page: str) -> bool:
    if page == "main":
        option = main_options_list.get(str(option))
    if page == "starting":
        option = starting_options_list.get(str(option))
    if option():
        return True
    else:
        return False


def choose_product() -> None:
    from .user import current_user

    while True:
        products = select("products")
        os.system("cls" if os.name == "nt" else "clear")
        print("(id, name, price, amount, provider_id_fk)")
        print("\n".join(str(product) for product in products))
        print("[1] - Choose product\n[2] - Back")
        option = input("Enter your option: ")
        if option == "1":
            product_id = input("Enter product id: ")
            amount_of_products = input("Enter amount of products: ")
            print("Added to cart!!!")
            current_user.add_to_cart(product_id, amount_of_products)
        if option == "2":
            return
        else:
            pass


def buy_products() -> bool:
    from .user import current_user

    try:
        for item in current_user.get_cart():
            id_pk, amount = item
            update("products", f"amount = amount - {amount}", f"id_pk = {id_pk}")
            current_user.clear_cart()
        return True
    except Exception as e:
        return False


def remove_from_cart() -> None:
    from .user import current_user

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Your cart:")
        print(f"    {current_user.get_cart()}")
        index_to_remove = input(
            "Enter the index of the product you want to remove or type 'back' "
        )
        if index_to_remove == "back":
            return
        current_user.remove_from_cart(index_to_remove)


def delete_account() -> bool:
    from .user import current_user

    phone_number = current_user.get_phone_number()
    if delete("clients", f"phone_number = '{phone_number}'"):
        current_user = None
        return True
    else:
        return False


def cart_page() -> None:
    from .user import current_user

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Your cart:")
        current_cart = current_user.get_cart()
        if current_cart:
            for index, item in enumerate(current_cart):
                print(f"{index}. {item}")
        print("[1] Buy products\n[2] Remove product\n[3] Clear cart\n[4] Back")
        option = input("Enter your option: ")
        if option == "1":
            buy_products()
        if option == "2":
            remove_from_cart()
        if option == "3":
            current_user.clear_cart()
        if option == "4":
            return
        else:
            pass


def market_page() -> None:
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("[1] Add product to the cart\n[2] Your cart\n[3] Back")
        option = input("Enter your option: ")
        if option == "1":
            choose_product()
        if option == "2":
            cart_page()
        if option == "3":
            return
        else:
            pass


def personal_page() -> None:
    from .user import current_user

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"first name: {current_user.get_first_name()}")
        print(f"last name: {current_user.get_last_name()}")
        print(f"phone number nuber: {current_user.get_phone_number()}")
        print("[1] Delete account\n[2] Back\n")
        option: str = input("Choose option: ")
        if option == "1":
            option = input("Are you sure?[y]/[n]")
            if option == "y":
                if delete_account():
                    input()
                    sys.exit()
            else:
                return
        if option == "2":
            return
        else:
            print("Wrong option")
        option: str = input("Choose option: ")


main_options_list = {"1": market_page, "2": personal_page, "3": log_out}


def main_options() -> None:
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("[1] Market\n[2] Personal info\n[3] Log-out")
        option: str = input("Choose option: ")
        if not execute_option(option, "main"):
            print("Error... try again")


def main_page() -> None:
    from .user import current_user

    if current_user:
        main_options()


def start() -> None:
    while True:
        print("[1] Log-in\n[2] Register\n[3] Exit")
        option: str = input("Choose option: ")
        if execute_option(option, "starting"):
            main_page()
        else:
            print("Error... try again")


if __name__ == "__main__":
    start()
