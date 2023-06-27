import requests, os

from pythorhead import Lemmy

# Your own instance's domain
LEMMY_DOMAIN = os.environ.get('FEDISEER_INSTANCE')
USERNAME = os.environ.get('FEDISEER_USERNAME')
PASSWORD = os.environ.get('FEDISEER_PASSWORD')
ACTIVITY_SUSPICION = os.environ.get('ACTIVITY_SUSPICION')
MONTHLY_ACTIVITY_SUSPICION = os.environ.get('MONTHLY_ACTIVITY_SUSPICION')

## ToDo - make environment variable.
# Extra domains you can block. You can just delete the contents if you want to only block suspicious domains
blacklist = {
    "truthsocial.com",
    "exploding-heads.com",
    "lemmygrad.ml",
}


lemmy = Lemmy(f"https://{LEMMY_DOMAIN}")
if lemmy.log_in(USERNAME, PASSWORD) is False:
    raise Exception("Could not log in to lemmy")

print("Fetching suspicions")
sus = requests.get(f"https://fediseer.com/api/v1/instances?activity_suspicion={ACTIVITY_SUSPICION}&active_suspicion={MONTHLY_ACTIVITY_SUSPICION}&domains=true", timeout=5).json()
defed = blacklist | set(sus["domains"])
# I need to retrieve the site info because it seems if "RequireApplication" is set
# We need to always re-set the application_question. 
# So we retrieve it from the existing site, to set the same value
site = lemmy.site.get()
application_question = None
if site["site_view"]["local_site"]["registration_mode"] == "RequireApplication":
    application_question = site["site_view"]["local_site"]["application_question"]
print("Editing Defederation list")
if application_question:
    ret = lemmy.site.edit(
        blocked_instances=list(defed),
        application_question=application_question,
        )
else:
    ret = lemmy.site.edit(
        blocked_instances=list(defed),
        )
print("Edit Successful")
