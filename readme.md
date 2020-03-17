### reproducing

1) Download the new articles from https://www.kaggle.com/jeet2016/us-financial-news-articles
2) Setup ELK stack - docker-compose up -d
3) Run insert_documents.py with a path to extracted new articles' root path

### index docs

py .\insert_documents.py root_dir_for_recursive_reading

### save all docs to one file

py .\write_documents_into_one.py root_dir_for_recursive_reading output_file