

#print formating very useful 
# x = ' hello my name is {x} and the best player of Peru is {x}'. format (x='italo')
# print(x)


# append vs extend  ---}
# pop --> index can be specify
# reverse() && sort() --->change in place do not need to be assigned to a var
#index a nested list 



# nums  = [ 1,2,3,4]
# to_be_added = [21313,13131]
# nums.append(to_be_added)
# print(nums)


# nums = list([23,2,32,32])
# lucky_num = nums.pop(1)
# print(nums)
# print(lucky_num)

# nums.reverse()

# print(nums)


# nums = list([3,323,32,['a','b','c']])
# print (nums[3][1])





# matrix = list([[1,2,3],[1987,1989,1990],['a','b','c']])
# list_nums =[row[2] for row in matrix ]
# print(list_nums)



#dict -> do not retain any kind of other . values hold any datatype 
#tupples -> inmutable and fix on size && support different data types
#sets -> unnored collections



# dict_data_types = {'italo':'34', 'Javier': '23', 'Amanda' : '34'}
# print(dict_data_types['Amanda'])

# set - unnored of collection items -> add() [method]
# set -doesnt repeat items  





# my_dict_items = {'lunch':'pizza' , 'breakfast' : 'eggs'}
# my_dict_items['lunch'] = 'burger'
# print(my_dict_items)


# my_stuff = { 'key1': 'one' , 'key2': 'two' , 'key3':{ 'three': [1, 2 ,'hello'] } }

# print (my_stuff['key3']['three'][2].upper())
# dict_example = {'breakfast': 'eggs' ,'lunch' : 'mashpotatoes'}
# dict_example['dinner'] = 'arroz con pollo'
# dict_example ['breakfast'] = 'chiken'
# print (dict_example)


# s = 'django'


# print(s[-2:])
# print(s[1:4])

# store = list(s)
# store.reverse()

# print(store)

# l  = [3,7, [1,4,'hello']]
# l[2][2] = 'goodbye'
# print (l)


# rhymes = [['cat', 'hat', 'fat'], ['mouse', 'house', 'louse'], ['be', 'see', 'key', 'he']]
# for elements in rhymes:
#     elements.reverse()
#     print (elements)





# def max_visits(visit_by_patient):
#     max_of_visit = 0 
#     for patients in visit_by_patient:
#         visit  = len(patients)
#         if (visit) > max_of_visit:
#             max_of_visit = visit
#     return max_of_visit

# print (max_visits([[2, 6], [3, 10], [15], [23], [1, 8, 15, 22, 29], [14]]))


class car(): 

    def __init__(self,make,color):
        self.make = make
        self.color = color


    def kind_of_car(self):
        print('the color of the car is', self.color)
        print('the make of the car is', self.make)




bmw  = car('bmw','yellow')



bmw.kind_of_car()