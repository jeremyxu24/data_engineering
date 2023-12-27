-- Create the client table
CREATE TABLE client (
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email_address VARCHAR(100),
    phone_number VARCHAR(100)
);

-- Insert 10 sample rows
INSERT INTO client (first_name, last_name, email_address, phone_number)
VALUES
    ('John', 'Doe', 'john.doe@example.com', '555-1234'),
    ('Jane', 'Smith', 'jane.smith@example.com', '555-5678'),
    ('Bob', 'Johnson', 'bob.johnson@example.com', '555-9876'),
    ('Alice', 'Williams', 'alice.williams@example.com', '555-4321'),
    ('Charlie', 'Brown', 'charlie.brown@example.com', '555-8765'),
    ('Eva', 'Miller', 'eva.miller@example.com', '555-2345'),
    ('David', 'Lee', 'david.lee@example.com', '555-7890'),
    ('Grace', 'Jones', 'grace.jones@example.com', '555-3456'),
    ('Frank', 'Davis', 'frank.davis@example.com', '555-6543'),
    ('Helen', 'Moore', 'helen.moore@example.com', '555-2109');
