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


# MySQL Data Types

## Numeric Data Types

### Integer Types
- `TINYINT` - 1 byte (-128 to 127) or (0 to 255) unsigned
- `SMALLINT` - 2 bytes (-32,768 to 32,767) or (0 to 65,535) unsigned
- `MEDIUMINT` - 3 bytes (-8,388,608 to 8,388,607) or (0 to 16,777,215) unsigned
- `INT` or `INTEGER` - 4 bytes (-2,147,483,648 to 2,147,483,647) or (0 to 4,294,967,295) unsigned
- `BIGINT` - 8 bytes (-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807) or (0 to 18,446,744,073,709,551,615) unsigned
- `BIT(M)` - Bit-field type (M bits, 1-64)

### Fixed-Point Types
- `DECIMAL(M,D)` or `DEC(M,D)` - Exact fixed-point number (M=total digits, D=decimal places)
- `NUMERIC(M,D)` - Synonym for DECIMAL

### Floating-Point Types
- `FLOAT(M,D)` - Single-precision floating-point (approximate)
- `FLOAT(p)` - Floating-point (p=precision bits)
- `DOUBLE(M,D)` or `DOUBLE PRECISION(M,D)` - Double-precision floating-point
- `REAL(M,D)` - Synonym for DOUBLE (unless REAL_AS_FLOAT SQL mode enabled)

## Date and Time Types
- `DATE` - Date (YYYY-MM-DD)
- `TIME` - Time (HH:MM:SS)
- `DATETIME` - Date and time (YYYY-MM-DD HH:MM:SS)
- `TIMESTAMP` - Timestamp (YYYY-MM-DD HH:MM:SS, range 1970-2038, timezone-aware)
- `YEAR` - Year (4-digit or 2-digit format)

## String Types

### Character Strings
- `CHAR(M)` - Fixed-length string (0-255 chars)
- `VARCHAR(M)` - Variable-length string (0-65,535 chars)
- `BINARY(M)` - Fixed-length binary string
- `VARBINARY(M)` - Variable-length binary string

### Text Types
- `TINYTEXT` - String up to 255 characters
- `TEXT` - String up to 65,535 characters
- `MEDIUMTEXT` - String up to 16,777,215 characters
- `LONGTEXT` - String up to 4,294,967,295 characters

### Blob Types (Binary Large Objects)
- `TINYBLOB` - Binary data up to 255 bytes
- `BLOB` - Binary data up to 65,535 bytes
- `MEDIUMBLOB` - Binary data up to 16,777,215 bytes
- `LONGBLOB` - Binary data up to 4,294,967,295 bytes

## JSON Type
- `JSON` - JSON-formatted data (introduced in MySQL 5.7.8)

## Spatial Data Types
- `GEOMETRY` - Any spatial type
- `POINT` - A point in space
- `LINESTRING` - Curve with linear interpolation between points
- `POLYGON` - Polygon
- `MULTIPOINT` - Collection of points
- `MULTILINESTRING` - Collection of linestrings
- `MULTIPOLYGON` - Collection of polygons
- `GEOMETRYCOLLECTION` - Collection of geometries

## Enumeration and Set Types
- `ENUM('val1','val2',...)` - String object with single value from predefined list
- `SET('val1','val2',...)` - String object with zero or more values from predefined list