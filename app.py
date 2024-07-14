import re
from linkedin_api import Linkedin

def print_profile(profile):
    print("Profile Details:")
    print("================")
    print(f"Name: {profile.get('firstName')} {profile.get('lastName')}")
    print(f"Headline: {profile.get('headline')}")
    print(f"Location: {profile.get('locationName')}")
    print(f"Industry: {profile.get('industryName')}")
    
    print("\nExperience:")
    for experience in profile.get('experience', []):
        print("---------------------")
        print(f"Title: {experience.get('title')}")
        print(f"Company: {experience.get('companyName')}")
        print(f"Location: {experience.get('locationName')}")
        print(f"Description: {experience.get('description')}")
    
    print("\nEducation:")
    for education in profile.get('education', []):
        print("---------------------")
        print(f"School: {education.get('schoolName')}")
        print(f"Degree: {education.get('degreeName')}")
        print(f"Field of Study: {education.get('fieldOfStudy')}")
        print(f"Start Date: {education.get('timePeriod', {}).get('startDate', {}).get('year')}")
        print(f"End Date: {education.get('timePeriod', {}).get('endDate', {}).get('year')}")
    
    print("\nSkills:")
    for skill in profile.get('skills', []):
        print(f"- {skill.get('name')}")

# Authenticate using LinkedIn credentials
api = Linkedin('kristineannecardosa32@gmail.com', 'kristine031')

# Get the LinkedIn username from the user
profile_username = input("Input LinkedIn username: ")

# Fetch the LinkedIn profile for the provided username
profile = api.get_profile(profile_username)

# Print the structured profile
print_profile(profile)