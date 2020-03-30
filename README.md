# WebScraper
A Python script for extracting information about the top articles on the HackerNews website.

#Prerequisites
-Firstly, you must have the validators module installed on your machine. Use the command 'pip install validators' in the command line to achieve this.
-To run the script, navigate to the directory containing the file hackernews.py on your machine. Then in the command line run the command "python3 hackernews.py 'posts'". In place of the string 'posts' you should enter an integer between 1 and 100, this being the number of articles you would like the function to return. For example; "python3 hackernews.py 87".

#Libraries
-Requests is an HTTP request library which I used to make a request for the webpage that I was concerned with.
-BeautifulSoup is a Python webscraping library that I used to extract and parse the html from the webpage I was examining.
-Validators is an input validation library; I used the validators.url method from it to validate that the URI's I was extracting from the webpage were genuine.
-I used the json.dumps method from the json module in order to convert the objects that contained the extracted data into the JSON format.
-Finally I used the sys library to create a placeholder variable that can be used to run the hackernews method from the command line.
