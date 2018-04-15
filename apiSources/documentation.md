### News API's to utilize:
#### News API
##### This api Queries a variety of news sources based off of passed parameters (subject, date, source, etc).
##### He Zhe ran into some trouble implementing certain calls from the backend, we may wish to attempt to make our calls from the front end (using AJAX) if that is easier. It'll ultimately depend on how we wish to further progress in our implementation.
* ##### [Python implementation utilizing python client library](https://newsapi.org/docs/client-libraries/python)
* ##### Endpoint - "everything":
* ##### Based off the "q" get request parameter, this api endpoint allows to search 30,000 news sources for theoretically any topic
* ##### [Everything Endpoint documentation](https://newsapi.org/docs/endpoints/everything)
* ##### Endpoint - "top headlines":
* ##### This endpoint returns the top headlines based off country requested.
* ##### Potentially useful for any analysis of trending topics
* [Top Headlines Endpoint Documentation](https://newsapi.org/docs/endpoints/top-headlines)
#### We may also wish to employ alternate news api's, these could be individual sources (NYtimes, WaPo, etc.), although that could get messy depending on if one was querying multiple sources at once(although not necessarily)
#### Additionally, there may be alternate news aggregate API's we can employ
#### At the very least, no matter what API's we employ, it's important that they provide article links, for searching and archiving purposes.
* #### [nytimes article search](https://developer.nytimes.com/article_search_v2.json#/README)
* #### [Google news api(another aggregate system)](https://newsapi.org/s/google-news-api)
* #### [List of sources available through newsapi](https://newsapi.org/sources)

##### Sources we will be using from list

1. New York Times (the-new-york-times)
2. BBC News (bbc-news)
3. CCN (ccn)
4. Fox News (fox-news)
5. Washington Post (the-washington-post)
6. Wall Street Journal (the-wallstreet-journal)
7. NBC News (nbc-news)
8. ESPN (espn)
9. CBS News (cbs-news)
10. ABC News (abc-news)

  * These can all be queried using the python api listed above.
  * the string in parentheses is the source parameter
