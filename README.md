# What this application does
Remote control your TV from your iPhone and watch 'The Office' episodes or any other TV show episodes

# Prerequisites
You need an Apple mobile device (iPhone or iPad), a TV with an HDMI-input, an Apple computer (e.g. Mac, MacBook) to install the application to your mobile device, a wireless local area network (WLAN/Wifi), and an extra computing device (I used a Raspberry Pi 3)

# Setup
1. Install the latest version of Xcode on your Apple computer
2. Clone this repository to your Apple computer
3. Connect your Apple mobile device to your Apple computer via cable
4. In Xcode, change the iOS requirements to your iOS version on your mobile Apple device, e.g. iOS 14.1
5. In Xcode, click the "Play" button to build and install the application on your mobile Apple device
6. Connect to your extra computing device, here a Raspberry Pi 3, via SSH and copy the 'Backend'-folder to the Raspberry Pi.
7. For single use run the 'wsgi.py' script on the Raspberry Pi. For regular usage, I recommend putting the shell script (located in the 'Backend'-folder) in your autostart folder on the Raspberry Pi. With that the 'wsgi.py' script runs automatically when the Raspberry Pi is turned on.
8. Download your favorite episodes of 'The Office' or any other show and copy them to your Raspberry Pi. 
9. Link the files in the 'season_episode_dict.csv'-file, so that the 'wsgi.py'-script can find them.
10. Run the installed app on your mobile Apple device and enjoy watching your favorite episodes!
