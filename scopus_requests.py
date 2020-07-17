#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from os import path
import json, requests, urllib

config_filename = "config.secret.json" if path.exists("config.secret.json") else "config.json"
config = json.load(open(config_filename))
con_file.close()
print(config['apikey'])


# In[ ]:


# search in each of the journals by ISSN, for "machine learning" in title/abstract/keywords:
issns = ["00218561"]
all_results = {}
for issn in issns:
    plain_query = "TITLE-ABS-KEY(\"machine learning\") AND ISSN({0})".format(issn)
    query_str = urllib.parse.urlencode({"query": plain_query, "apiKey": config['apikey'] })
    url_str = "https://api.elsevier.com/content/search/scopus?{0}".format(query_str)
    #print(url_str)
    r = requests.get(url_str)
    #print(r.status_code)
    #print(r.json())
    all_results.update({issn: r.json()})

print(all_results)

