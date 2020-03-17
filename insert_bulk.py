import sys
import json
import glob
from pathlib import Path    
from pprint import pprint
from elasticsearch import Elasticsearch

root_dir = sys.argv[1]
elastic_client = Elasticsearch(['localhost'], port=9200)

with open(root_dir) as json_file:
    json_docs = json.load(json_file)
    elastic_client.bulk('news_articles', 'Blog', json_docs)
