# Task Manager with Python and MySQL

This project is a simple task manager built with Python and MySQL. It allows users to create and manage tasks, as well as track their progress.

## Getting Started

### Prerequisites

- Python 3.x
- MySQL

### Installation

1. Clone this repository to your local machine using `https://github.com/charef00/tasks_manager_python_mysql.git`
2. Open your terminal and execute the command `mysql -u root` to enter the MySQL command line interface. If this doesn't work, you may need to add the MySQL environment variable to your system.
3. Once you're in the MySQL command line interface, create a new database by running `CREATE DATABASE database_name;`
4. Check that the database has been created by running `SHOW DATABASES;` and verifying that the database appears in the list.
5. Select the newly created database by running `USE database_name;`
6. Create the `tasks` table with the following attributes: `id` (primary key), `description` (not null), `indicateur` (not null, default 0). To create this table, run the following SQL command:

```sql
CREATE TABLE tasks (
id INT PRIMARY KEY,
description VARCHAR(255) NOT NULL,
indicateur INT NOT NULL DEFAULT 0
);

```
7. Install the required packages by running `pip install -r requirements.txt` 

8. Modify the `model.py` file to match your MySQL configuration. Specifically, you'll need to update the `__init__` method to set the `host`, `database`, `user`, `password`, `port`, `conn`, `cursor`, and `table` variables to match your MySQL setup. For example:

```python
def __init__(self):
    self.host = "localhost"
    self.database = "database_name"
    self.user = "username"
    self.password = "password"
    self.port = 3306
    self.conn = None
    self.cursor = None
    self.table = "tasks"

```

### Usage

To run the task manager, execute `python app.py` in your terminal.

https://www.youtube.com/watch?v=nVFqzOYqvDc&t=1210s

## Contributing

This project is open to contributions. If you'd like to contribute, please create a pull request or contact the project owners for more information.

## License

This project is licensed under the MIT License. See `LICENSE` for more information.
