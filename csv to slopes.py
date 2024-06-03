# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np

def calculate_slope(x, y):
    # Fit a linear regression model to calculate the slope
    coefficients = np.polyfit(x, y, 1)
    slope = coefficients[0]
    return slope

def process_csv_file(file_path, x_column, y_column,):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Convert the columns to numeric types
    df[x_column] = pd.to_numeric(df[x_column], errors='coerce')
    df[y_column] = pd.to_numeric(df[y_column], errors='coerce')

    # Drop NaN values
    df = df.dropna()
    

    # Select data points between 0.75 and 1.0 x values
    mask = (df[x_column] >= 0.2) & (df[x_column] <= 0.45)
    x_values = df.loc[mask, x_column]
    y_values = df.loc[mask, y_column]

    # Calculate the slope
    slope = calculate_slope(x_values, y_values)

    return slope

def main(input_folder, output_file, x_column, y_column):
    # Create an empty list to store DataFrames
    dfs = []

    # Process each CSV file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_folder, filename)

            # Process the CSV file and calculate the slope
            slope = process_csv_file(file_path, x_column, y_column)

            # Append results to the list
            dfs.append(pd.DataFrame({"File Name": [filename], "Slope": [slope]}))

    # Concatenate all DataFrames into a single DataFrame
    result_df = pd.concat(dfs, ignore_index=True)

    # Write the results to a single CSV file
    result_df.to_csv(output_file, index=False)


if __name__ == "__main__":
    # Replace 'input_folder', 'output_file', 'x_column', and 'y_column' with your actual values
    input_folder = r'C:\Users\Public\OneDrive\NURP Project\S24 Review\35C\csv output'
    output_file = r'C:\Users\Public\OneDrive\NURP Project\S24 Review\35C\35_slopes.csv'
    x_column = "Strain"
    y_column = "Stress"

    main(input_folder, output_file, x_column, y_column)

