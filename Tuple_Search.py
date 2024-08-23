def find_tuples_with_two_numbers(tuples, a, b, c,d,e,f,g,h):
 Num  = 0 ;
 for t in tuples:
   
    count = 0
    if a in t:
         count += 1
    if b in t:
         count += 1
    if c in t:
         count += 1

    if d != None:      
        if d in t :
            count +=1   

    if e != None:      
        if e in t :
            count +=1   

    if f != None:      
        if f in t :
            count +=1   

    if g != None:      
        if g in t :
            count +=1   

    if h != None:      
        if h in t :
            count +=1   
                   
    if count >= 2:
        print(Num)
        print(t)
    Num += 1 

tuples = [(0, 2), (0, 1), (1, 2), (1, 5), (2, 5), (0, 6), (2, 6), (1, 3), (3, 5), (0, 4), (4, 6), (2, 9),
 (5, 9), (6, 9), (3, 8), (5, 8), (4, 7), (6, 7), (7, 11), (10, 11), (8, 10), (1, 10), (0, 11), (14, 17), 
 (14, 15), (15, 16), (16, 17), (12, 19), (12, 13), (13, 18), (18, 19), (22, 23), (22, 24), (23, 24), 
 (25, 27), (25, 26), (26, 27)] 
#find_tuples_with_two_numbers(tuples, 0,1,2,None)

#find_tuples_with_two_numbers(tuples, 0,1,2,6,None,None,None,None)

find_tuples_with_two_numbers(tuples, 6,9,5,8,10,11,7,None)



/********************************

array_mado = []


def find_tuples_with_two_numbers(array_mado,tuples, a, b, c,d,e,f,g,h):

     Num  = 0 ;

     for t in tuples:

   

           count = 0

           if a in t:

               count += 1

           if b in t:

               count += 1

           if c in t:

               count += 1



           if d != None:      

                if d in t :

                   count +=1   



           if e != None:      

                if e in t :

                    count +=1   



           if f != None:      

                if f in t :

                    count +=1   



           if g != None:      

                if g in t :

                    count +=1   



           if h != None:      

                if h in t :

                    count +=1   

                   

           if count >= 2:

                print(Num)

                print(t)

                array_mado.append(Num)
           Num += 1 

           
    # for k in array_mado:
         #  print("{}-".format(k))      
      #print("\n")  
    
tuples = [(0, 2), (0, 1), (1, 2), (1, 5), (2, 5), (0, 6), (2, 6), (1, 3), (3, 5), (0, 4), (4, 6), (2, 9),

 (5, 9), (6, 9), (3, 8), (5, 8), (4, 7), (6, 7), (7, 11), (10, 11), (8, 10), (1, 10), (0, 11), (14, 17), 

 (14, 15), (15, 16), (16, 17), (12, 19), (12, 13), (13, 18), (18, 19), (22, 23), (22, 24), (23, 24), 

 (25, 27), (25, 26), (26, 27)] 

#find_tuples_with_two_numbers(tuples, 0,1,2,None)



#find_tuples_with_two_numbers(tuples, 0,1,2,6,None,None,None,None)




    
            
find_tuples_with_two_numbers(array_mado,tuples, 6,9,5,8,10,11,7,None)

for k in array_mado:
           print("{}-".format(k))  
           
           
#arr =[2,6,8,4,5]
def set_bits_from_list(numbers):
    pop = 0
    for num in numbers:
        pop |= (1 << num)
    return pop
print(set_bits_from_list(array_mado))


def Split(kam):
    s1 = (kam >> 0)& 0xff
    print(s1)
    s2 =(kam >>  8) & 0xff
    print(s2)
    s3 = (kam >> 16) & 0xff
    print(s3)
    s4 = (kam >>24)& 0xff
    print(s4)
    
    print("{} - {} - {} - {}   \n".format(bin(s4),bin(s3),bin(s2),bin(s1)))
    
    print(f"{s4:b} - {s3:b} - {s2:b} - {s1:b}")
    
Split(set_bits_from_list(array_mado))    
    

