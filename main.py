# user defined class
from crawl import crawl_job
from indexer import indexer

# built-in libraries
import nltk

# Download the NLTK stop words if needed
nltk.download('stopwords')
nltk.download('punkt')

# seed url to start crawling with
seed_urls = ["https://en.wikipedia.org/wiki/Google_File_System"]

# create a crawler, pro
crawl = crawl_job.CrawlJob(seed_urls)
# run crawler on seeds
documents = crawl.start_crawl_job()

# creating indexer instance
indexer_worker = indexer.Indexer(documents)
# running indexer
forward_index = indexer_worker.run_indexer()
# getting anchor link list from indexer
anchor = indexer_worker.get_anchor()

print(f"anchor: {anchor}")

print(f"forward_index: {forward_index}")

# URL Resolver
