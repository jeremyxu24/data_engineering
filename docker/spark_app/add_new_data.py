import psycopg2
import time
from faker import Faker

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="jxu_db",
    user="jxu_db",
    password="123",
    host="docker_postgres_1",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

# Create Faker instance for generating fake data
fake = Faker()

try:
    while True:
        # Generate fake data
        first_name = fake.first_name()
        last_name = fake.last_name()
        email_address = fake.email()
        phone_number = fake.phone_number()

        # Insert data into the client table
        cur.execute(
            "INSERT INTO client (first_name, last_name, email_address, phone_number) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, email_address, phone_number)
        )

        # Commit the transaction
        conn.commit()

        print(f"Row added: {first_name} {last_name}, {email_address}, {phone_number}")

        # Wait for 5 seconds before the next iteration
        time.sleep(5)

except KeyboardInterrupt:
    print("Script terminated by user.")

finally:
    # Close the cursor and connection
    cur.close()
    conn.close()
