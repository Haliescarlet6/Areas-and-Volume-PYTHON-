#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

print("Hello, welcome to AREAS HUB")
figure = str(input("Enter the name of the figure you want to find the area or volume : "))

#SQUARE#
if figure == "square":
    print("What do you need to find the area of the square or the perimeter ?")
    userans = str(input("area / perimeter : "))
    if userans == "area":
        print("What is given in the question the side or the diagonal of the square ?")
        userans2 = str(input("side / diagonal : "))
        if userans2 == "side":
            side = int(input("Enter the value of the side (NO UNITS): "))
            area = side ** 2
            print("The area of the square with side",side,"unit is :",area)
            print("Thank You")
        elif userans2 == "diagonal":
            diagonal = int(input("Enter the value of the diagonal(NO UNITS) : "))
            area = (d * d)/2
            print("The area of the square with diagonal",diagonal,"units is :",area)
            print("Thank You")
                        
    elif userans == "perimeter":
        print("What is given in the question the side or the diagonal of the square ?")
        userans2 = str(input("side / diagonal : "))
        if userans2 == "side":
            side = int(input("Enter the value of the side (NO UNITS): "))
            perimeter = side * 4
            print("The area of the square with side",side,"unit is :",perimeter)
            print("Thank You")
        elif userans2 == "diagonal":
            diagonal = int(input("Enter the value of the diagonal(NO UNITS) : "))
            perimeter = 2.82 * d
            print("The perimeter of the square with diagonal",diagonal,"units is :",permeter)
            print("Thank You")
            
            
            
            
#RECTANGLE#
if figure =="rectangle":
    print("What do you need to find the area of the rectangle or the perimeter ?")
    userans = str(input("area / perimeter : "))
    if userans == "area":
        print("What is given in the question the sides or the diagonal of the square ?")
        userans2 = str(input("side / diagonal : "))
        if userans2 == "side":
            side1 = int(input("Enter the value of the length (NO UNITS): "))
            side2 = int(input("Enter the value of the breadth (NO UNITS): "))
            area = side1  * side2
            print("The area of the rectangle with side",side1,"and",side2,"unit is :",area)
            print("Thank You")
        elif userans2 == "diagonal":
            d = int(input("Enter the value of the diagonal(NO UNITS) : "))
            side1 = int(input("Enter the value of the one of the side (NO UNITS): "))
            step1 = (d*d) - (side1*side1)
            step2 = math.sqrt(step1)
            step3 = side1 * step2
            area = step3
            print("The area of the square with diagonal",diagonal,"units is :",area)
            print("Thank You")
            
    if userans == "perimeter":
        print("What is given in the question the sides or the diagonal of the square ?")
        userans2 = str(input("side / diagonal : "))
        if userans2 == "side":
            side1 = int(input("Enter the value of the length (NO UNITS): "))
            side2 = int(input("Enter the value of the breadth (NO UNITS): "))
            perimeter = 2*(side1  + side2)
            print("The area of the rectangle with side",side1,"and",side2,"unit is :",perimeter)
            print("Thank You")
        elif userans2 == "diagonal":
            d = int(input("Enter the value of the diagonal(NO UNITS) : "))
            side1 = int(input("Enter the value of the one of the side (NO UNITS): "))
            step1 = (d*d) - (side1*side1)
            step2 = math.sqrt(step1)
            step3 = 2 * step2
            perimeter =  (2*side1) - step3
            print("The area of the square with diagonal",diagonal,"units is :",perimeter)
            print("Thank You")
            
            
            
            
#TRIANGLE#
if figure =="triangle":
    print("What do you need to find the area of the rectangle or the perimeter ?")
    userans = str(input("area / perimeter : "))
    if userans == "area":
        print("What is given in the question the sides or the base and height of the rectangle ?")
        userans2 = str(input("side / bh : "))
        if userans2 == "side":
            s1 = int(input("Enter the value of the side 1 (NO UNITS): "))
            s2 = int(input("Enter the value of the side 2 (NO UNITS): "))
            s3 = int(input("Enter the value of the side 3 (NO UNITS): "))
            s = (s1 + s2 + s3) / 2
            step2 = (s*(s-s1)*(s-s2)*(s-s3))
            step3 = math.sqrt(step2)
            area = step3
            print("The area of the triangle is :",area)
            print("Thank You")
        elif userans2 == "bh":
            b = int(input("Enter the value of the breadth(NO UNITS) : "))
            h = int(input("Enter the value of the height(NO UNITS): "))
            step1 = b * h
            step2 = (1/2) * step1
            area = step2
            print("The area of the triangle is :",area)
            print("Thank You")
    
    elif ueserans == "perimeter":  
        s1 = int(input("Enter the value of the side 1 (NO UNITS): "))
        s2 = int(input("Enter the value of the side 2 (NO UNITS): "))
        s3 = int(input("Enter the value of the side 3 (NO UNITS): "))
        s = (s1 + s2 + s3)
        perimeter = s
        print("The perimeter of the triangle is : ", perimeter)
        print("Thank You")
            
           
        
        
