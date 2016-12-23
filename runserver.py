#!/usr/bin/env python

"""Script to run the application."""
from trend_app import app, socketio

if __name__ == '__main__':
    socketio.run(app, debug=True)
