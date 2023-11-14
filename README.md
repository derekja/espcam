# espcam
This is a repo for the ESP-CAM workshop taught at UVic in the fall of 2023 using the AI Thinker board and OpenCV using YOLOv3 for image recognition.

To install the esp32-cam board first install the Arduino 2.2.1 environment:

https://www.arduino.cc/en/software

Then in the preferences dialogue add the board manager url: https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json

Then in the Tools -> Board manager install the ESP32 by Espressif Systems

Then you can plug the board into a usb port and select the "AI Thinker ESP32-CAM" board on the appropriate port.

Next, load the sketch ("cameraserver.ino") into the arduino environment (by either cloning this repository, or clicking on the code button and downloading a zip file and extracting it to a directory)

If you are on the UVic network, you can leave lines 11 and 12 at their defaults, and fill in your netlink information for lines 7-9. And make sure that line 79 is commented out, and line 80 is uncommented.

If you are on a home network, put your ssid and password in lines 11-12 and then comment out line 80 and uncomment line 79.

open the serial monitor, set the baud to 115200, and press the reset button on the ESP32-CAM (or unplug and plug back in the board)

The URL of the camera should now appear in the serial monitor as follows (but with your own URL)

CAMERA OK
http://10.75.1.66
  /cam-lo.jpg
  /cam-hi.jpg
  /cam-mid.jpg

  If the camera does not read as OK, check your ssid and username and reset the ESP32-CAM board again.

  You can now open a web browser (that is on the same subnet) to one of the three URLs listed and see the camera output. Each time the page is reloaded a new image will be present.

Python setup

You should probably use virtual environments for your python setup. This prevent different versions from conflicting with each other. Please see additional information here: https://realpython.com/python-virtual-environments-a-primer/

You may also want some introduction to git and source code control. I like github desktop and generally use the command line tools in the git bash shell that it installs. You can find information about that here: https://docs.github.com/en/desktop/overview/getting-started-with-github-desktop

Make sure that you have python 3.x installed. https://www.python.org/downloads/

Install the editor of your choice. I will demonstrate in VS Code, but any editor is fine.

pip install numpy
pip install opencv-python

place the files from this repository into a directory (using either git clone, if you have installed github desktop, or by clicking on the code dropdown and downloading a zip file. You may have done this already in the above section on setting up the ESP32-CAM)

edit the detection.py file to use the proper url for your camera

In a git bash window (or other python shell) you can 

The weights for yolo come from https://pjreddie.com/media/files/yolov3.weights and you should copy them into your source directory (since they are not mine to license I cannot put them into the repository, the description of the yolo code is here: https://pjreddie.com/darknet/yolo/)

The inspiration for this project came from a version that reads from a video and is found here: https://github.com/yashrajmani/OpenCV_Yolo3_Object_Detection-from-Video/tree/main

run "python3 detections.py" and move the camera around to see what is detected. Press the "q" key to exit the application.