#CIRCLE#
elif figure =="circle":
    print("Do you want to find the area or the circumfrence of the circle ?")
    userans = str(input("area / circumfrence : "))
    if userans == "area":
        print("What is the radius of the circle ?")
        r = int(input("Enter the value of the radius (NO UNITS): "))
        area = (22 * r * r) / 7
        print("The area of the circle with radius",r,"units is : ",area)
        print("Thank You")
        
    elif userans =="circumfrence":
        print("What is the radius of the circle ?")
        r = int(input("Enter the value of the radius (NO UNITS): "))
        circumfrence = (44 * r ) / 7
        print("The circumfrence of the circle is :",circumfrence)
        print("Thank You")
        
        
        
        
#PARALLELLOGRAM#
if figure == "parallelogram":
    print("What do you need to find the area of the parellogram or the perimeter ?")
    userans = str(input("area / perimeter : "))
    if userans == "area":
        b = int(input("Enter the value of the base (NO UNITS): "))
        h = int(input("Enter the value of the height (NO UNITS): "))
        area = b * h
        print("The area of the parallelogram with is : ",area)
        print("Thank You")
        
        
    elif userans == "perimeter":
        print("NOTE THAT THE TWO SIDES SHOULD BE ADJACENT")
        s1 = int(input("Enter the value of the side 1 (NO UNITS): "))
        s2 = int(input("Enter the value of the side 2 (NO UNITS): "))
        perimeter = 2 *(s1 + s2)
        print("The perimeter of the parallelogram is : ", perimeter)
        print("Thank You")
        
        
        
        
#RHOMBUS#
if figure =="rhombus":
    print("What do you need to find the area of the rhombus or the perimeter ?")
    userans = str(input("area / perimeter : "))
    if userans == "area":
        d1 = int(input("Enter the value of the diagonal 1 (NO UNITS): "))
        d2 = int(input("Enter the value of the diagonal 2 (NO UNITS): "))
        area = (d1 * d2) / 2
        print("The area of the parallelogram with is : ",area)
        print("Thank You")
        
    elif userans == "perimeter":
        print("NOTE THAT THE TWO SIDES SHOULD BE ADJACENT")
        s1 = int(input("Enter the value of the side 1 (NO UNITS): "))
        s2 = int(input("Enter the value of the side 2 (NO UNITS): "))
        perimeter = 2 *(s1 + s2)
        print("The perimeter of the rhombus is : ", perimeter)
        print("Thank You")
        
        
        
        
#CUBE#
if figure =="cube":
    print("Do you want to find the surface area or the volume of the cube ?")
    userans = str(input("sa / volume : "))
    if userans == "sa":
        print("Do you want to find the TSA or LSA ?")
        userans2 = str(input("tsa / lsa : "))
        if userans2 == "lsa":
            a = int(input("Enter the value of the side of the cube (NO UNITS): "))
            lsa = 4 * a * a
            print("The Lateral Surface Area(LSA) of the cube is:",lsa)
            print("Thank You")
        elif userans2 == "tsa":
            a = int(input("Enter the value of the side of the cube (NO UNITS): "))
            tsa = 6 * a * a
            print("The Total Surface Area(TSA) of the cube is:",tsa)
            print("Thank You")
            
    elif userans == "volume" :
        a = int(input("Enter the value of the side of the cube (NO UNITS): ")) 
        volume =  a **3
        print("The volume of the cube is :" , volume)
        print("Thank You")
        
        
        
        
#CUBOID#
if figure =="cuboid":
    print("Do you want to find the surface area or the volume of the cuboid ?")
    userans = str(input("sa / volume : "))
    if userans == "sa":
        print("Do you want to find the TSA or LSA ?")
        userans2 = str(input("tsa / lsa : "))
        if userans2 == "lsa":
            l = int(input("Enter the value of the length of the cuboid (NO UNITS): "))
            b = int(input("Enter the value of the breadth of the cuboid (NO UNITS): "))
            h = int(input("Enter the value of the height of the cuboid (NO UNITS): "))
            lsa = 2 * h *(l + b)
            print("The Lateral Surface Area(LSA) of the cuboid is:",lsa)
            print("Thank You")
        elif userans2 == "tsa":
            l = int(input("Enter the value of the length of the cuboid (NO UNITS): "))
            b = int(input("Enter the value of the breadth of the cuboid (NO UNITS): "))
            h = int(input("Enter the value of the height of the cuboid (NO UNITS): "))
            tsa = 2 * ((l*b)+(b*h)+(h*l))
            print("The Total Surface Area(TSA) of the cube is:",tsa)
            print("Thank You")
            
    elif userans == "volume" :
        l = int(input("Enter the value of the length of the cuboid (NO UNITS): "))
        b = int(input("Enter the value of the breadth of the cuboid (NO UNITS): "))
        h = int(input("Enter the value of the height of the cuboid (NO UNITS): "))
        volume =  l * b *h
        print("The volume of the cuboid is :" , volume)
        print("Thank You")
        
