# espcam
This is a repo for the ESP32-CAM workshop taught at UVic in the fall of 2023 using the AI Thinker board and OpenCV using YOLOv3 for image recognition.

Here is a video walkthrough of the installation: https://share.descript.com/view/QBxWRlFY9pw

## Installation

#### M-series Mac Setup

To install Arduino on newer Mac's you should have XCode, HomeBrew, and Rosetta installed. To install XCode and HomeBrew, run the following commands:
(these are not necessary on any mac other than an M-series)

```bash
install xcode
install homebrew
```

**Note:** To install Rosetta on M-Series Mac's you also need to install Rosetta. To check if you have Rosetta installed the following command can be executed and should output 'Yes':

```bash
softwareupdate --install-rosetta
# Verify that Rosetta is installed by running the following command.
# Output should be 'Yes'
/usr/bin/pgrep -q oahd && echo Yes || echo No
```

### Arduino & Python Installation

To install the esp32-cam board first install the Arduino 2.2.1 environment:


https://www.arduino.cc/en/software

Then in the preferences dialogue add the board manager url: https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json

Then in the Tools -> Board manager install the ESP32 by Espressif Systems

Then you can plug the board into a usb port and select the "AI Thinker ESP32-CAM" board on the appropriate port.

Next, load the sketch ("cameraserver.ino") into the arduino environment (by either cloning this repository, or clicking on the code button and downloading a zip file and extracting it to a directory)

Next, go to https://github.com/yoursunny/esp32cam and click on the "code" button and download a zip file

In the arduino UI, under sketch click on include library-> add zip library and point to the zip file you just downloaded.

ignore this! the uvic network will not work at the moment! If you are on the UVic network, you can leave lines 11 and 12 at their defaults, and fill in your netlink information for lines 7-9. And make sure that line 82 is commented out, and line 84 is uncommented.

If you are on a home network, put your ssid and password in lines 11-12 and then comment out line 84 and uncomment line 82.

open the serial monitor, set the baud to 115200, and press the reset button on the ESP32-CAM (or unplug and plug back in the board)

The URL of the camera should now appear in the serial monitor as follows (but with your own URL)

CAMERA OK

http://10.75.1.66

  /cam-lo.jpg

  /cam-hi.jpg

  /cam-mid.jpg

  If the camera does not read as OK, check your ssid and username and reset the ESP32-CAM board again.

  You can now open a web browser (that is on the same subnet) to one of the three URLs listed and see the camera output. Each time the page is reloaded a new image will be present.

#### Python Setup

You should probably use virtual environments for your python setup. This prevent different versions from conflicting with each other. Please see additional information here: https://realpython.com/python-virtual-environments-a-primer/

You may also want some introduction to git and source code control. I like github desktop and generally use the command line tools in the git bash shell that it installs. You can find information about that here: https://docs.github.com/en/desktop/overview/getting-started-with-github-desktop

Make sure that you have python 3.x installed. https://www.python.org/downloads/ (I would advise against 3.12 right now, one of the examples does not work)

Install the editor of your choice. I will demonstrate in VS Code, but any editor is fine.

pip install numpy

pip install opencv-python

place the files from this repository into a directory (using either git clone, if you have installed github desktop, or by clicking on the code dropdown and downloading a zip file. You may have done this already in the above section on setting up the ESP32-CAM)

edit the detection.py file to use the proper url for your camera

In a git bash window (or other python shell) you can 

The weights for yolo come from https://pjreddie.com/media/files/yolov3.weights and you should copy them into your source directory (since they are not mine to license I cannot put them into the repository, the description of the yolo code is here: https://pjreddie.com/darknet/yolo/)

The inspiration for this project came from a version that reads from a video and is found here: https://github.com/yashrajmani/OpenCV_Yolo3_Object_Detection-from-Video/tree/main

run "python3 detections.py" and move the camera around to see what is detected. Press the "q" key to exit the application.

This example can be extended to a later (and more performant) version of YOLO by following the tutorial here: https://thepythoncode.com/article/yolo-object-detection-with-opencv-and-pytorch-in-python

Some more detail on the YOLO family of detectors can be found here: https://www.v7labs.com/blog/yolo-object-detection

And some detail on training the models and writing new detectors here: https://www.freecodecamp.org/news/how-to-detect-objects-in-images-using-yolov8/

A nice example from a student in my lab is here: [https://github.com/sofiiak13/OpenCV](https://github.com/sofiiak13/OpenCV) (this is the one that needs something lower than python 3.12, but higher than 3.9)

