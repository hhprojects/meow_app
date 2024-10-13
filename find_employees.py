import pandas as pd
from fuzzywuzzy import fuzz

def employee_csv_to_df():
    employee_file_path = 'static/employees.csv'
    employee_df = pd.read_csv(employee_file_path)
    
    return employee_df

def check_missing_skills(query, threshold=90):
    employee_df = employee_csv_to_df()
    missing_skill_employees = []

    # Loop through each row in the employee dataframe
    for index, row in employee_df.iterrows():
        resume_text = row['Original_Text']  # Assuming the resume text is in a column called 'Text'
        file_id = row['fileID']    # Assuming the employee's fileID is in a column called 'fileID'
        
        # Perform fuzzy matching between the query and the employee's resume text
        similarity_score = fuzz.token_set_ratio(query, resume_text)
        
        # Check if the similarity score is below the threshold
        if similarity_score < threshold:
            missing_skill_employees.append(str(file_id)+".pdf")
    
    return missing_skill_employees
