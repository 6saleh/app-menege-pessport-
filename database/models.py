def create_table(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS passports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        national_id TEXT UNIQUE NOT NULL,
        passport_number TEXT UNIQUE NOT NULL,
        full_name TEXT NOT NULL,
        date_of_birth TEXT NOT NULL,
        nationality TEXT NOT NULL,
        issue_date TEXT NOT NULL,
        expiry_date TEXT NOT NULL,
        authority TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
