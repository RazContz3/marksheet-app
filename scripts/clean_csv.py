import csv

# Columns to keep (main details + basket subjects)
main_columns = [
    'No', 'Name', 'R/C   BU.', 'SINHALA', 'ENGLISH', 'MATHS', 'HISTORY', 'SCIENCE',
    'BI (BS/Civics/Tamil)', 'B2(A/D/EM/WM/Dr)', 'B3(IT/HSc/HE)', 'TOTAL', 'AVERAGE', 'POSITION'
]
basket_columns = [
    'BS', 'Civics', 'Tamil', 'Geography', 'Art', 'Dancing', 'E Music', 'W Music', 'Drama', 'E Lit.',
    'ICT', 'HSc', 'Media'
]
# Some basket columns may be empty, so we will keep them if present
keep_columns = main_columns + basket_columns

input_file = 'data/processed/clean_10S1_Marks_Sheet_2025.csv'
output_file = 'data/processed/final_10S1_Marks_Sheet_2025.csv'

with open(input_file, newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    # Find which columns are present
    present_columns = [col for col in keep_columns if col in reader.fieldnames]
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=present_columns)
        writer.writeheader()
        for row in reader:
                # Only keep rows with a valid student number and at least one non-zero mark
                if row['No'] and row['No'].isdigit():
                    # Check if at least one subject mark is non-zero
                    subject_marks = [row.get(subj, '') for subj in ['SINHALA','ENGLISH','MATHS','HISTORY','SCIENCE','BI (BS/Civics/Tamil)','B2(A/D/EM/WM/Dr)','B3(IT/HSc/HE)']]
                    if any(mark not in ('', '0') for mark in subject_marks):
                        filtered_row = {col: row.get(col, '') for col in present_columns}
                        writer.writerow(filtered_row)
print(f"Cleaned file written to {output_file}")
