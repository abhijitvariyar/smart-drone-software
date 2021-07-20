import numpy as np
import math


class Drone:

    # Constructor: Takes positions as list of co-ordinates
    def __init__(self, positions: list):
        self.locations = positions              # Storing locations data in list
        self.path = [0]                         # Initializing list for path with first node as starting node

    # PUBLIC: Method to get the location data
    def get_locations(self):
        return self.locations

    # PUBLIC: Method to print the location data
    def print_locations(self):
        for i in self.locations:
            print(i)

    def distance_between(self, loc1: list, loc2: list) -> float:
        return self.__calculate_dist(loc1, loc2)

    # PUBLIC: Method to find path
    def calculate_path(self):
        dist_mat = self.__cal_dist_matrix()         # Calculating distance matrix
        path_nodes = [0]                            # Initializing path list with first node
        curr_node = self.path[0]                    # Setting current node to the first node
        min_nodes = list()                          # Initializing distance list with empty list

        # print(dist_mat)

        for _ in range(len(dist_mat)-1):
            min_nodes = list()
            for col in range(len(dist_mat)):
                if col in path_nodes:
                    pass
                else:
                    min_nodes.append(dist_mat[curr_node][col])

            min_dist = min(min_nodes)
            path_nodes.append(self.__index(min_dist, dist_mat[curr_node]))
            curr_node = path_nodes[-1]

        # To add the remaining node into the end of the path
        for i in range(len(min_nodes)):
            if i not in min_nodes:
                min_nodes.append(i)
            min_nodes[i] += 1

        # To increment each node by 1 to represent node number instead of index value
        # for i in range(len(path_nodes)):
        #     path_nodes[i] += 1

        self.path = path_nodes
        return self.path

    # PUBLIC: Function to calculate the distance between two locations
    def dist(self, loc_1, loc_2):
        return self.__calculate_dist(loc_1, loc_2)

    # PRIVATE: Method to calculate the distance matrix for the different locations
    def __cal_dist_matrix(self):
        mat = list()
        size = len(self.locations)
        for _ in range(size):
            mat.append([0 for _ in range(size)])

        # Converting nested list into numpy array
        mat = np.asarray(mat, dtype = np.float)

        # Creating the distance matrix to store distances between the locations
        for row in range(len(mat)):
            for col in range(row+1):
                dist = self.__calculate_dist(self.locations[row], self.locations[col])
                mat[row][col] = dist
                mat[col][row] = dist

        print(mat)
        return mat

    # PRIVATE: Method to calculate the index value of the element
    @staticmethod
    def __index(min_dist: int, arr: np.asarray):
        for ind in range(len(arr)):
            if arr[ind] == min_dist:
                return ind

    # PRIVATE: Method to calculate distances between two locations
    @staticmethod
    def __calculate_dist(pos1: list, pos2: list):
        R = 6373.0

        lat1 = math.radians(pos1[0])
        lon1 = math.radians(pos1[1])
        lat2 = math.radians(pos2[0])
        lon2 = math.radians(pos2[1])
        
        dlat = lat1 - lat2
        dlon = lon1 - lon2
        
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c
        
