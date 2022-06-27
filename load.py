from common.base import session
from common.table import Users
from sqlalchemy.dialects.postgresql import insert

def insert_new_users_into_psql_db():

  users_to_insert = session.query(
    Users.first_name,
    Users.last_name,
    Users.email,
    Users.days_since_hired,
    Users.car,
    Users.dept
  )

  print("[Load] Number of users to insert: ", users_to_insert.count())

  stm = insert(Users).from_select(
      ["first_name", "last_name", "email", "days_since_hired", "car", "dept"],
      users_to_insert,
  )

  # Execute and commit the statement to make changes in the database.
  session.execute(stm)
  session.commit()

  print("[Load] Complete!")


def insert_new_users_into_bigquery(df):
  from google.cloud import bigquery

  PROJECT_NAME = 'test_project'
  DATASET_NAME = 'test_dataset'
  TABLE_NAME = 'test_table'

  bq_client = bigquery.Client(project=PROJECT_NAME)

  job_config = bigquery.LoadJobConfig(
    schema=[
      bigquery.SchemaField(name="first_name", field_type="STRING", mode="NULLABLE"),
      bigquery.SchemaField(name="last_name", field_type="STRING", mode="NULLABLE"),
      bigquery.SchemaField(name="email", field_type="STRING", mode="REQUIRED"),
      bigquery.SchemaField(name="days_since_hired", field_type="INTEGER", mode="NULLABLE"),
      bigquery.SchemaField(name="car", field_type="STRING", mode="NULLABLE"),
      bigquery.SchemaField(name="dept", field_type="STRING", mode="NULLABLE")
    ]
  )

  job_config.source_format = bigquery.SourceFormat.CSV
  job_config.skip_leading_rows=0
  dataset_ref = bq_client.dataset(DATASET_NAME)

  load_job = bq_client.load_table_from_dataframe(
    df,
    dataset_ref.table(TABLE_NAME),
    job_config=job_config
  )

  load_job.result()

  print(f"Table '{TABLE_NAME}' updated!")


def main():
  print("[Load] Start")
  print("[Load] Inserting new rows into Users table")
  insert_new_users_into_psql_db()
  print("[Load] End")

  ### This is a function for uploading data into Google Cloud BigQuery, if needed
  #insert_new_users_into_bigquery()