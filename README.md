# smart-drone-software
This is a simple project made by me to try and create some basic software to handle an autonomous drone's flight plan and delivery. The project takes the location data of the customers and creates a simple distance matrix which consists of the distances from each node to all other nodes. From this, the closest node from the current node is taken as the next node in the path (with the first current node being the current location of the drone as it starts from the drone bay). This way the flight path is established.

After this, the drone is assumed to be moving and as it reaches within 1 km of the current destination node, it sends an SMS via IFTTT and Webhooks to the intended recipient. Then when the distance between the destination node and the current location of the drone (taken from the GPS module) becomes zero, the product is assumed to have been delivered and the destination node becomes the next one in the list.

DUE TO THE PANDEMIC AND LACK OF PARTS TO MAKE THE DRONE, MANY ASPECTS OF THIS SOFTWARE HAS BEEN SIMULATED AND NOT EXACTLY AS IT HAS BEEN DESCRIBED.

Navigating the directories - 

The folder named "drone" consists of the python files that deal with the input of the location information as well as the formulation of the flight path data.
In this project, the location data was hard-coded for demonstration purposes.

This was a hardware project that was made using a Raspberry Pi 4 and a Neo6M GPS module. The code shown here was uploaded into the Raspberry Pi and run on it to simulate the working of this on a movable device.
