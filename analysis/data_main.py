import database as db
import random

def create_random_dataset() -> list:
    deg_lat = 12
    deg_long = 77

    pos_dataset = list()

    for _ in range(2000):
        loc = list()
        random_min_lat = random.uniform(0.88, 0.99)
        random_min_long = random.uniform(0.57, 0.75)
        loc.append(deg_lat + random_min_lat)
        loc.append(deg_long + random_min_long)
        pos_dataset.append(loc)

    return pos_dataset


if __name__ == '__main__':
    dataset = create_random_dataset()                               # Creates a random dataset for analysis
    print("Number of locations in the dataset: ", len(dataset))

    data_obj = db.Data(dataset)
    data_obj.write_data_to_file()                                   # Writes the randomized location data to file "files/locations_set_1.txt"
    data_obj.push_to_storage("files/locations_set_1.txt")           # Pushes/ Uploads the data .txt file to Firebase storage

    data_obj.get_from_storage()                                     # Downloads data .txt file from Firebase storage

    loc_list = data_obj.read_data_file("locations_set_1.txt")
    print(len(loc_list))

    an_obj = db.Analysis(loc_list)
    drone_bay_location = an_obj.calculate_centroid()
    print("Optimum location for the drone bay is: ", drone_bay_location)
