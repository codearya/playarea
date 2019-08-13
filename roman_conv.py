

'''

i = 1
v = 5
x = 10
l = 50
c = 100
m = 1000

Input given must in descending value order except when a letter is immediately preceded by a one lower than it in which case it will be substracted

xiv = 14
mmxlix = 2049

read from left to right
Only one number - lookup dictionary and return value
More than one - lookup dict and get the values
if the previous one is less then current then current - prev and save in a result var
 iterate this
 if previous is greater than current just add prev to current

'''


my_dict = {'i':1, 'v':5, 'x':10, 'l':50,'c':100,'m':1000 }

def roman_conv(romannum):

    '''for x in my_dict:
        val = my_dict.values()
        print(my_dict['i'])
        print(val)'''
    r_list = list(romannum)
    print("Input Roman Number is {}".format(romannum))
    print("Input Roman Number list is {}".format(r_list))
    eresult = 0
    rconv_list = []
    for x in r_list:
        val = my_dict[x]
        #print("roman value of {0} is {1}".format(x,val))
        rconv_list.append(val)
        #print("roman converted list is {}".format(rconv_list))
        #print("current value is {}".format(val))
        #print("\n\n")
    print("roman converted list is {}".format(rconv_list))
    i =0
    while i < len(rconv_list):
            print("current number is {0}".format(rconv_list[i]))
            print("previous number is {0}".format(rconv_list[i-1]))
            if i-1 <0:
                eresult = eresult+ rconv_list[i]
                #del rconv_list[i]
            elif rconv_list[i-1] >=0 and rconv_list[i-1] < rconv_list[i]:
                eresult = eresult + rconv_list[i] - rconv_list[i-1] - rconv_list[i-1]
                #del rconv_list[i]
            elif rconv_list[i-1] >=0 and rconv_list[i-1] >= rconv_list[i]:
                eresult = eresult + rconv_list[i]
                #del rconv_list[i]
            print("end results is {}".format(eresult))
            print("\n \n")
            i+=1


roman_conv('vvvvvv')



'''
 for x in rconv_list:
            print("Index of {0} is {1}".format(x,rconv_list.index(x)))
            #print("Index of previous number is {0}".format(rconv_list[(rconv_list.index(x)-1)])
            if rconv_list.index(x)-1 <0:
                eresult = eresult+ rconv_list[rconv_list.index(x)]
                rconv_list.remove(rconv_list)
            elif rconv_list.index(x)-1 >=0 and rconv_list[rconv_list.index(x)-1] < rconv_list[rconv_list.index(x)]:
                eresult = eresult + rconv_list[rconv_list.index(x)] - rconv_list[rconv_list.index(x)-1] - rconv_list[rconv_list.index(x)-1]
                rconv_list.remove(x)
            elif rconv_list.index(x)-1 >=0 and rconv_list[rconv_list.index(x)-1] >= rconv_list[rconv_list.index(x)]:
                eresult = eresult + rconv_list[rconv_list.index(x)]
                rconv_list.remove(x)
            print(eresult)
            print("\n \n")

'''

