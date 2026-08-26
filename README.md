# Data Cleaning Master

A command-line data cleaning tool built in Python that takes a raw CSV or Excel dataset and returns a cleaned, analysis-ready file, along with a separate log of any duplicate records that were removed.

## What it does

- Accepts `.csv` or `.xlsx` files and validates the file path before processing
- Reports total rows and columns in the raw dataset
- Detects duplicate records, saves them to a separate `_duplicates.csv` file for review, then removes them from the working dataset
- Detects missing values and reports a per-column breakdown
- Handles missing values differently depending on data type:
  - Numeric columns (`int`, `float`) are filled with the column mean
  - Non-numeric columns have rows with missing values dropped
- Outputs a cleaned dataset as `{dataset_name}_Clean_data.csv`
- Prints progress at each stage so the user can follow what the script is doing to their data

## Usage

Run the script and provide the dataset path and a name to use for the output files:

```bash
python data_cleaning_master.py
```

You'll be prompted for:
- **Dataset path** — full or relative path to your `.csv` or `.xlsx` file
- **Dataset name** — used to name the output files (e.g. `jan_sales` produces `jan_sales_Clean_data.csv`)


## Requirements

- Python 3.x
- pandas
- numpy
- openpyxl (for `.xlsx` support)
- xlrd (for legacy Excel formats)

Install dependencies with:

```bash
pip install pandas numpy openpyxl xlrd
```

## Why I built this

I was cleaning the same kinds of datasets by hand across different projects, checking for duplicates, spotting missing values, deciding how to handle them, and I wanted a repeatable tool that could do the first pass automatically instead of rewriting the same pandas logic every time. It's built to be simple enough to hand to someone with a messy spreadsheet and no coding background.

## Possible next steps

- Support for additional file types (JSON, Parquet)
- Configurable missing-value strategy (median, mode, or custom fill instead of mean)
- A summary report (HTML or PDF) of what was cleaned and why

