"""Script to generate app and socketio."""
from flask import Flask, session, request
from flask_socketio import SocketIO, emit, disconnect
from twitter import TwitterStream
thread = None


def create_app_and_socket():
    """Helper to create and return app and socketio."""
    # Set this variable to "threading", "eventlet" or "gevent" to test the
    # the best option based on installed packages.
    async_mode = None

    app = Flask(__name__, static_url_path='')
    app.config.from_object('trend_app.default_settings')
    app.config['SECRET_KEY'] = 'secret!'
    socketio = SocketIO(app, async_mode=async_mode)

    twitter_auth = app.config.get("TWITTER_AUTH")

    # The Background Thread to emit tweets infinitely until a new click.
    def background_thread(tweet_iter):
        """Send server generated tweets to client."""
        while True:
            data = tweet_iter.next()
            print "serving: ", data.get('text')
            socketio.emit('my_response',
                          {'data': data.get('text', "No text")},
                          namespace='/dubai_trend')
            print "sleep..."
            socketio.sleep(3)

    # The Topic Click Handler.
    @socketio.on('topic_click', namespace='/dubai_trend')
    def test_message(message):
        search_term = message['data']
        global thread
        if thread:
            thread.kill()
        if search_term:
            print "found search term", search_term
            print "streaming twitter..."
            stream = TwitterStream(auth=twitter_auth, secure=True)
            tweet_iter = stream.statuses.filter(
                track=search_term,
                locations='24.910739, 54.936314, 25.302092, 55.340652')
            print "got twitter stream..."
            thread = socketio.start_background_task(target=background_thread,
                                                    tweet_iter=tweet_iter)
            app.config['THREAD'] = thread
        return True

    # Disconnect Handlers.
    @socketio.on('disconnect_request', namespace='/dubai_trend')
    def disconnect_request():
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit(
            'my_response', {'data': 'Disconnected!',
                            'count': session['receive_count']})
        disconnect()

    @socketio.on('disconnect', namespace='/dubai_trend')
    def test_disconnect():
        print('Client disconnected', request.sid)

    # Error Handlers.
    @socketio.on_error('/dubai_trend')
    def error_handler_chat(e):
        socketio.emit('my_response',
                      {'data': "Check Network Connectivity And Try Again."},
                      namespace='/dubai_trend')

    return app, socketio
