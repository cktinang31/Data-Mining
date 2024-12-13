from linkedin_api import Linkedin
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments, pipeline
import json

api = Linkedin('kristineannecardosa32@gmail.com' , 'kristine031')

profile = input("Input your linkedin username:")

profile_data = (api.get_profile(profile))

print(json.dumps(profile_data, indent=2))

job_description = ""

if 'skills' in profile_data and len(profile_data['skills']) > 0:
    job_description = "\n".join(skill.get('name', "") for skill in profile_data['skills'])

print("Job description:")
print(job_description)

field_of_study = ""
if 'education' in profile_data and len(profile_data['education']) > 0:
    field_of_study = profile_data['education'][0].get('fieldOfStudy', "")

print("Field of study:")
print(field_of_study)

model_name = "facebook/bart-large-mnli"
model_revision = "c626438"

classifier = pipeline("zero-shot-classification", model=model_name, revision=model_revision)

possible_labels = ["Software Engineer", "Data Scientist", "Project Manager"]

res = classifier(job_description, possible_labels)

print("Classification results:")
for label, score in zip(res['labels'], res['scores']):
    print(f"{label}: {score:.4f}")
    
if field_of_study.lower() in job_description.lower():
    print(f"The job is not directly related to the field of study ({field_of_study}).")
else:
    print(f"The job is  related to the field of study ({field_of_study}).")