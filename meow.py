from flask import Flask, render_template, request, redirect, url_for
import os
import shutil
import pdf_to_csv
import shortlist_applicants 

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/applicants'
app.config['SHORTLISTED_FOLDER'] = 'static/uploads/shortlisted/'
# Step 1: Home page - Resume upload
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'resume' not in request.files:
            return 'No file part'
        files = request.files.getlist('resume')
        if files:
            for file in files:
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filepath)
            return redirect(url_for('job_form'))
    return render_template('index.html')

# Step 2: Job role & description input page
@app.route('/job', methods=['GET', 'POST'])
def job_form():
    if request.method == 'POST':
        job_role = request.form['job_role']
        job_desc = request.form['job_desc']
        job_description = job_role + "\n" + job_desc
        pdf_to_csv.create_csv()
        shortlisted_applicants = shortlist_applicants.shortlist_applicants(job_description)
        shortlisted_file_names = [i[1] for i in shortlisted_applicants]
        
        
        # Copy shortlisted files to the 'shortlisted' folder
        for fileID in shortlisted_file_names:
            print(f"{fileID}.pdf")
            source_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{fileID}.pdf")
            destination_path = os.path.join(app.config['SHORTLISTED_FOLDER'], f"{fileID}.pdf")
            shutil.copy(source_path, destination_path)  # Copy file to shortlisted folder
        
        return redirect(url_for('results', job_role=job_role, job_desc=job_desc))
    return render_template('job_form.html')

# Step 3: Display filtered resumes
@app.route('/results')
def results():
    job_role = request.args.get('job_role')
    job_desc = request.args.get('job_desc')

    # Implement your resume filtering logic here
    resumes = filter_resumes(job_role, job_desc)

    return render_template('results.html', resumes=resumes, job_role=job_role)

def filter_resumes(job_role, job_desc):
    # Placeholder function: Implement your filtering logic here
    # For simplicity, we return all uploaded resumes.
    resume_files = os.listdir(app.config['SHORTLISTED_FOLDER'])
    return resume_files

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)

