import os
import json
from dotenv import load_dotenv

class AppSetting:
    def __init__(self, name, slotSetting, value):
        self.name = name
        self.slotSetting = slotSetting
        self.value = value

# Load the .env file
load_dotenv()

# Create an empty list to store the app settings
app_settings = []
env_file_path = './src/.env'
# Loop through the .env file and assign properties to the AppSetting class
with open(env_file_path, 'r') as file:
    for line in file:
        if line.strip() != '' and not line.startswith('#'):
            key, value = line.strip().split('=')
            slotSetting = False
            app_setting = AppSetting(key, slotSetting, value)
            app_settings.append(app_setting)

# Convert the app settings to JSON
app_settings_json = json.dumps([app_setting.__dict__ for app_setting in app_settings], indent=4)

# Write the JSON to a file
with open('appsetting.json', 'w') as file:
    file.write(app_settings_json)
