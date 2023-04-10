# Task Manager with Python and MySQL

This project is a simple task manager built with Python and MySQL. It allows users to create and manage tasks, as well as track their progress.

## Getting Started

### Prerequisites

- Python 3.x
- MySQL

### Installation

1. Clone this repository to your local machine using `git clone https://github.com/your_username/your_project_name.git`
2. Open your terminal and execute the command `mysql -u root` to enter the MySQL command line interface. If this doesn't work, you may need to add the MySQL environment variable to your system.
3. Once you're in the MySQL command line interface, create a new database by running `CREATE DATABASE database_name;`
4. Check that the database has been created by running `SHOW DATABASES;` and verifying that the database appears in the list.
5. Select the newly created database by running `USE database_name;`
6. Create the `tasks` table with the following attributes: `id` (primary key), `description` (not null), `indicateur` (not null, default 0). To create this table, run the following SQL command:

```
CREATE TABLE tasks (
id INT PRIMARY KEY,
description VARCHAR(255) NOT NULL,
indicateur INT NOT NULL DEFAULT 0
);

```
