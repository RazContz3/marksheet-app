import csv
import glob
import os

# Columns to keep (main details + basket subjects)
main_columns = [
    'No', 'Name', 'R/C   BU.', 'SINHALA', 'ENGLISH', 'MATHS', 'HISTORY', 'SCIENCE',
    'BI (BS/Civics/Tamil)', 'B2(A/D/EM/WM/Dr)', 'B3(IT/HSc/HE)', 'TOTAL', 'AVERAGE', 'POSITION'
]
basket_columns = [
    'BS', 'Civics', 'Tamil', 'Geography', 'Art', 'Dancing', 'E Music', 'W Music', 'Drama', 'E Lit.',
    'ICT', 'HSc', 'Media'
]
keep_columns = main_columns + basket_columns

input_folder = 'data/processed'
output_folder = 'data/processed'

# Find all clean CSV files
for file in glob.glob(os.path.join(input_folder, 'clean_*.csv')):
    output_file = os.path.join(output_folder, 'final_' + os.path.basename(file))
    with open(file, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        present_columns = [col for col in keep_columns if col in reader.fieldnames]
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=present_columns)
            writer.writeheader()
            for row in reader:
                if row['No'] and row['No'].isdigit():
                    subject_marks = [row.get(subj, '') for subj in ['SINHALA','ENGLISH','MATHS','HISTORY','SCIENCE','BI (BS/Civics/Tamil)','B2(A/D/EM/WM/Dr)','B3(IT/HSc/HE)']]
                    if any(mark not in ('', '0') for mark in subject_marks):
                        filtered_row = {col: row.get(col, '') for col in present_columns}
                        writer.writerow(filtered_row)
    print(f"Cleaned file written to {output_file}")
