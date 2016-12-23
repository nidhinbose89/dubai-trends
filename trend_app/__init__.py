from app import create_app_and_socket


app, socketio = create_app_and_socket()

import trend_app.views
