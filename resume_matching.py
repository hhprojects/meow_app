from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Function to compute cosine similarity between applicant and employee resumes
def compute_similarity(applicant, employee, weights):
    exp_similarity = util.cos_sim(model.encode(str(applicant['Experience'])), model.encode(str(employee['Experience']))).item()
    skill_similarity = util.cos_sim(model.encode(str(applicant['Skills'])), model.encode(str(employee['Skills']))).item()
    edu_similarity = util.cos_sim(model.encode(str(applicant['Education'])), model.encode(str(employee['Education']))).item()

    # Weighted average
    overall_similarity = (weights['experience'] * exp_similarity +
                          weights['skills'] * skill_similarity +
                          weights['education'] * edu_similarity)
    return overall_similarity


def matched_resumes(applicant_df, employee_df):
    
    # Extract relevant columns for applicants and employees
    applicant_experience = applicant_df['Experience'].fillna('').astype(str)
    applicant_skills = applicant_df['Skills'].fillna('').astype(str)
    applicant_education = applicant_df['Education'].fillna('').astype(str)

    employee_experience = employee_df['Experience'].fillna('').astype(str)
    employee_skills = employee_df['Skills'].fillna('').astype(str)
    employee_education = employee_df['Education'].fillna('').astype(str)
    
    # Weights
    weights = {
        'experience': 0.5,
        'skills': 0.3,
        'education': 0.2
    }

    # Compute similarity for each applicant compared to each employee
    similarity_scores = []
    threshold = 0.6

    for i, applicant in applicant_df.iterrows():
        max_similarity = 0
        for j in range(len(employee_experience)):  # Compare with every employee
            employee = {'Experience': employee_experience[j],
                        'Skills': employee_skills[j],
                        'Education': employee_education[j]}

            # Calculate similarity between applicant and current employee
            similarity_score = compute_similarity(applicant, employee, weights)

            # Track the highest similarity score
            if similarity_score > max_similarity:
                max_similarity = similarity_score

        # If the highest similarity score exceeds the threshold, add to the result
        if max_similarity > threshold:
            fileID = applicant['fileID']  # Ensure 'fileID' exists in applicant_df
            similarity_scores.append((i, fileID, max_similarity))

    # Rank and sort the results by similarity score
    ranked_resumes = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Output ranked resumes with their row number and similarity score
    for row_num, fileID, score in ranked_resumes:
        print(f"Row: {row_num}, FileID: {fileID}, Highest Similarity Score: {score}")
        
    return ranked_resumes