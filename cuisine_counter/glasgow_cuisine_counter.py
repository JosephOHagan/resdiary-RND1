import csv
import math

def main():

    cuisineDict = {}
    restaurantDict = {}

    with open( 'CuisineTypes.csv', 'rb' ) as f:
        reader = csv.reader(f)

        next( reader, None )
        for row in reader:
            cuisineDict[int(row[1])] = 0
            restaurantDict[int(row[1])] = row[0]

    with open( 'RestaurantCuisineTypes.csv', 'rb' ) as f:
        reader = csv.reader(f)

        next( reader, None )
        for row in reader:
            cuisineDict[int(row[1])] += 1

    sortedOccurrences = sorted(cuisineDict.values(), reverse=True)
    sortedTypes = sorted(cuisineDict, key=cuisineDict.get, reverse=True)

    i = 0

    with open( 'results.csv', 'w' ) as csvfile:
	fieldnames = ['Cuisine', 'Occurrences']
	writer = csv.DictWriter( csvfile, fieldnames=fieldnames )

	writer.writeheader()
	for cuisine in sortedTypes:
		writer.writerow( {'Cuisine': restaurantDict[cuisine], 'Occurrences': sortedOccurrences[i]} )
		i += 1

if __name__=="__main__":
    main()
