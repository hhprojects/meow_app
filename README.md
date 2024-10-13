# Problem Statement
## Theme 3: Future-Ready Workforce
In today’s fast-changing business environment, PSA is committed to building an empowered and diverse workforce, capable of thriving amid constant transformation. Some key focus areas are inclusive talent development, multi-generational workforce engagement, data-driven career pathways, human-centered performance management, and technology-driven initiatives that enhance well-being and promote equity and inclusion. 

We invite participants to create innovative, data and AI-driven solutions that help us foster a culture of continuous learning and belonging, supporting employees across all generations in the key areas. 
 
The aim is to enhance PSA's ability to nurture a highly engaged, diverse workforce, driving long-term success in the dynamic port and its ecosystem.


# Idea PORTential: Automated Resume to Job Matching
## Objective: Matching current employees within PSA with applicants applying for job roles in PSA, optimizing hiring and internal mobility. Promote internal mobility by matching existing employees to new opportunities based on their skill sets and growth potential.

## Methodology:
Using AI algorithms to parse resumes and identify relevant work experiences, skill sets, and qualifications. 
Automate the filtering process to recommend suitable candidates internally (for promotions and lateral moves) and externally (for new hires).
Compare these qualifications to current employees and applicants to filter applicants similar to current ones. The reason behind this is that we assume applicants should have enough or similar qualifications to be considered for hiring under PSA.
Furthermore using a similar matching algorithm, we will identify current employees that are recommended to be sent to courses.

## Technology used: 
AI Model: Pandas, NLP, Fuzzy
Frontend: HTML, CSS
Backend: PyFlask

## Feature 1: 
A web application that allows you to drop one folder containing all the applicants' resumes in a PDF format
Through keyword matching and threshold scores, our AI will identify applicants who have similar work experiences/skill sets to current employees.
Our AI will then rank and display resumes that are suitable or unsuitable for hiring 
## Feature 2:
HR can indicate certain skill sets they require their employees to have/learn for future development
Our AI will search through the employee database and find employees who do not have this skill
Our AI will search the web for courses that are similar or relevant to the skill sets indicated by HR

## How our solution solves the problem:
By automating the process of having to manually scan through hundreds of resumes, our AI helps to filter out the most relevant resumes for the required job role
Additionally, filtering the resumes results in a more accurate selection of potential candidates with less bias
Simplifies the process of upskilling employees
## Limitations:
Sample datasets used (found online), less accurate as compared to using sample resumes of employees from PSA
Hard to predict the future skills needed for the industry
