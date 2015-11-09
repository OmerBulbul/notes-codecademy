Queries
=======

Queries
-------

Learn the most commonly used SQL commands to query a table in a database.

<div id='top'/>

Table of Contents
-----------------

- [Queries](#toc1)
- [Select-II](#toc2)
- [Select Distinct](#toc3)
- [Where](#toc4)
- [Like-I](#toc5)
- [Like-II](#toc6)
- [Between](#toc7)
- [And](#toc8)
- [Or](#toc9)
- [Order By](#toc10)
- [Limit](#toc11)
- [Generalizations](#toc12)

<div id='toc1'/>

Queries
-------

[[Back to Top]](#top)

### Learn

In this lesson you will be learning different SQL commands to query a single table in a database.

One of the core purposes of the SQL language is to retrieve information stored in a database. This is commonly referred to as querying. Queries allow us to communicate with the database by asking questions and having the result set return data relevant to the question. In this lesson, you will be querying a database with one table named `movies`. Let's get started.

### Instructions

1. Let's take a look at the `name` and `imdb_rating` of every movie in the database.

In the code editor type

```sql
SELECT name, imdb_rating FROM movies;
```

<div id='toc2'/>

Select-II
---------

[[Back to Top]](#top)

### Learn

```sql
SELECT name, imdb_rating FROM movies;
```

In Lesson 1 you learned that `SELECT` is used every time you want to query data from a database.

Multiple columns can be queried at once by separating column names with a comma. By specifying `name`, `imdb_rating`, the result set contains a `name` and `imdb_rating` column.

### Instructions

1. Let's continue with the `SELECT` statement. In the code editor, type

```sql
SELECT DISTINCT genre FROM movies;
```

Did you notice anything about the output?

<div id='toc3'/>

Select Distinct
---------------

[[Back to Top]](#top)

### Learn

```sql
SELECT DISTINCT genre FROM movies;
```

`SELECT DISTINCT` is used to return unique values in the result set. It filters out all duplicate values. Here, the result set lists each genre in the `movies` table exactly once.

1. `SELECT DISTINCT` specifies that the statement is going to be a query that returns unique values in the specified column(s)

2. `genre` is the name of the column to display in the result set.

3. `FROM movies` indicates the table name to query from.

Filtering the results of a query is an important skill in SQL. It is easier to see the different possible genres a movie can have after the data has been filtered, than to scan every row in the table.

The rest of this lesson will teach you different commands in SQL to filter the results of a query.

### Instructions

1. The way to filter queries in SQL is to use the WHERE clause. In the code editor type

```sql
  SELECT * FROM movies WHERE imdb_rating > 8;
```

<div id='toc4'/>

Where
-----

[[Back to Top]](#top)

### Learn

```sql
SELECT * FROM movies
  WHERE imdb_rating > 8;
```

This statement filters the result set to only include movies with IMDb ratings greater than 8. How does it work?

1. `WHERE` is a clause that indicates you want to filter the result set to include only rows where the following *condition* is true.

2. `imdb_rating > 8` is a condition that filters the result set. Here, only rows with a value greater than 8 in the `imdb_rating` column will be returned in the result set.

3. `>` is an *operator*. Operators create a condition that can be evaluated as either true or false. Common operators used with the `WHERE` clause are:
    - `=` equals
    - `!=` not equals
    - `>` greater than
    - `<` less than
    - `>=` greater than or equal to
    - `<=` less than or equal to

There are also some special operators that we will learn more about in the upcoming exercises.

### Instructions

1. `LIKE` is a special operator that can be used in a `WHERE` clause. In the code editor type

```sql
SELECT * FROM movies
WHERE name LIKE 'Se_en';
```

<div id='toc5'/>

Like-I
------

[[Back to Top]](#top)

```sql
SELECT * FROM movies
WHERE name LIKE 'Se_en';
```

`LIKE` can be a useful operator when you want to compare similar values. Here, we are comparing two movies with the same name but are spelled differently.

1. `LIKE` is a special operator used with the `WHERE` clause to search for a specific pattern in a column.
2. `name LIKE Se_en` is a condition evaluating the `name` column for a specific pattern.
3. `Se_en` represents a pattern with a wildcard character. The `_` means you can substitute any individual character here without breaking the pattern. The names k and `Se7en` both match this pattern.

`%` is another wildcard character that can be used with `LIKE`. We will learn more about `%` in the next exercise.

### Instructions

1. Let's use `LIKE` to query a few other patterns. In the code editor type

    ```sql
    SELECT * FROM movies
    WHERE name LIKE 'a%';
    ```

2. Remove the previous query. Then type

    ```sql
    SELECT * FROM movies
    WHERE name LIKE '%man%';
    ```

    What do you think `%` is doing?

<div id='toc6'/>

Like-II
-------

[[Back to Top]](#top)

<div id='toc7'/>

Between
-------

[[Back to Top]](#top)

<div id='toc8'/>

And
---

[[Back to Top]](#top)

<div id='toc9'/>

Or
--

[[Back to Top]](#top)

<div id='toc10'/>

Order By
--------

[[Back to Top]](#top)

<div id='toc11'/>

Limit
-----

[[Back to Top]](#top)

<div id='toc12'/>

Generalizations
---------------

[[Back to Top]](#top)




Writing Queries
---------------

Practice writing the most common types of queries.
