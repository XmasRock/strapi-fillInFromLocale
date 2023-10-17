# strapi-fillInFromLocale
strapi-fillInFromLocale is a Python script for Strapi (https://strapi.io/) to fill in the content of the Target locale with the content of the Source locale for a Content Type with the ID you are providing

# Install
Clone the repository
```
git clone https://github.com/XmasRock/strapi-fillInFromLocale.git
```

Install the python-dotenv library
```
pip install python-dotenv
```

Create your .env from .env.example
```
cp .env.example .env
```

From your Strapi instance create an API Token.
Modify your new `.env` file with 
```
STRAPI_URL_BASE=<YOUR STRAPI INSTANCE URL BASE ex.: https://strapi.mydomain.com/api>
STRAPI_API_KEY=<YOUR STRAPI API TOKEN ex.: 8d1a5d3db1e401802a206aa32f198be87a47931e2b0... >
```
# Use
Get help

```
python strapi-fillInFromLocale.py -h
```

Using the long options to copy the content of items for the Content Type **Article** with **ID=1** from **locale=fr** to fill in items of the **locale=en**  

```
python strapi-fillInFromLocale.py --contentType article --contentTypeId 1 --localeSource fr --localeTarget en
```

Same with short options

```
python strapi-fillInFromLocale.py -c article -i 1 -s fr -t en
```