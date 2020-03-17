import sys
import json
import glob
from pathlib import Path    
from pprint import pprint
from elasticsearch import Elasticsearch

root_dir = sys.argv[1]

elastic_client = Elasticsearch(['localhost'], port=9200)

for path in glob.iglob(root_dir +'/**', recursive=True):
    filename = Path(path).name
    print('checking if should index: ' + filename)
    if (filename.startswith('blogs') or filename.startswith('news')) and filename.endswith('.json'):
        try:
            print('indexing: ' + path)
            file = open(path, 'r').read()
            elastic_client.index(index='news_articles', doc_type='Blog', body=file)
        except:
            print("Error when indexing: " + filename)
