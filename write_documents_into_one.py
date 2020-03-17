import sys
import os
import json
import glob
from pathlib import Path
from pprint import pprint

root_dir = sys.argv[1]
result_file_path = sys.argv[2]

for path in glob.iglob(root_dir + '/**', recursive=True):
    filename = Path(path).name
    print('checking if should index: ' + filename)
    if filename.startswith('blogs') and filename.endswith('.json'):
        with open(result_file_path, "a") as myfile:
            try:
                file = open(path, 'r').read()
                myfile.writelines('{ "index" : { "_index" : "news_articles"} }\n')
                myfile.writelines(file + '\n')
            except:
                print("Error when reading " + filename)