#CYLINDER#
if figure =="cylinder":
    print("Do you want to find the SA or the volume of the cylinder ?")
    userans = str(input("sa / volume : "))
    if userans =="sa":
        print("Do you want to find the TSA or CSA ?")
        userans2 = str(input("tsa / csa : "))
        if userans2 == "tsa":
            r = int(input("Enter the value of the radius of the cylinder (NO UNITS) : "))
            h = int(input("Enter the value of the height of the cylinder (NO UNITS): "))  
            step1 = (44 * r)
            step2 = (r + h)
            step3 = (step1 * step2) / 7
            tsa = step3
            print("The Total Surface Area(TSA) of the cylinder is:",tsa)
            print("Thank You")
        elif userans == "csa":
            r = int(input("Enter the value of the radius of the cylinder (NO UNITS) : "))
            h = int(input("Enter the value of the height of the cylinder (NO UNITS): "))  
            step1 = (44 * r * h)/7
            lsa = step1
            print("The Curved Surface Area(CSA) of the cylinder is:",lsa)
            print("Thank You")
            
    elif userans == "volume":
        r = int(input("Enter the value of the radius of the cylinder (NO UNITS) : "))
        h = int(input("Enter the value of the height of the cylinder (NO UNITS): "))  
        volume = ( 22 * r * r * h) / 7
        print("The volume of the cylinder is :" , volume)
        print("Thank You")
        
        
        
        
#CONE#
if figure == "cone":
    print("Do you want to find the SA or the volume of the cone ?")
    userans = str(input("sa / volume : "))
    if userans =="sa":
        print("Do you want to find the TSA or CSA ?")
        userans2 = str(input("tsa / csa : "))
        if userans2 == "tsa":
            r = int(input("Enter the value of the radius of the cone (NO UNITS) : "))
            l = int(input("Enter the value of the slant height of the cone (NO UNITS): ")) 
            step1 = (22 * r ) / 7
            step2 = (r + l)
            step3 = step1 * step2
            tsa = step3
            print("The Total Surface Area(TSA) of the cone is:",tsa)
            print("Thank You")
        elif userans2 == "csa":
            r = int(input("Enter the value of the radius of the cone (NO UNITS) : "))
            l = int(input("Enter the value of the slant height of the cone (NO UNITS): ")) 
            lsa = (22 * r * l ) / 7
            print("The Curved Surface Area(CSA) of the cone is:",lsa)
            print("Thank You")
            
    elif userans == "volume":
        r = int(input("Enter the value of the radius of the cone (NO UNITS) : "))
        h = int(input("Enter the value of the height of the cone (NO UNITS): "))
        volume = (22 * r * r * h)/21
        print("The volume of the cone is :" , volume)
        print("Thank You")
        
        
        
        
#SPHERE#
if figure =="sphere":
    print("Do you want to find the SA or the volume of the sphere")
    userans = str(input("sa / volume : "))
    if userans == "sa":
        r = int(input("Enter the value of the radius of the sphere (NO UNITS) : "))
        tsa = (88 * r * r) / 7
        print("The Total Surface Area(TSA) of the sphere is:",tsa)
        print("Thank You")
        
    elif userans == "volume":
        r = int(input("Enter the value of the radius of the sphere (NO UNITS) : "))
        volume = (88 * r * r * rf) / 21
        print("The volume of the sphere is :" , volume)
        print("Thank You")
            
            
            
            
#HEMISPHERE#
if figure == "hemisphere":
    print("Do you want to find the SA or the volume of the hemisphere ?")
    userans = str(input("sa / volume : "))
    if userans == "sa":
        print("Do you want to find the TSA or CSA ?")
        userans2 = str(input("tsa / csa : "))
        if userans2 == "tsa":
            r = int(input("Enter the value of the radius of the sphere (NO UNITS) : "))
            tsa = (66 * r * r) / 7
            print("The Total Surface Area(TSA) of the hemisphere is:",tsa)
            print("Thank You")
        elif userans =="lsa":
            r = int(input("Enter the value of the radius of the sphere (NO UNITS) : "))
            tsa = (44 * r * r) / 7
            print("The Curved Surface Area(CSA) of the hemisphere is:",tsa)
            print("Thank You")
            
            


# In[ ]:





# In[ ]:




