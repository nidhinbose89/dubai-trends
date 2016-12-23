# To run the application

> pip install -r requireents.txt
> ./runserver.py


# The application fetches the top 25 trending topics in Dubai based on tweet volume.

- It is done via Yahoo! WOEID (Where On Earth IDentifier). I have hard-coded Dubai's WOEID in default_settings.py.

# When any of topic is selected, the adjacent panel shows tweets pertaining to it.
 - The tweets are obtained from Twitter's streaming API via locking a geographic area's -- here Dubai -- lat/long co-ordinates.

 Note - I am force resetting the thread on every page refresh by killing it. This can be avoided or kept [trend_app.views.index].