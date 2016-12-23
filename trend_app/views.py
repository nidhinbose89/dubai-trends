"""Views.py."""
from flask import render_template
from twitter import Twitter
from trend_app import app
from urllib2 import URLError

twitter_auth = app.config.get("TWITTER_AUTH")


@app.route('/')
def index():
    """View to get the top 25 trends and show in index.html."""
    thread = app.config.get('THREAD', None)
    if thread:
        thread.kill()
    twitter = Twitter(auth=twitter_auth)
    top_25_topics = []
    try:
        results = twitter.trends.place(_id=app.config.get("DUBAI_WOEID"))
        if results:
            top_25_topics = sorted(
                results[0]['trends'],
                key=lambda x: x['tweet_volume'],
                reverse=True)[:25]
    except URLError:
        # show in HTML that there is no network.
        pass
    except Exception as e:
        raise e
    return render_template("index.html", top_25_topics=top_25_topics)
