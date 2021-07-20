import pyrebase


class Data:

    # Constructor: To set-up the requirements for the Firebase Application
    def __init__(self, locations):
        # Setting up the configuration settings for the firebase API
        self.firebaseConfig = {
            "apiKey"            : "AIzaSyDCFFBEJgVbCuujbsdn8jFULrW41r-ROrI",
            "authDomain"        : "autodrone-ceb89.firebaseapp.com",
            "databaseURL"       : "https://autodrone-ceb89-default-rtdb.asia-southeast1.firebasedatabase.app",
            "projectId"         : "autodrone-ceb89",
            "storageBucket"     : "autodrone-ceb89.appspot.com",
            "messagingSenderId" : "524000825410",
            "appId"             : "1:524000825410:web:f144502a065e3d284e1ddb",
            "measurementId"     : "G-DLHSKQM5N9"
        }

        self.firebase = pyrebase.initialize_app(self.firebaseConfig)  # Setting up the firebase API
        self.db = self.firebase.database()                            # Setting up the object for the DATABASE
        self.storage = self.firebase.storage()                        # Setting up the object for the STORAGE
        self.locations = locations

    # PUBLIC: Method to push data file (.txt) to Firebase storage
    def push_to_storage(self, filename):
        cloud_file_name = "data/locations_set_1"
        self.storage.child(cloud_file_name).put(filename)

    # PUBLIC: Method to download data file (.txt) from Firebase storage
    def get_from_storage(self):
        cloud_file_name = "data/locations_set_1"
        self.storage.child(cloud_file_name).download("analysis", "locations_set_1.txt")

    # PUBLIC: Method to write the location data into a .txt file
    def write_data_to_file(self):
        fw = open("files/locations_set_1.txt", 'w')
        for location in self.locations:
            # print(location[0], ", ", location[1])
            add_string = str(location[0]) + ',' + str(location[1]) + '\n'
            fw.write(add_string)

        fw.close()

    # PUBLIC: Method to read the location data from the .txt file
    def read_data_file(self, fileName) -> list:
        locations = list()
        filename = "files/" + fileName
        fr = open(filename, 'r')
        data = fr.readlines()
        for line in data:
            loc_data = line.split(',')
            loc_data[0] = float(loc_data[0])
            loc_data[1] = float(loc_data[1])
            locations.append(loc_data)

        return locations

class Analysis:

    def __init__(self, points: list):
        self.points = points

    def calculate_centroid(self):
        sum_x = 0
        sum_y = 0
        for point in self.points:
            sum_x += point[0]
            sum_y += point[1]

        return [(sum_x / len(self.points)), (sum_y / len(self.points))]
