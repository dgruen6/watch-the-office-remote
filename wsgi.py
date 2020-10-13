from flask import (Flask, render_template)
from omxplayer.player import OMXPlayer

# Create the web application instance
app = Flask(__name__, template_folder="templates")


# Create a URL route in our application for "/"
@app.route('/play')
def play():
    """
    This function starts playing the video

    :return: String with status
    """
    global player
    video_path = 'https://www2080.o0-5.com/token=sYs-qvU4LC_3thExMsQgnA/1602613714/2a02:908::/27/1/29/753e64c2f00da07f81f72c5be86bf291-720p.mp4'
    player = OMXPlayer(video_path, dbus_name='org.mpris.MediaPlayer2.omxplayer1')

    return "Playing video."


@app.route('/pause')
def pause():
    """
    This function pauses the video

    :return: String with status
    """
    player.pause()

    return "Video paused."


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
