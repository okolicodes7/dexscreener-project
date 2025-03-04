# dexscreener-project
below is a simple python script that calls an api endpoint on dexscreener, to fetch token profiles.


### Steps
I imported a request library that was part of setup command in dexscreener. I also imported a time library 
I took the API endpoint from dexscreener and installed it in a variable called API_URL and given that It can only make 60 request per minute.
I set another variable named MAX_REQUESTS_PER_MIN to 60 then I initialized a loop that’ll be able to make 60 requests. Now I tried to get request passing in the API_URL it into a response variable. Made an if statement to check if the score of the response is equals to 200 then fetch the output of a  response and set it to a variable I named data. 
I used a python built in function named `isinstance`. to check if the data is a list before doing a full loop over all token profiles in the data object.
so first of all i print a new line called token profile then proceeded to print the schema i want
Then I called sleep on the time library
