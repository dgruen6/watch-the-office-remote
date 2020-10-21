import csv
import os
import subprocess

from flask import Flask, request, current_app
from omxplayer.player import OMXPlayer  # OMXPlayer is available by default on Raspberry Pi


# Create the web application instance
app = Flask(__name__)

# Season-episode-dictionary
season_episode_csv_file = 'season_episode_dict.csv'
reader = csv.reader(open(season_episode_csv_file, 'r'))
season_episode_dict = {}
for row in reader:
    season, episode, link = row
    season_episode_dict[(int(season), int(episode))] = link

# Create space for player object in application context
app.config['player'] = None


@app.route('/select')
def select():
    """
    Select season and episode and start playing selected item.
    E.g. http://192.168.0.134:5000/select?season=1&episode=2

    :return: String with status
    """
    # Get current player object
    player = current_app.config['player']

    # Stop player if it exists (stops a running video)
    if player:
        player.stop()
        subprocess.call("pkill omx", shell=True)

    # Read season and episode number from request
    season_ = request.args.get('season', default=1, type=int)
    episode_ = request.args.get('episode', default=1, type=int)
    video_link = season_episode_dict[(season_, episode_)]

    # Create new player object. Playback starts automatically
    player = OMXPlayer(video_link)
    current_app.config['player'] = player

    return "Playing season {} episode {}".format(season_, episode_)


@app.route('/play')
def play():
    """
    This function resumes playing the video if video currently paused

    :return: String with status
    """
    player = current_app.config['player']
    player.play()

    return "Playing video."


@app.route('/pause')
def pause():
    """
    This function pauses the video.

    :return: String with status
    """
    player = current_app.config['player']
    player.pause()

    return "Video paused."


@app.route('/tv-power')
def tv_power():
    """
    Turn TV on or off

    :return: String with status
    """
    status = request.args.get('status', default=1, type=str)
    if status == 'on':
        os.system("echo on 0 | cec-client -s -d 1")
        return "TV on"
    elif status == 'off':
        os.system("echo standby 0 | cec-client -s -d 1")
        return "TV off"
    else:
        return "Invalid command. Valid commands are 'on' and 'off'"


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0')
