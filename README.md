# Data Science Project - Team 15

## Authors
- Christian Northrup
- Jozef Porubcin

## Requirements
- 36 GiB of free disk space
- Python 3
- A bunch of Python libraries

## How to Run
1. Download the database file [here](https://www.kaggle.com/datasets/maltegrosse/8-m-spotify-tracks-genre-audio-features/download?datasetVersionNumber=1).
1. Extract `archive.zip`.
1. Open `optimize_db.ipynb`. In the second cell, set `PATH_DB` to the path of the extracted database file. Save the file, run all of the cells, and wait for them to finish before closing the file. The print statements in the fourth cell provide progress feedback.
1. Open `create_dataframe.ipynb`. In the second cell, set `PATH_DB` to the path of the extracted database file. Save the file, run all of the cells, and wait for them to finish before closing the file. This program takes much less time to finish compared to `optimize_db.ipynb`.
1. Open `correlations.ipynb` and `visualization.ipynb`. In the second cell, set `PATH_CSV` to the path of the CSV file generated from `create_dataframe.ipynb`.

Now you can run `correlations.ipynb` and `visualization.ipynb` to see their output.

## Notes
- `optimize_db.ipynb` copies the original tables and creates new tables with indexes by defining a primary key. It rejects data with any null values, so the resulting tables are defined in every column. Very few rows had missing data, so the resulting tables are still representative of the entire original database.
- `create_dataframe.ipynb` defaults to excluding tracks with a popularity score of 0. To generate the complete CSV with all tracks possible, set `MIN_POPULARITY` in the second cell to `0`. Be warned that this will nearly double the size of the resulting CSV file.