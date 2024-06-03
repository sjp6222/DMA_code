import os
import pandas as pd

def process_text_file(input_file, output_folder):
    try:
        # Read the text file, skipping the first 45 lines
        df = pd.read_csv(input_file, skiprows=53, delim_whitespace=True, header=None, encoding='utf-16-le')

        # Select the third and fourth columns
        selected_columns = df.iloc[:, [7, 6]]

        # Divide the fourth column by 100 using .loc to avoid the SettingWithCopyWarning
        selected_columns.loc[:, 7] /= 100

        # Create a new dataframe with the selected columns and rename them
        result_df = pd.DataFrame({
            'Strain': selected_columns[7],  # Fourth column (divided by 100)
            'Stress': selected_columns[6],  # Third column
        })

        # Get the base name of the input file
        base_name = os.path.splitext(os.path.basename(input_file))[0]

        # Save the result dataframe to a CSV file in the output folder
        output_path = os.path.join(output_folder, f'{base_name}_output.csv')
        result_df.to_csv(output_path, index=False)
    
    except pd.errors.ParserError as e:
        print(f"Error processing file {input_file}: {e}")

def process_text_files_in_folder(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Process each text file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.abspath(os.path.join(input_folder, filename))
            process_text_file(input_path, output_folder)


# Replace 'input_folder' and 'output_folder' with your actual input and output folder paths
input_folder = r'C:\Users\Public\OneDrive\NURP Project\S24 Review\35C\txt input'  # Add the correct path here
output_folder = r'C:\Users\Public\OneDrive\NURP Project\S24 Review\35C\csv output'  # Add the correct path here

process_text_files_in_folder(input_folder, output_folder)

