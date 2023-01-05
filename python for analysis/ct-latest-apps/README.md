## Latest applications

#### Data

List of companies is provided in `companies.json`.
Job openings and applications are located in the [SQLite](https://docs.python.org/3/library/sqlite3.html) database `applications.db` (tables `jobs` and `applications`).


#### Task

Please provide a Python script which extracts latest application names for each of the company.
Note: test data has a small sample size, please implement a script which could cope with large amount of data in a SQL database.

#### Output

Script should print out each company record in a new line, company and applicant name separated with a dash (`-`). Example:

```
> Ikea - John Smith
> Deutsche Bahn - Max Mustermann
```
