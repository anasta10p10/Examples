import pandas as pd
import sqlite3

# connect to database, find for each company_id latest applicant name
con = sqlite3.connect("applications.db")

df_id = pd.read_sql_query(
    f"""
    SELECT company_id,name  as applicant_name
    FROM ( 
        SELECT company_id, a.name, row_number() over(partition by company_id order by created desc) as r 
        FROM jobs j inner join applications a 
        ON j.id = a.job_id
        ) t 
    WHERE r = 1""",
    con,
)

df_id.company_id = df_id.company_id.astype("int64")

df_companies = pd.read_json("companies.json")
# by company id find company name from json file
df_res = df_companies.merge(df_id, how="left", left_on="id", right_on="company_id")[
    ["name", "applicant_name"]
]
# print data by rows
for i, data in df_res.iterrows():
    print(f"{data['name']} - {data['applicant_name']}")
