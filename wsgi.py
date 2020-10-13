import csv
import os

from flask import Flask, request
from omxplayer.player import OMXPlayer

# Create the web application instance
app = Flask(__name__, template_folder="templates")

# Season-episode-dictionary
season_episode_csv_file = 'season_episode_dict.csv'
reader = csv.reader(open(season_episode_csv_file, 'r'))
season_episode_dict = {}
for row in reader:
    season, episode, link = row
    season_episode_dict[(int(season), int(episode))] = link

# Placeholder for player object
player = None


@app.route('/select')
def select():
    """
    Select season and episode and start playing selected item.
    E.g. http://192.168.0.134:5000/select?season=1&episode=2

    :return: String with status
    """
    global player

    if player:
        player.stop()
    season_ = request.args.get('season', default=1, type=int)
    episode_ = request.args.get('episode', default='1', type=int)
    video_link = season_episode_dict[(season_, episode_)]
    #TODO: check if season episode combination valid

    player = OMXPlayer(video_link, dbus_name='org.mpris.MediaPlayer2.omxplayer1')
    player.play()

    return "Playing season {}, episode {}.".format(season_, episode_)


@app.route('/play')
def play():
    """
    This function starts playing the video

    :return: String with status
    """
    player.play()

    return "Playing video."


@app.route('/pause')
def pause():
    """
    This function pauses the video

    :return: String with status
    """
    player.pause()

    return "Video paused."


@app.route('/tv-power')
def tv_power():
    """
    Turn TV on or off

    :return:
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
