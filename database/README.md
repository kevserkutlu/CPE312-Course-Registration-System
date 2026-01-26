# 🗄️ Database

This folder contains the database schema and initialization data for the system.

### 📄 Files

* **`schema.sql`**: The main SQL script containing table creation (`CREATE TABLE`), relationship definitions (`FOREIGN KEY`), and constraints.
* **`data.sql` (Optional)**: Sample student, course, and instructor data for testing the system.

### 🛠️ Setup

You can prepare the database by running the SQL files in this folder using your chosen DBMS (e.g., PostgreSQL).

```sql
psql -U postgres -d course_registration -f schema.sql
```

