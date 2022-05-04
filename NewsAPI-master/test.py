import unittest
from run import NewsApiClient

class TestNewsApiClient(unittest.loader):

   newsapi = NewsApiClient(api_key="1111f8f3bf334cc6a0af77fa30f68e29")

   top_headlines = newsapi.get_top_headlines(sources= "bbc-news" )

   all_articles = newsapi.get_everything(sources="bbc-news")




if __name__ == '__main__':
    unittest.main()