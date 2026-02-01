
CREATE TABLE users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    email NVARCHAR(255) NOT NULL UNIQUE,
    created_at DATETIMEOFFSET NOT NULL 
        DEFAULT SYSDATETIMEOFFSET()
);

CREATE TABLE accounts (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    user_id INT NOT NULL,
    name NVARCHAR(255) NOT NULL,
    balance DECIMAL(12,2) NOT NULL DEFAULT 0.00,
    created_at DATETIMEOFFSET NOT NULL 
        DEFAULT SYSDATETIMEOFFSET(),

    CONSTRAINT FK_accounts_users
        FOREIGN KEY (user_id) REFERENCES users(id)
);


CREATE TABLE transactions (
    id INT IDENTITY(1,1) PRIMARY KEY,
    account_id BIGINT NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    transaction_date DATE NOT NULL,
    description NVARCHAR(MAX),
    category NVARCHAR(255),
    created_at DATETIMEOFFSET NOT NULL 
        DEFAULT SYSDATETIMEOFFSET(),

    CONSTRAINT FK_transactions_accounts
        FOREIGN KEY (account_id) REFERENCES accounts(id)
);


CREATE TABLE budgets (
    id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT NOT NULL,
    category NVARCHAR(255) NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    created_at DATETIMEOFFSET NOT NULL 
        DEFAULT SYSDATETIMEOFFSET(),

    CONSTRAINT FK_budgets_users
        FOREIGN KEY (user_id) REFERENCES users(id)
);


