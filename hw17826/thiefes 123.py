# start
##################1
smokers = {"John Smith", "Maya Levi", "Noam Cohen", "Liam Patel"}
ride_bikes = {"Maya Levi", "Omer Halevi", "Liam Patel"}
ride_motorcycles = {"John Smith", "Noam Cohen", "Rina Gold"}
likes_skyjump = {"John Smith", "Rina Gold", "Dina Bar"}
#1
suspects = smokers| ride_bikes| ride_motorcycles| likes_skyjump
print(suspects)
#2
print ('The clues:')
print ('1 : The suspect SMOKES')
print ('2 : The suspect likes SKYDIVING')
print ('3 : The suspect rides a BIKE or a MOTORCYCLE')
guilty = smokers & likes_skyjump & (ride_motorcycles | ride_bikes)
print(guilty)

print ()
#####################2
smokers = {"Avi Ron", "Sara Kim", "Ben Azulay", "Nina Fox"}
ride_bikes = {"Sara Kim", "Tom Green", "Nina Fox"}
ride_motorcycles = {"Avi Ron", "Ben Azulay", "Nina Fox", "Eli Stone"}
likes_skyjump = {"Avi Ron", "Nina Fox", "Dana Wolf"}
#1
suspect = smokers| ride_bikes| ride_motorcycles| likes_skyjump
print(suspect)
#2
print ('The clues:')
print ('1 : The suspect rides a BIKE or a MOTORCYCLE')
print ('2 : The suspect SMOKES')
print ('3 :The suspect likes SKYDIVING')
print ('4 : The suspect is NOT someone who rides BOTH bike and motorcycle')
guilty = smokers & likes_skyjump & (ride_motorcycles.symmetric_difference(ride_bikes))
print(guilty)

print ()
#####################3
night_shift = {"Alex", "Jordan", "Taylor", "Casey"}
access_server_room = {"Jordan", "Casey", "Morgan", "Riley"}
hardware_expert = {"Taylor", "Riley", "Casey", "Alex"}
management_role = {"Jordan", "Morgan"}
#1
print ('The clues:')
print ('1 : The suspect was on the NIGHT SHIFT.')
print ( '2 : The suspect has access to the SERVER ROOM.')
print ('3 : The suspect is a HARDWARE EXPERT.')
print ( '4 : The suspect is NOT in a MANAGEMENT ROLE.')
guilty = night_shift & access_server_room & hardware_expert - management_role
print(guilty)
#2
prove =all([ ('Casey') in night_shift,('Casey') in access_server_room,('Casey') in hardware_expert,('Casey') not in management_role])
print(prove)
# stop