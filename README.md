## This project is on hiatus. There is a new feed from 911 that I will tap into. I want to also rewrite this project in Node so I can implement client functions
# Bryx-Home
This project is to pull calls from the Bryx API from their website and turn on my smart bulbs and preform other actions to alert me to a fire call
### Requirements
- Requests
- PHue
- Selenium and associated drivers for firefox
- Json
- configparser
- pymongo

### INI Layout
[BRYX]  
token =   
username =   
password =   
  
[DATABASE]  
password =   
databasestring =   

[HUE]  
bridgeaddress = 

### Planned Upgrades
- Add the ability to turn off lights from a website
- Add the ability to parse multiple different departments
- Turn on and off alerting for different departments at will
- Add a view to see what the call information is
- Add support for other bulb types?

### Changelog
##### 1.0.0
- Changed urllib3 to use requests as it provides better output for me to parse
- Add the ability to pull the auth token from bryx directly so there is no involvement from me
- Change the way the hue bulbs connect so I know when I need to readd the bridge before a call comes in
- Add the ability to update calls after they come in so that in the future I an see all of the data
- Changed the way config loads so that I can save the new token I find
- Made sleep timer longer less overall database and api calls
- Break out database string into its own configuration

##### 0.1.0
- Connect to hue bulbs
- Save calls to a database
- Turn on bulb when a new call is found
##### 0.0.1
- Added the ability to pull calls from bryx
