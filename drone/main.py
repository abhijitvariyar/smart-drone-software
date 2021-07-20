import Drone as dn
import Customer as cs
# import gps_main as gps

import requests

# gps_obj = gps.GPS()
curr_location = [12.9712, 77.6991]
# curr_location = gps_obj.get_location()
# curr_location[0] = float(curr_location[0])
# curr_location[1] = float(curr_location[1])
print(curr_location)


# Current location of the drone is - 
# NMEA Latitude: 12.9712 NMEA Longitude: 77.6991

# Adding customer information to a list of Customer objects
customer_info = list()
customer_info.append(cs.Customer("Abhijit Variyar" , +919449364238, [12.9801, 77.6948]))
customer_info.append(cs.Customer("Ritvik Rao"      , +919449364238, [12.9776, 77.6990]))
customer_info.append(cs.Customer("Kartik Vashist"  , +919449364238, [12.9833, 77.6899]))
customer_info.append(cs.Customer("Mithul Manoj"    , +919449364238, [12.9689, 77.67004]))

location_list = [[float(curr_location[0]), float(curr_location[1])]]    # The location already existing in the list is the starting point for drone
for obj in customer_info:
    location_list.append(obj.location)

drone = dn.Drone(location_list)

# Setting up data for the working loop
has_path_ended = False                          # The bool variable to check if all the nodes have been visited or not

path = drone.calculate_path()                   # The path the drone has to follow in terms of node number
print("Path to be followed: ", path)

'''
This is the main loop where we check whether the drone's location is within a given range from
the destination or if the drone has reached its destination. The loop will keep running till
the delivery has been done.

There will be 2 stages in the loop -
1. When the drone reaches within a certain range (for example 1 km) when an IFTTT message will be sent
2. When the drone's distance from the destination becomes zero (we will assume that the delivery has been done)
   when we will increment the node in the path and begin tracking the distance to the next node in the path.
'''
location_data = drone.get_locations()
path_index = 1

# The main work loop
while not has_path_ended:
    curr_node = path[path_index]
    curr_customer = customer_info[curr_node-1]
    dist = drone.distance_between(curr_location, curr_customer.location)

    if dist < 1.0:
        # The IFTTT post request that sends the information to the IFTTT trigger to send the SMS
        headers = {"Content-Type": 'application/json'}

        data = '{"value1": "' + str(curr_customer.phoneNo) + '", "value2":"' + curr_customer.name + '"}'
        print("Sending information to phone!")
        response = requests.post(
            "https://maker.ifttt.com/trigger/delivery/with/key/b5AX3sdysVp8JSBGKrZS9q",
            headers = headers,
            data = data
        )
        print("IFTTT message sent to user at node ", path[path_index] , "(Name: ", curr_customer.name + ")")
        dist = 0.0

    if dist == 0.0 and curr_node != path[-1]:
        path_index += 1
        curr_location = curr_customer.location
        choice = input("Shall we simulate for the next location? [y/n]: ")
        if choice == 'y' or choice == 'Y':
            pass
        else:
            break

    if dist == 0.0 and curr_node == path[-1]:
        has_path_ended = True
        print("The deliveries for the day has been completed.")
