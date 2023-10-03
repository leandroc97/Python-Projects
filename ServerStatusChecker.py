import requests
 #The requests library allows to send HTTP requests

 #Storing the Website URLs in a readable list by assigning a list variable
website_url = [
    "https://walkingtourslisbon.com/", 
    "https://walkingtourslisbon.com/about/", 
    "https://walkingtourslisbon.com/services/", 
    "https://walkingtourslisbon.com/contact/",
]
  #Storing the HTTP response codes in a list

status = {
    200: "Website Available",
    301: "Permanent Redirect",
    302: "Temporary Redirect",
    404: "Not Found",
    500: "Internal Server Error",
    503: "Service Unavailable"
}
 #A loop to check each URL of the website and provide its HTTP response code
for url in website_url:
    try:
        web_response = requests.get(url)
        print(url, status[web_response.status_code])
 
    except:
        print(url, status[web_response.status_code])