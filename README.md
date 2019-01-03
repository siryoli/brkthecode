# brkthecode
http://www.brkthecode.com/

 The IFS Labs Turkish Delight business is booming but they have hit a bottleneck in delivering the product to their customers. Traditional delivery methods just can’t keep up with the demand. But luckily, they have a fleet of drones at their disposal.

As you might imagine, the drones themselves are limited in range so a multitude of battery changing stations have been setup throughout the country but there is a limitation. Different stations have different capacity batteries available. And it takes a constant of time to land and take off from each stop.

The challenge, if you choose to accept it, is to come up with an optimal algorithm that returns a list of the minimum amount of stations to stop at in order to make an oven fresh Turkish Delight delivery to a customer. You would be given a list of stations that the drone would fly over along the way with the distances between each of them. Use any programming language of your preference.

Assumptions

1. The drone always starts from the station 0
2. The drone does not have to land at each and every station
3. The delivery location you need to get to, is the last station
4. The return trip is unnecessary
5. Battery capacity of 1 unit can cover a distance of 1km
6. The drone can support only 1 battery of any capacity
7. If the drone lands at a station it must have its battery changed
8. The world is flat with no obstacles
9. Only limiting factor to the drone’s range is battery


Example

Sample Data Set
{
    "id" : ID,
    "generatedOn" : DATE,
    "data" : [ [ 7, 1 ] , [ 5 , 5 ] , [ 8 , 2 ] , [ 1 , 2 ] , [ 0 , 0 ] ]
}

Assuming the index of the above 2D “data” array represents the station:

It can be interpreted as

Station (index of array) 	0 	1 	2 	3 	4
Battery Capacity (units) 	7 	5 	8 	1 	0
Distance to Next Station (km) 	1 	5 	2 	2 	0



As you can probably guess, there are multiple paths to the destination. Starting from station 0 with a battery that can fly 7km, all the following paths are valid.
Path A   	1 	2 	4
Path B   	2 	4 	

None of the paths via station 3 are valid since it only carries batteries that can go for 1km, so it would be impossible to reach the destination.

Since the goal of this exercise is to minimize the number of stops, the correct answer would be 2, 4.

The expected output is a text file in JSON format.

{
    "answer" : [ 2 , 4 ]
} 
