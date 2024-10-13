import textacy
import textacy.preprocessing as tp
import spacy
from fuzzywuzzy import fuzz
import re

nlp = spacy.load("en_core_web_sm")

def cleaning_resume(resumes):

    # remove /n
    resumes = resumes.replace('\n', ' ')

    # convert all to lower case
    resumes = resumes.lower()

    # clean ascii special characters
    resumes = resumes.encode(encoding="ascii", errors="ignore").decode()
    
    # remove urls
    resumes = re.sub(r"(@\[A-Za-z0-9 ]+)|(\w+:\/\/\S+)|^rt|http.+?", " ", resumes)

    # remove special characters and keep space
    resumes = re.sub("[.'!#$%&\'()*+,-./:;<=>?@[\\]^ `{|}~]"," ", resumes)

    # remove extra white spaces
    resumes = re.sub('\s+', ' ', resumes)

    # Return the cleaned text
    return resumes


def clean_job_description(text):
    text = text.lower()
    return text

def calculate_vector_similarity(resume_text, job_description):
    resume_doc = nlp(resume_text)
    job_doc = nlp(clean_job_description(job_description))
    return resume_doc.similarity(job_doc)

def combined_similarity(resume_text, job_description):
    fuzzy_score = fuzz.token_set_ratio(clean_job_description(job_description), resume_text)
    vector_score = calculate_vector_similarity(resume_text, job_description)
    return ((fuzzy_score * 0.5) + (vector_score * 0.5))/100