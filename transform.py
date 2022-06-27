import csv
import ndjson
import pandas as pd
from common.table import Users
from common.base import session
from common.table import Users


def filter_data_by_revision(path):
  print(f"[Transform] Filtering data from {path}...")

  with open(path) as f:
    data = ndjson.load(f)

  df = pd.DataFrame()

  for i in range(0, len(data)):
    df = df.append({
      "version": data[i]["version"],
      "first_name": data[i]["record"]["field_group_one"]["first_name"],
      "last_name": data[i]["record"]["field_group_one"]["last_name"],
      "email": data[i]["record"]["field_group_one"]["email"],
      "days_since_hired": data[i]["record"]["field_group_two"]["days_since_hired"],
      "car": data[i]["record"]["field_group_two"]["car"],
      "dept": data[i]["record"]["field_group_two"]["dept"]
    }, ignore_index=True)

  # Get only most recent version input
  df_groupby = df.groupby("email").version.transform(max)
  df = df.loc[df.version == df_groupby]

  # Create a CSV file with the most recent inputs
  df.to_csv(path.split(".")[0] + ".csv", index=False)

  print(f"[Transform] Added transformed data from {path} to a CSV file.")


def transform_new_data(path):
  print(f"[Transform] Table from {path}...")

  with open(path, mode="r") as csv_file:
    # Read the new CSV ready to be processed
    reader = csv.DictReader(csv_file)

    # Initialize an empty list for our objects
    objects = []

    for row in reader:
      # Apply transformations and save as table object
      objects.append(
        Users(
          first_name = row["first_name"],
          last_name = row["last_name"],
          email = row["email"],
          days_since_hired = row["days_since_hired"],
          car = row["car"],
          dept = row["dept"]
        )
      )

    # Save all new processed objects and commit
    session.bulk_save_objects(objects)
    session.commit()
    print("[Transform] Done!")


def main():
  print("[Transform] Start")

  filter_data_by_revision("/data/source1.ndjson")
  transform_new_data("/data/source1.csv")

  filter_data_by_revision("/data/source2.ndjson")
  transform_new_data("/data/source2.csv")

  filter_data_by_revision("/data/source3.ndjson")
  transform_new_data("/data/source3.csv")