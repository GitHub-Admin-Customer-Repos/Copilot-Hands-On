-- Lets assume we have two tables: `target_table` and `source_table`. The `target_table` 
-- contains the current state of the data, and the `source_table` contains the new data 
-- that we want to merge into the `target_table`.

-- Schema:
CREATE TABLE target_table (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255),
    updated_at TIMESTAMP
);

CREATE TABLE source_table (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255),
    updated_at TIMESTAMP
);

-- create a `MERGE` statement that will:
-- 1. Update existing records in `target_table` if they exist in `source_table` and have different values.
-- 2. Insert new records into `target_table` if they do not exist.
-- 3. Delete records from `target_table` if they do not exist in `source_table`.

-- Solution:
MERGE INTO target_table AS target
USING source_table AS source
ON target.id = source.id
WHEN MATCHED AND (
    target.name <> source.name OR
    target.address <> source.address OR
    target.updated_at <> source.updated_at
) THEN
    UPDATE SET
        target.name = source.name,
        target.address = source.address,
        target.updated_at = source.updated_at
WHEN NOT MATCHED BY TARGET THEN
    INSERT (id, name, address, updated_at)
    VALUES (source.id, source.name, source.address, source.updated_at)
WHEN NOT MATCHED BY SOURCE THEN
    DELETE;


-- 1. **Matching Rows**:
   -- The `ON target.id = source.id` clause specifies the condition for matching rows between the `target_table` and `source_table`.

-- 2. **Update Operation**:
   -- The `WHEN MATCHED` clause checks if the rows exist in both tables and if any of the columns (`name`, `address`, `updated_at`) have different values.
   -- If the condition is met, the `UPDATE` operation updates the `target_table` with the values from the `source_table`.

-- 3. **Insert Operation**:
   -- The `WHEN NOT MATCHED BY TARGET` clause checks if the rows exist in the `source_table` but not in the `target_table`.
   -- If the condition is met, the `INSERT` operation adds the new rows to the `target_table`.

-- 4. **Delete Operation**:
   -- The `WHEN NOT MATCHED BY SOURCE` clause checks if the rows exist in the `target_table` but not in the `source_table`.
   -- If the condition is met, the `DELETE` operation removes the rows from the `target_table`.

-- This `MERGE` statement ensures that the `target_table` is synchronized with the `source_table`, handling updates, inserts, and deletes as needed.