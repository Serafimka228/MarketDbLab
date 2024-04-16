import decimal
import psycopg2
from .config import DB_PASSWORD, DB_NAME, HOST, USER, table_names


def insert(table_name: str, *attributes) -> bool:
    """
    INSERT INTO {table_name} ({attributes_names}) VALUES ({attributes})

    Sample:
        insert("clients", "John", "Bravo", "555-2031", "qwerty12345")
    """
    try:
        connection = psycopg2.connect(
            user=USER, host=HOST, password=DB_PASSWORD, database=DB_NAME
        )
        with connection.cursor() as cursor:
            attributes_names: tuple[tuple] = table_names.get(table_name, None)
            data_types: tuple = tuple(data_type for _, data_type in attributes_names)
            attributes_names: tuple = tuple(attr for attr, _ in attributes_names)
            attributes_names = ", ".join(attributes_names)
            number_of_attributes: str = "".join(
                ["%s ", ","] * (len(data_types) - 1) + ["%s "]
            )
            cursor.execute(
                f"INSERT INTO {table_name} ({attributes_names}) VALUES ({number_of_attributes})",
                attributes,
            )
            connection.commit()
            return True
    except Exception as e:
        print(f"Exception: {e}")
        return False
    finally:
        if connection:
            connection.close()


def select(table_name: str, condition: str = "", *attribute_names) -> list or None:
    """SELECT {attributes} FROM {table_name} {condition}"""
    try:
        connection = psycopg2.connect(
            user=USER, host=HOST, password=DB_PASSWORD, database=DB_NAME
        )
        with connection.cursor() as cursor:
            if len(attribute_names) == 0:
                cursor.execute(f"SELECT * FROM {table_name} {condition}")
            else:
                attributes: str = ",".join(attribute_names)
                cursor.execute(f"SELECT {attributes} FROM {table_name} {condition}")
            return cursor.fetchall()
    except Exception as e:
        print(f"Exception: {e}")
        return None
    finally:
        if connection:
            connection.close()


def update(table_name: str, set_str: str, where_str: str) -> bool:
    try:
        connection = psycopg2.connect(
            user=USER, host=HOST, password=DB_PASSWORD, database=DB_NAME
        )
        with connection.cursor() as cursor:
            cursor.execute(
                f"UPDATE {table_name} SET {set_str} WHERE {where_str}",
            )
            connection.commit()
            return True
    except Exception as e:
        print(f"Exception: {e}")
        return False
    finally:
        if connection:
            connection.close()


def delete(table: str, condition: str) -> bool:
    try:
        connection = psycopg2.connect(
            user=USER, host=HOST, password=DB_PASSWORD, database=DB_NAME
        )
        with connection.cursor() as cursor:
            cursor.execute(
                f"DELETE FROM {table_name} WHERE ({condition})",
            )
            connection.commit()
        return True
    except Exception as e:
        print(f"Exception: {e}")
        return False
    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    # insert("clients", "John", "Bravo", "555-2031", "qwerty12345")
    select("clients", "WHERE phone_number='555-3001'", "first_name", "last_name")
    print(select("clients", "WHERE id_pk=1"))
