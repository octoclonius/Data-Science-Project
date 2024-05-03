# Data Science Project - Team 15

## Authors
- Christian Northrup
- Jozef Porubcin

## Requirements
- 36 GiB of free disk space
- pip
- conda

## How to Run
1. Download the database file [here](https://www.kaggle.com/datasets/maltegrosse/8-m-spotify-tracks-genre-audio-features/download?datasetVersionNumber=1).
1. Extract `archive.zip` as `spotify.sqlite`.
1. Create and activate a conda environment, then run `conda install -c conda-forge --file requirements.yaml`.
1. Open and run `optimize_db.ipynb`. Wait for all of the cells to finish before closing the file. The print statements in the fourth cell provide progress feedback. This program might take around an hour to run.
1. Open and run `create_dataframe.ipynb`. Wait for all of the cells to finish before closing the file. This program takes much less time (less than half an hour) to finish compared to `optimize_db.ipynb`.

Now you can run `correlations.ipynb`, `visualization.ipynb`, `artist_regression.ipynb`, `artist_visualization.ipynb`, and `hgbm_regression.ipynb` to see their output.

## Notes
- `optimize_db.ipynb` copies the original tables and creates new tables with indexes by defining a primary key. It rejects data with any null values, so the resulting tables are defined in every column. Very few rows had missing data, so the resulting tables are still representative of the entire original database.
- `create_dataframe.ipynb` defaults to excluding tracks with a popularity score of 0. To generate the complete CSV with all tracks possible, set `MIN_POPULARITY` in the second cell to `0`. Be warned that this will nearly double the size of the resulting CSV file.