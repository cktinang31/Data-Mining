from linkedin_api import Linkedin

api=Linkedin('kristineannecardosa32@gmail.com' , 'kristine031')

profile=input("Input your linkedin username:")

print(api.get_profile(profile))