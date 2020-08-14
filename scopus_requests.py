#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from os import path
import json, requests, urllib

config_filename = "config.secret.json" if path.exists("config.secret.json") else "config.json"
config_file = open(config_filename)
config = json.load(open(config_filename))
config_file.close()
#print(config['apikey'])


# In[ ]:


headers = {"X-ELS-APIKey": config["apikey"]}
# some query parameters require an insttoken, which must be requested from Elsevier
if len(config["insttoken"]) > 0:
    headers["X-ELS-Insttoken"] = config["insttoken"]

# search in each of the journals by ISSN, for "machine learning" in title/abstract/keywords:
issns = ["00218561"]
all_results = {}
for issn in issns:
    search_string = "TITLE-ABS-KEY(\"machine learning\") AND ISSN({0})".format(issn)
    query_params = {"query": search_string}
    #query_params["view"] = "COMPLETE" # add more query params here
    query_str = urllib.parse.urlencode(query_params)
    url_str = "https://api.elsevier.com/content/search/scopus?{0}".format(query_str)
    #print(url_str)
    
    r = requests.get(url_str, headers=headers)
    #print(r.status_code)
    #print(r.json())
    all_results.update({issn: r.json()})

print(all_results)

# save all_results as a JSON file:
#with open('results.json', 'w') as outfile:
#    json.dump(all_results.json(), outfile)

