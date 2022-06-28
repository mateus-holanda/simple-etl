# simple-etl
This is a simple ETL pipeline to extract data from a source, clean it and load it to a database.

<p align="center">
  <img alt="banner" src=".github/banner.jpg" width="100%">
</p>

## 🚀 Technologies

This project was developed with the help of the following technologies:

- Python
- SQLAlchemy
- Psycopg2
- PostgreSQL

## 💻 Project

The source can come from anywhere, but in this case it comes from 3 different URL's as shown in lines 5-7 at `./extract.py` file and as below. Can't guarantee they'll still be available at the time you are reading this, but the URL's content are also available inside the folder `./data`.

```python
source1 = "http://208.167.255.20:8080/primer/2022_01_03.json.txt"
source2 = "http://208.167.255.20:8080/primer/2022_01_04.json.txt"
source3 = "http://208.167.255.20:8080/primer/2022_01_05.json.txt"
```

If you notice, the format of the data is a Newline Delimited JSON (NDJSON), which is a bit different from the convencional JSON. You can see more about NDJSON [here](http://ndjson.org/).

The `./execute.py` script is the orchestrator of this ETL. Inside of it the `./extract.py`, `./transform.py` and `./load.py` scripts are called.

The engine and session for the database are found in `./common/base.py` and the relations in `./common/table.py`.

To run this project, inside the root folder you can simply type `python execute.py`.
