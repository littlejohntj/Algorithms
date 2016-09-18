import math
import sys

def sort_points_by_x(point_1, point_2): 
	if point_1[0] <= point_2[0]:
		return True
	else:
		return False

def sort_points_by_y(point_1, point_2):
	if point_1[1] <= point_2[1]:
		return True
	else: 
		return False 

def merge_sort(node_list, compare):

	list_len = len(node_list)

	# check for your base case. the size of the list is less than or equal to two. 
	if list_len == 1: 
		return node_list
	elif list_len == 2:
		if compare(node_list[1], node_list[0]):
			temp_node = node_list[0]
			node_list[0] = node_list[1]
			node_list[1] = temp_node
		return node_list

	# split the list into two lists, left and right
	left_node_list = node_list[0:int(math.ceil( list_len / 2.0 ))]
	right_node_list = node_list[int(math.ceil( list_len / 2.0 )):]

	# recursivly call a merge_sort on both halves 
	sorted_left_node_list = merge_sort(left_node_list, compare)
	sorted_right_node_list = merge_sort(right_node_list, compare)

	# merge the two sorted lists 
	sorted_node_list = []
	i = j = 0 
	while i < len(sorted_left_node_list) or j < len(sorted_right_node_list):

		if i == len(sorted_left_node_list):
			sorted_node_list.append( sorted_right_node_list[j] )
			j += 1
		elif j == len(sorted_right_node_list):
			sorted_node_list.append( sorted_left_node_list[i] )
			i += 1
		elif compare(sorted_left_node_list[i], sorted_right_node_list[j]):
			sorted_node_list.append( sorted_left_node_list[i] )
			i += 1
		else: 
			sorted_node_list.append( sorted_right_node_list[j] )
			j += 1

	# return the sorted and merged list 
	return sorted_node_list

def distance(point_1, point_2):
	return math.sqrt( (point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2 )

def brute_force_find_closest_points(points):
	smallest_distance = -1 
	point_1 = ()
	point_2 = ()
	for i, j in enumerate(points):
		for p,d in enumerate(points):
			if i != p:
				temp_distance = distance(j, d)
				if temp_distance < smallest_distance or smallest_distance == -1:
					smallest_distance = temp_distance
					point_1 = j
					point_2 = d
	return (point_1, point_2)

def find_closest_points(p, y):

	# first get the length of p
	p_length = len(p)

	# check if the length of p is less than 4 for the base case 
	if p_length < 4: 
		return brute_force_find_closest_points(p)

	# split p into p_l and p_r 
	p_l = p[0:int(math.ceil( p_length / 2.0 ))]
	p_r = p[int(math.ceil( p_length / 2.0 )):]

	# partition y into y_l and y_r where y_l are the points in y that are in p_l and y_r are the points in y that are in p_r 
	y_l = []
	y_r = []

	for point in y:
		if point in set(p_l):
			y_l.append(point)
		else:
			y_r.append(point) 

	cloesest_pair_left = find_closest_points(p_l, y_l)
	cloesest_pair_right = find_closest_points(p_r, y_r)

	d_left = distance(cloesest_pair_left[0], cloesest_pair_left[1])
	d_right = distance(cloesest_pair_right[0], cloesest_pair_right[1])
	 
	if d_right < d_left:
		shorted_distance = d_right
		closest_pair = cloesest_pair_right
	else:
		shorted_distance = d_left
		closest_pair = cloesest_pair_left
	
	y_prime = [pt for pt in y if abs(pt[0] - p_l[-1][0]) <= shorted_distance]
	
	for a, b in enumerate(y_prime): 
		i = a + 1
		while i <= a + 7:
			if i <= len(y_prime) - 1:
				temp_distance = distance(b, y_prime[i])
				if temp_distance < shorted_distance:
					shorted_distance = temp_distance
					closest_pair = (b, y_prime[i])
			i = i + 1
	return closest_pair

	

q = [(1,5), (8,2), (1,1), (12,6), (6,6), (4,2), (1.1, 1.2), (11, 10), (10,10), (2,4), (0,0), (1,3), (3,5), (5,3), (2,7), (7,9), (.5, .5), (1,9)]

# presort the list of points q 
p = merge_sort(q, sort_points_by_x)
y = merge_sort(q, sort_points_by_y)

cp = find_closest_points(p, y)

print "{0} {1}".format(cp[0],cp[1])

