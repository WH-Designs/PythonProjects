""" This module includes the SearchEngine class.

Author:
Date:
"""

import lab_web_crawler.crawler_util as crawler_util


class SearchResult(object):
    """ This is a simple container class for storing search results

    Public Attributes:
       url -   A string containing the URL of an HTML document.
       title - A string containing the title of the HTML page.
    """

    # YOU SHOULD NOT NEED TO MODIFY THIS CLASS.

    def __init__(self, url, title):
        """ Initialize the search result object. """
        self.url = url
        self.title = title

    def __eq__(self, rhs):
        """ Overide the == operator.
        Search results are considered equal if they have the same url.
        """
        return type(self) == type(rhs) and self.url == rhs.url

    def __hash__(self):
        """ Return hash of search result. """
        return hash(self.url)

    def __str__(self):
        return f'{self.url} {self.title}'


class HTMLPage(object):
    """ This is a simple container class for storing search results

    Public Attributes:
       url -   A string containing the URL of an HTML document.
       title - A string containing the title of the HTML page.
    """

    # YOU SHOULD NOT NEED TO MODIFY THIS CLASS.

    def __init__(self, url, title, text):
        """ Initialize the search result object. """
        self.url = url
        self.title = title
        self.text = text

    def __eq__(self, rhs):
        """ Overide the == operator.
        Search results are considered equal if they have the same url.
        """
        return type(self) == type(rhs) and self.url == rhs.url

    def get_text(self):
        return self.text

    def get_title(self):
        return self.title

    def __hash__(self):
        """ Return hash of search result. """
        return hash(self.url)

    def __str__(self):
        return f'{self.url} {self.title} {self.text}'


class SearchEngine(object):
    """
    The SearchEngine class is responsible for crawling some collection
    of HTML documents and creating an index that maps from words in
    those documents to SearchResult objects containing URLs and page
    titles.  This class also provides a method for searching the index
    once it is created.
    """

    def __init__(self):
        """ Construct a SearchEngine.

        At the time of construction the index is empty.
        """
        # YOUR CODE HERE You will (at least) need someplace to store
        # the search index (I suggest a dictionary) and some way of
        # keeping track of which URLs have already been crawled (I
        # suggest a set).

        # pass is a do-nothing instruction. It's just here because
        # it is a syntax error in Python to have an empty code block.
        # Replace it with good code.
        self._index = dict()
        self._urls = list()

    def crawl(self, url, max_depth):
        """  Update the index by crawling a collection of HTML documents.

        The crawl begins at url and will visit all pages within max_depth links.
        For example, if max_depth = 0, only the document located at the
        indicated url is indexed. If max_depth = 2, the original document is
        indexed, along with all documents that it links to and all of the
        documents that THOSE documents link to.  This method tracks which URLs
        have already been visited so that no URL will be processed more than
        once.

        Arguments:
           url      -    A string containing a valid URL.  For example:
                        "https://people.wou.edu/~cordoval/index.html" or
                        "C:\\Users\\LPCordova\\somefile.html"
           max_depth -   The maximum crawl depth.  See explanation above.

         No return value.
        """
        # YOUR CODE HERE
        self._crawl_helper(url, 0, max_depth)

    def _crawl_helper(self, url, current_depth, max_depth):
        if current_depth == max_depth:
            return

        self._urls.append(url)
        grabber = crawler_util.HTMLGrabber(url, True)
        text = grabber.get_text()
        urls = grabber.get_links()
        title = grabber.get_title()

        html_page = HTMLPage(url, title, text)

        self._index[url] = html_page

        for item in urls:
            if item not in self._urls:
                self._crawl_helper(item, current_depth + 1, max_depth)

    def search(self, word):
        """  Return a list of SearchResult objects that match the given word.

        This function returns a (possibly empty) list of SearchResult
        objects.  Each object refers to a document that contains
        the indicated word.  The search is NOT case sensitive.

        This method will accept any string, but assumes that the string
        represents a single word.  Since the index only stores individual
        words, any strings with spaces or punctuation will necessarily
        have 0 hits.

        Arguments:
          word - A string to search for in the search engine index.

          Return: A list of SearchResult objects.  The order of the
                  objects in the list is not specified.
        """
        # YOUR CODE HERE.
        search_results = list()

        for url, html_page in self._index.items():
            if word in html_page.get_text():
                search_results.append(SearchResult(url, html_page.get_title()))
        return search_results


def main():
    url = input('Please enter url: ')
    max_depth = input('Please enter the maximum crawl depth: ')
    search_term = input('Please enter the search term or enter to quit: ')
    engine = SearchEngine()
    engine.crawl(url, max_depth)
    while search_term != '':
        search_results = engine.search(search_term)
        for search in search_results:
            print(search)
        search_term = input('Please enter the search term or enter to quit: ')


if __name__ == "__main__":
    # TESTING CODE HERE. IF YOU WANT IT.
    main()
