
INSERT INTO users(name, email)
VALUES('Juan Pérez', 'juan@mail.com'),
('María López', 'maria@mail.com'),
('Carlos Ruiz', 'carlos@mail.com'),
('Ana Torres', 'ana@mail.com'),
('Luis Gómez', 'luis@mail.com');

INSERT INTO accounts (user_id, name, balance)
VALUES
(1, 'Cuenta Ahorro', 1500.00),
(1, 'Cuenta Corriente', 800.00),
(2, 'Cuenta Ahorro', 2500.50),
(3, 'Cuenta Nómina', 1200.00),
(3, 'Cuenta Ahorro', 300.00),
(4, 'Cuenta Personal', 950.00),
(5, 'Cuenta Principal', 400.00);


INSERT INTO transactions (account_id, amount, transaction_date, description, category)
VALUES
(1, -150.00, '2026-01-05', 'Supermercado', 'Alimentación'),
(1, -75.50,  '2026-01-07', 'Gasolina', 'Transporte'),
(2, 1200.00, '2026-01-01', 'Pago salario', 'Ingresos'),
(2, -200.00, '2026-01-10', 'Pago internet', 'Servicios'),
(3, -300.00, '2026-01-08', 'Renta', 'Vivienda'),
(3, -120.00, '2026-01-12', 'Electricidad', 'Servicios'),
(4, 900.00,  '2026-01-01', 'Pago nómina', 'Ingresos'),
(4, -100.00, '2026-01-15', 'Restaurante', 'Comida'),
(5, -50.00,  '2026-01-18', 'Café', 'Gastos personales'),
(6, -200.00, '2026-01-20', 'Compras varias', 'Otros');


INSERT INTO budgets (user_id, category, amount, start_date, end_date)
VALUES
(1, 'Alimentación', 500.00, '2026-01-01', '2026-01-31'),
(1, 'Transporte', 300.00, '2026-01-01', '2026-01-31'),
(2, 'Vivienda', 1000.00, '2026-01-01', '2026-01-31'),
(3, 'Servicios', 400.00, '2026-01-01', '2026-01-31'),
(4, 'Entretenimiento', 250.00, '2026-01-01', '2026-01-31');
