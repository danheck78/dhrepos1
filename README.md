This repository contains three demonstrations of my understanding and skill regarding Python and SQL.

Once you download and extract ninecardpoker.zip, you can run the self-standing application therein named "ninecardpoker".

This game uses pygame to take user clicks as input, place cards within the game window and refresh the game window after each click while also notifying the player of what was scored.  Instructions are provided at the beginning of the game, and error-handling functionality is built-in so that the player cannot place cards where a card already exists.

Also, "webscript" is a data scraper that uses selenium, requests, seaborn, and BeautifulSoup.  It examines a blog I control, calculates the frequency of each letter in the alphabet within the source text (minus most irrelevant tags), writes this data to a .CSV file, prepares a web browser in Chrome to alert me that the analysis is complete via the blog's contact page, and finally displays an x-y bar graph summarizing the data.

Lastly, the source file named "sqlinpython" demonstrates my understanding of how Python and SQL can work together by applying methods found in the mysql library to queries formatted as strings.  After a user provides the script a MySQL password, it creates a database on the server.  Then, when provided a database password, the script creates and populates two tables therein and prints the result of a UNION-based query upon them.
