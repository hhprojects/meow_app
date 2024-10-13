import pandas as pd
import job_description_matching
import resume_matching

def csv_to_df():
    # Load your data (CSV file)
    applicant_file_path = 'static/datasets.csv'
    applicant_df = pd.read_csv(applicant_file_path)

    employee_file_path = 'static/employees.csv'
    employee_df = pd.read_csv(employee_file_path)
    
    return applicant_df, employee_df


def shortlist_applicants(job_description):
    jd_threshold=0.2
    resume_threshold=0.7
    
    applicant_df, employee_df = csv_to_df()
    
    # Compute similarity for each applicant compared to the job description first
    applicant_df['Cleaned_Text'] = applicant_df.Original_Text.apply(lambda x: job_description_matching.cleaning_resume(x))
    applicant_df['Similarity_Score'] = applicant_df['Cleaned_Text'].apply(
        lambda resume_text: job_description_matching.combined_similarity(resume_text, job_description)
    )
    applicant_df = applicant_df[applicant_df['Similarity_Score'] > jd_threshold]
    print(applicant_df)

    return resume_matching.matched_resumes(applicant_df, employee_df)
