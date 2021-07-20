# import serial
# from time import sleep
# import sys
#
# ser = serial.Serial("/dev/serial0")
# gpgga_info = "$GPGGA,"
# GPGGA_buffer = 0
# NMEA_buff = 0
#
#
# class GPS:
#
#     def convert_to_degrees(self, raw_value):
#         decimal_value = raw_value/100.00
#         degrees = int(decimal_value)
#         mm_mmmm = (decimal_value - int(decimal_value))/0.6
#         position = degrees + mm_mmmm
#         position = "%.4f" %(position)
#         return position
#
#     def get_location(self):
#         try:
#             while True:
#                 received_data = (str)(ser.readline()) #read NMEA string received
#                 GPGGA_data_available = received_data.find(gpgga_info)   #check for NMEA GPGGA string
#
#                 if (GPGGA_data_available > 0):
#                     GPGGA_buffer   = received_data.split("$GPGGA,",1)[1]  #store data coming after “$GPGGA,” string
#                     NMEA_buff      = (GPGGA_buffer.split(','))
#                     nmea_time      = list()
#                     nmea_latitude  = list()
#                     nmea_longitude = list()
#                     nmea_time      = NMEA_buff[0]                    #extract time from GPGGA string
#                     nmea_latitude  = NMEA_buff[1]                    #extract latitude from GPGGA string
#                     nmea_longitude = NMEA_buff[3]                    #extract longitude from GPGGA string
#                     print("NMEA Time: ", nmea_time,'\n')
#                     lat   = (float)(nmea_latitude)
#                     lat   = self.convert_to_degrees(lat)
#                     longi = (float)(nmea_longitude)
#                     longi = self.convert_to_degrees(longi)
#                     print("Current location of the drone is - ")
#                     print ("NMEA Latitude:", lat,"NMEA Longitude:", longi,'\n')
#                     return [lat, longi]
#
#         except KeyboardInterrupt:
#             sys.exit(0)
