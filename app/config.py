import datetime


HOST = "127.0.0.1"
USER = "postgres"
DB_PASSWORD = "1234"
DB_NAME = "Shop"

table_names = {
    "clients": (
        ("first_name", str),
        ("last_name", str),
        ("phone_number", str),  # str("555-3001")
        ("password", str),
    ),
    "deals": (
        ("deal_time", datetime.time),  # datetime.time(9, 00, 00)
        ("deal_date", datetime.date),  # datetime.date(2024, 1, 1)
        ("amount", float),
        ("client_id_fk", int),
        ("staff_id_fk", int),
    ),
    "deals_products": (
        ("deal_id_fk", int),
        ("product_id_fk", int),
        ("amount_of_products", int),
        ("price_of_products", float),
    ),
    "product_providers": (
        ("name", str),
        ("phone_number", str),  # str("555-3001")
        ("address", str),
    ),
    "products": (
        ("name", str),
        ("price", float),
        ("amount", int),
        ("provider_id_fk", int),
    ),
    "products_warehouses": (
        ("product_id_fk", int),
        ("warehouse_id_fk", int),
        ("amount_of_products", int),
        ("date_of_delivery", datetime.date),  # datetime.date(2024, 1, 1)
    ),
    "staff": (
        ("first_name", str),
        ("last_name", str),
        ("phone_number", str),  # str("555-3001")
        ("job_position", str),  # str("loader")
        ("salary", int),
        ("warehouse_id_fk", int),
    ),
    "warehouses": (
        ("address", str),
        ("working_hours", str),  # str("9 AM - 5 PM")
        ("number_of_products", int),
    ),
}
