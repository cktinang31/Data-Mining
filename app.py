from linkedin_api import Linkedin
from transformers import pipeline
from transformers import AutoTokenizer
import json

api = Linkedin('kristineannecardosa32@gmail.com' , 'kristine031')

profile = input("Input your linkedin username:")

profile_data = (api.get_profile(profile))

print(json.dumps(profile_data, indent=2))

# classifier = pipeline("")

# res = classifier("", profile)

# print(res)