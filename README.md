# NACE Source Analysis Tool

This tool automatically classifies sources by NACE codes, evaluates trustworthiness and risk scores, and allows manual or automated data entry.

## Features

- Web article scraping and analysis
- Trust and risk scoring
- Automated NACE prediction via ML model
- Excel import & export
- Manual entry and live monitoring
- Full GUI via Tkinter
- Scrollable table with sorting
- README viewer button (this!)

## How to Use

1. **Train the model:**
   Run `training_nace.py` with your labeled training data (`training_data.csv`).

2. **Run the app:**
   Execute your main Python file (`Digitale Transformation.ipynb` or converted `.py` file).

3. **Analyze data:**
   - Load Excel file (`.xlsx`)
   - Or use the **"Analyze Web Article"** button
   - Or enter manually in the form

4. **Results:**
   Data is saved in `nace_source_evaluation.xlsx`.

## Requirements

- Python 3.9+
- Required libraries:  
  `pandas`, `tkinter`, `sklearn`, `newspaper3k`, `beautifulsoup4`, `requests`, `joblib`, `watchdog`

## Install with:

pip install pandas newspaper3k beautifulsoup4 requests scikit-learn watchdog

## Folder Structure

models/               → Trained model files (.pkl)
incoming_sources/     → Folder watched for new Excel files
processed/            → Archive of processed Excel files
training_data.csv     → Labeled NACE training data
training_nace.py      → Script to train the classifier
README.md             → This instruction file

