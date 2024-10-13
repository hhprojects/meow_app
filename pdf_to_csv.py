import pdfplumber
import csv
import os
import re
import pandas as pd

input_folder = "static/uploads/applicants"
output_csv = "static/datasets.csv"

# Define categories and their associated roles
categories = {
    'Accountancy': r'\b(Accountant|Senior Accountant|Financial Accountant|Junior Accountant|Staff Accountant|Tax Accountant)\b',
    'Software Developer': r'\b(Front End Developer|Back End Developer|Full Stack Developer|Software Engineer|Web Developer)\b',
    'IT': r'\b(Technician|Manager|Coordinator|Specialist)\b',
    # Add more categories and roles as needed
}

# Function to extract specific sections from resume text
def extract_sections(text):
    sections = {
        'Category': '',
        'Role': '',  # New header for specific role
        'Summary': '',
        'Education': '',
        'GPA': '',  # New header for GPA
        'University': '',  # New header for University/School name
        'Skills': '',
        'Experience': '',
        'Certifications': '',
        'Other': '',  # For any text that doesn't fit other categories
        'Original_Text': text.lower()  # Store original text
    }

    # Regular expressions for each section
    patterns = {
        'Summary': r'(Summary|Objective|Professional Summary)',
        'Education': r'(Education|Academic Background)',
        'Skills': r'(Skills|Core Competencies|Technical Skills|Programming|Programming Languages)',
        'Experience': r'(Experience|Work Experience|Professional Experience)',
        'Certifications': r'(Certifications|Licenses|Accreditations)',
    }

    # Normalize the text for easier pattern matching
    text_lower = text.lower()

    # Track the last matched section
    current_section = 'Other'

    # Check for roles and assign the corresponding category and role
    for category, pattern in categories.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            sections['Category'] = category  # Assign category
            sections['Role'] = match.group(0)  # Capture specific role
            break

    # Split the text into lines and try to assign them to sections
    for line in text.split('\n'):
        line_lower = line.lower().strip()

        # Check if the line matches any section header
        matched_section = False
        for section, pattern in patterns.items():
            if re.search(pattern.lower(), line_lower):
                current_section = section
                matched_section = True
                break

        # If the line doesn't match a section, add it to the current section
        if not matched_section:
            sections[current_section] += line + ' '

    # Extract GPA and University/School from the education section
    if sections['Education']:
        gpa_match = re.search(r'\bGPA\s*[:=]?\s*([0-4]\.[0-9]{1,2})\b', sections['Education'], re.IGNORECASE)
        university_match = re.search(r'\b(?:University|College|Institute|School|Academy|Program|Programme)\b[^\n]*', sections['Education'], re.IGNORECASE)

        if gpa_match:
            sections['GPA'] = gpa_match.group(1)  # Extract GPA value
        if university_match:
            sections['University'] = university_match.group(0).strip()  # Extract University/School name

    return sections

def create_csv():
    # Open CSV file for writing
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Add headers for the CSV
        writer.writerow(['fileID', 'Category', 'Role', 'Summary', 'Education', 'GPA', 'University', 'Skills',
                        'Experience', 'Certifications', 'Other', 'Original_Text'])

        # Loop through all PDF files in the folder
        for filename in os.listdir(input_folder):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(input_folder, filename)

                print(f"Converting: {filename}")  # Print the name of the PDF being converted

                # Remove the .pdf extension from the filename for fileID
                file_id = os.path.splitext(filename)[0]

                # Open and process each PDF
                with pdfplumber.open(pdf_path) as pdf:
                    all_text = ""

                    # Extract text from all pages
                    for page in pdf.pages:
                        all_text += page.extract_text() + "\n"

                    # Replace problematic encodings
                    all_text = re.sub(r'[^\x00-\x7f]', r' ', all_text)  # Remove non-ASCII characters

                    # Extract sections from the resume
                    sections = extract_sections(all_text)

                    # Write the extracted sections to CSV
                    writer.writerow([file_id, sections['Category'], sections['Role'], sections['Summary'],
                                    sections['Education'], sections['GPA'], sections['University'],
                                    sections['Skills'], sections['Experience'], sections['Certifications'],
                                    sections['Other'], sections['Original_Text']])

    print(f"All PDF files from {input_folder} have been converted and saved to {output_csv}")