from fake_useragent import UserAgent
import json
import requests
from requests.adapters import HTTPAdapter
from rich import print




class UserCheck:

    def __init__(self, username):
        self.username = username


    def username_check(self):
        
        print(f"[bold white]Username:[/bold white] {self.username}")
        # Load all websites from sites.json file
        with open("sites.json", "r") as sites_file:
        
#           print(sites_file) # Verify that the function loads the sites correctly

            for line in sites_file:
                # LinkedIn will respond with a 999 status code if these headers are not included
                headers = {
                    'Accept': "text/html, application/xhtml+xml,application/xml;q=-0,image/webp,*/*;q=0.8",
                    'accept-encoding': "gzip, deflate, sdch, br",
                    'accept-language': "en-US,en;q=0.8,ms;q=06",
                    'User-Agent':str(UserAgent().random)}
               #print(headers) # Verify that the headers are being included correctly
                json_site = json.loads(line)

                # Verify the site lines are pulled in correctly
#               print(json_site['site'], type(json_site['urls']))
                try: 
                    for url in json_site['urls']:
                        for proto in ["http://", "https://"]:
                            link = proto + url + self.username
                            r = requests.get(link, headers=headers)
                            if r.status_code == 200:
                                print(f"[bold green]FOUND[/bold green] - [bold blue]{json_site['site']}[/bold blue] - [italic white]{link}[/italic white]")
                                break

                except requests.exceptions.Timeout as timeout_err:
                    print(f"Request timeout : {timeout_err}")
                except requests.exceptions.HTTPError as http_err:
                    print(f"HTTP error occurred: {http_err}")
                except requests.exceptions.RequestException as req_err:
                    print(f"Request Exception Error: {req_err}")