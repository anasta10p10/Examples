import pandas as pd
import sqlite3

# connect to database, get necessary tables, make the approriate types for columns
con = sqlite3.connect("applications.db")

df_jobs = pd.read_sql_query("SELECT * from jobs", con)
df_jobs.id = df_jobs.id.astype("int64")
df_jobs.company_id = df_jobs.company_id.astype("int64")

df_applications = pd.read_sql_query("SELECT * from applications", con)
df_applications.id = df_applications.id.astype("int64")
df_applications.job_id = df_applications.job_id.astype("int64")
df_applications["created"] = pd.to_datetime(df_applications["created"])

df_companies = pd.read_json("companies.json")
# join the tables to get necssary columns
df_res = (
    df_companies.merge(df_jobs, how="left", left_on="id", right_on="company_id")[
        ["name", "id_y"]
    ]
    .rename(columns={"id_y": "job_id"})
    .merge(df_applications, how="left", on="job_id")[["name_x", "name_y", "created"]]
    .rename(columns={"name_x": "company_name", "name_y": "applicant_name"})
)
# group and find the latest applicant name
res = df_res.loc[df_res.groupby("company_name")["created"].idxmax()][
    ["company_name", "applicant_name"]
]
# print data by rows
for i, data in res.iterrows():
    print(f"{data['company_name']} - {data['applicant_name']}")
