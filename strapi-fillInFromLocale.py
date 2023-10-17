
import requests
import json
import sys, getopt
import os
from dotenv import load_dotenv

load_dotenv()

urlBase = os.getenv("STRAPI_URL_BASE")
token = os.getenv("STRAPI_API_KEY")

# ---------------
# --- duplicate 
# ---------------
def fillInFromSource(contentType, id, source, target):
    url = urlBase +"/"+contentType+"s/"+id
    print(url)
    parameters = {"locale" : source, "populate" : "*"}
    headers = {"Authorization": "Bearer "+token}
    reponse = requests.get(url,params=parameters, headers=headers)
    data = reponse.json()
    print(json.dumps(data,indent=4))

    # --- manipulate the data
    data["data"]["attributes"]["locale"]=target
    del data["data"]["attributes"]["createdAt"]
    del data["data"]["attributes"]["updatedAt"]
    del data["data"]["attributes"]["publishedAt"]
    # --- create the same data for new locale
    url = urlBase +"/"+contentType+"s/"+id+"/localizations"
    reponse = requests.post(url,headers=headers,json=data["data"]["attributes"])
    print(json.dumps(reponse.json(),indent=4))


    
############
# --- MAIN
############

def main(argv):
    opts, args = getopt.getopt(argv,"hc:i:s:t:",["contentType=","contentTypeId=","localeSource=","localeTarget="])
    for opt, arg in opts:
        if opt == '-h':
            print ('''
                   strapi-fillInFromLocale is a Python script for Strapi (https://strapi.io/) to fill in the content of the Target locale with the content of the Source locale 
                   for a Content Type with the ID you are providing
                   python strapi-fillInFromLocale.py --contentType (or -c) <contentType> --contentTypeId (or -i) <id> --localeSource (or -s) <locale> --localeTarget (or -t) <locale>
                        ex1: python strapi-fillInFromLocale.py --contentType article --contentTypeId 1 --localeSource fr --localeTarget en 
                        ex2: python strapi-fillInFromLocale.py -c article -i 1 -s fr -t en ''')
            sys.exit()
        elif opt in ("-c", "--contentType"):
            contentType = arg
        elif opt in ("-i", "--contentTypeId"):
            id = arg
        elif opt in ("-s", "--localeSource"):
            source = arg
        elif opt in ("-t", "--localeTarget"):
            target = arg
        else:
            print("Error: unknown option "+opt)
            sys.exit(1)

    fillInFromSource(contentType, id, source, target)
    
   
###############
# --- bootstrap to run as a script
###############
if __name__ == "__main__":
   main(sys.argv[1:])
