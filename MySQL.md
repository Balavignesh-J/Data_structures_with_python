# Essential MySQL Commands

## Database Operations
- `CREATE DATABASE dbname;` - Create a new database
- `DROP DATABASE dbname;` - Delete a database
- `SHOW DATABASES;` - List all databases
- `USE dbname;` - Select a database to work with

## Table Operations
- `CREATE TABLE tablename (column1 datatype, column2 datatype, ...);` - Create a new table
- `DROP TABLE tablename;` - Delete a table
- `SHOW TABLES;` - List all tables in current database
- `DESCRIBE tablename;` or `DESC tablename;` - Show table structure
- `ALTER TABLE tablename ADD columnname datatype;` - Add a column
- `ALTER TABLE tablename DROP COLUMN columnname;` - Remove a column
- `ALTER TABLE tablename MODIFY COLUMN columnname newdatatype;` - Modify column datatype
- `ALTER TABLE tablename RENAME TO newtablename;` - Rename a table
- `TRUNCATE TABLE tablename;` - Delete all data in a table but keep the structure

## Data Manipulation
- `INSERT INTO tablename (column1, column2, ...) VALUES (value1, value2, ...);` - Insert data
- `SELECT column1, column2 FROM tablename;` - Select data
- `SELECT * FROM tablename;` - Select all columns
- `UPDATE tablename SET column1=value1, column2=value2 WHERE condition;` - Update data
- `DELETE FROM tablename WHERE condition;` - Delete data
- `SELECT DISTINCT column FROM tablename;` - Select unique values

## Query Clauses
- `WHERE` - Filter records
- `ORDER BY column ASC|DESC` - Sort results
- `GROUP BY` - Group identical data
- `HAVING` - Filter groups
- `LIMIT` - Limit number of results
- `OFFSET` - Skip number of results

## Joins
- `INNER JOIN` - Returns matching records from both tables
- `LEFT JOIN` - Returns all records from left table and matched from right
- `RIGHT JOIN` - Returns all records from right table and matched from left
- `FULL JOIN` - Returns all records when there's a match in either table
- `CROSS JOIN` - Returns Cartesian product of tables

## Indexes
- `CREATE INDEX indexname ON tablename (columnname);` - Create index
- `DROP INDEX indexname ON tablename;` - Delete index
- `SHOW INDEX FROM tablename;` - Show indexes for a table

## Constraints
- `PRIMARY KEY` - Uniquely identifies each record
- `FOREIGN KEY` - Ensures referential integrity
- `NOT NULL` - Column cannot contain NULL values
- `UNIQUE` - All values in column are different
- `CHECK` - Ensures values meet specific conditions
- `DEFAULT` - Sets default value for column

## Views
- `CREATE VIEW viewname AS SELECT columns FROM table WHERE condition;` - Create view
- `DROP VIEW viewname;` - Delete view
- `SHOW FULL TABLES WHERE Table_type = 'VIEW';` - List all views

## Users and Privileges
- `CREATE USER 'username'@'host' IDENTIFIED BY 'password';` - Create user
- `DROP USER 'username'@'host';` - Delete user
- `GRANT ALL PRIVILEGES ON dbname.* TO 'username'@'host';` - Grant privileges
- `REVOKE ALL PRIVILEGES ON dbname.* FROM 'username'@'host';` - Revoke privileges
- `FLUSH PRIVILEGES;` - Reload privileges
- `SHOW GRANTS FOR 'username'@'host';` - Show user privileges

## Backup and Restore
- `mysqldump -u username -p dbname > backup.sql` - Export database (command line)
- `mysql -u username -p dbname < backup.sql` - Import database (command line)

## Transactions
- `START TRANSACTION;` - Begin transaction
- `COMMIT;` - Save changes
- `ROLLBACK;` - Undo changes
- `SAVEPOINT savepointname;` - Create savepoint
- `ROLLBACK TO savepointname;` - Rollback to savepoint

## Functions
- Aggregate: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`
- String: `CONCAT()`, `SUBSTRING()`, `TRIM()`, `UPPER()`, `LOWER()`
- Date: `NOW()`, `CURDATE()`, `DATEDIFF()`, `DATE_ADD()`
- Math: `ROUND()`, `CEIL()`, `FLOOR()`, `ABS()`, `RAND()`

## Advanced Features
- `CREATE PROCEDURE procedurename() BEGIN ... END` - Create stored procedure
- `CALL procedurename();` - Call stored procedure
- `CREATE FUNCTION functionname() RETURNS datatype BEGIN ... END` - Create function
- `CREATE TRIGGER triggername BEFORE|AFTER INSERT|UPDATE|DELETE ON tablename FOR EACH ROW BEGIN ... END` - Create trigger
- `SHOW PROCESSLIST;` - Show active connections
- `EXPLAIN SELECT ...` - Show query execution plan

## Configuration
- `SHOW VARIABLES;` - Show server variables
- `SHOW STATUS;` - Show server status
- `SET GLOBAL variable=value;` - Change global variable
- `SET SESSION variable=value;` - Change session variable