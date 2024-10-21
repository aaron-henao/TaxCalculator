CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE calculations (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    gross_income NUMERIC(12, 2),
    deductions NUMERIC(12, 2),
    tax_credits NUMERIC(12, 2),
    tax_paid NUMERIC(12, 2),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
