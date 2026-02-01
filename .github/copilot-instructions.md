# Copilot Instructions for Finanzas-personales

## Overview
This project is a personal finance management system built in Python. It utilizes a database connection for data storage and a graphical user interface (GUI) for user interaction.

## Architecture
- **Main Components**: The project consists of modules for database connection (`conexion.py`), window management (`ventanas.py`), and layout positioning (`dimensiones.py`).
- **Data Flow**: User inputs are collected through the GUI and processed to interact with the database.
- **Service Boundaries**: Each module has a specific responsibility, ensuring separation of concerns.

## Developer Workflows
- **Running the Application**: Use the command `python main.py` to start the application.
- **Database Configuration**: Ensure that environment variables for database connection are set:
  - `DB_SERVER`
  - `DB_NAME`
  - `DB_USER`
  - `DB_PASSWORD`
- **Testing**: Tests can be added in the `test/` directory. Use `pytest` to run tests.

## Project Conventions
- **Environment Variables**: Sensitive information such as database credentials should be stored in environment variables to avoid hardcoding.
- **Window Centering**: The `center_window` function in `dimensiones.py` is used to center GUI windows, promoting a consistent user experience.

## Integration Points
- **Database**: The application connects to a SQL Server database using `pyodbc`. Ensure the ODBC driver is installed.
- **GUI Framework**: The project uses `tkinter` for the GUI, which is standard in Python for desktop applications.

## Examples
- **Centering a Window**: The `center_window` function is called in `ventanas.py` to position the income window correctly.

## Additional Notes
- Review the `README.md` for project setup instructions and additional context.