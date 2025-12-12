from database.database_manager import get_connection
from utils.validators import is_valid_date, is_future_date, is_valid_national_id


def add_passport(
    national_id,
    passport_number,
    full_name,
    date_of_birth,
    nationality,
    issue_date,
    expiry_date,
    authority,
):
    if not is_valid_national_id(national_id):
        raise ValueError("Invalid national ID format.")
    if (
        not is_valid_date(date_of_birth)
        or not is_valid_date(issue_date)
        or not is_valid_date(expiry_date)
    ):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    if not is_future_date(expiry_date):
        raise ValueError("Expiry date must be in the future.")

    conn = get_connection()
    try:
        conn.execute(
            """
            INSERT INTO passports (national_id, passport_number, full_name, date_of_birth, nationality, issue_date, expiry_date, authority)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                national_id,
                passport_number,
                full_name,
                date_of_birth,
                nationality,
                issue_date,
                expiry_date,
                authority,
            ),
        )
        conn.commit()
    except conn.IntegrityError as e:
        raise ValueError(f"Error: {e}")
    finally:
        conn.close()


def view_all_passports():
    conn = get_connection()
    cursor = conn.execute("SELECT * FROM passports")
    passports = cursor.fetchall()
    conn.close()
    return passports


def search_passport(search_term):
    conn = get_connection()
    cursor = conn.execute(
        """
        SELECT * FROM passports 
        WHERE national_id LIKE ? OR passport_number LIKE ? OR full_name LIKE ?
    """,
        (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"),
    )
    passports = cursor.fetchall()
    conn.close()
    return passports


def update_passport(passport_number, **kwargs):
    conn = get_connection()
    try:
        updates = ", ".join([f"{key} = ?" for key in kwargs])
        values = list(kwargs.values()) + [passport_number]
        conn.execute(
            f"UPDATE passports SET {updates} WHERE passport_number = ?", values
        )
        conn.commit()
    finally:
        conn.close()


def delete_passport(passport_number):
    conn = get_connection()
    try:
        conn.execute(
            "DELETE FROM passports WHERE passport_number = ?", (passport_number,)
        )
        conn.commit()
    finally:
        conn.close()
