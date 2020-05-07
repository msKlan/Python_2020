# import NotFoundException      #kunne ikke finde denne exception
import pandas as pd
import requests



class my_iter_module():
    def __init__(self, url_list):
        self.url_list = url_list

    def download(self, url, filename):
        # raises NotFoundException when url returns 404
        if requests.head(url) == 404:
            raise '404 not found'
            # raise NotFoundException()
        else:
            df = pd.DataFrame(url)
            df.to_csv(filename)
        return 'File succesfully downloaded'
        # re = requests.get(url)

    def multi_download(self, url_list):
        # uses threads to download multiple urls as text and stores filenames as a property
        pass

    def __iter__(self):
        # returns an iterator
        return self

    def __next__(self):

        # returns the next filename (and stops when there are no more)
        pass

    def urllist_generator(self):
        # returns a generator to loop through the urls
        for url in self.url_list:
            yield url

    def avg_vowels(self, text):
        # a rough estimate on readability returns average number of vowels in the words of the text
        pass

    def hardest_read(self):
        # returns the filename of the text with the highest vowel score (use all the cpu cores on the computer for this work.
        pass
