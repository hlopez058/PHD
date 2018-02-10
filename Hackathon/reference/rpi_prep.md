# How to prep the RPI3 for TjBot


1. Use the NOOBs image on SD card and load into the RPI slot. The NOOBs image should be on the SD card but if you need to load it with an sd card loader .

     *  Install noobs from the NOOBS sd image 1.6Gb
     * https://learn.adafruit.com/setting-up-a-raspberry-pi-with-noobs/copy-noobs-onto-an-sd-card 

2. Connect to wifi (this would require FAU authenticating the MAC address)

3. Install Packages : Open a terminal application on the Pi and execute the following commands to install the latest version of Node.js and npm (Node Package Manager). You need these packages later to run your code.

`curl -sL http://ibm.biz/tjbot-bootstrap | sudo sh -`


4. Setup the Audio on the RPI
The usb audio is default but the speaker needs to be forced to use the audio jack. `sudo raspi-config ` force the speaker to come through the audio jack 


5. Download sample code : 
`git clone https://github.com/ibmtjbot/tjbot.git 
cd tjbot/recipes/conversation
npm install`

