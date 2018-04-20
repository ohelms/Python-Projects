#Checks if the character is lower case
def is_lower_101(char):
    limit=ord("Z")
    return (ord(str(char))) > limit

assert is_lower_101("A") == False
assert is_lower_101("J") == False
assert is_lower_101("V") == False
assert is_lower_101("a") == True
assert is_lower_101("f") == True
assert is_lower_101("n") == True


#Replaces a letter with another letter that is 13 letters away from it in the alphabet
def char_rot_13(char):
        chor=ord(char)
        places=13
        
        if char.isupper():
            if chor > ord("M"):
                chor = chor - places
            else:
                chor = chor + places

        elif char.islower():
            if chor > ord("m"):
                chor = chor - places
            else:
                chor = chor + places

        return chr(chor)

assert char_rot_13("a") == "n"
assert char_rot_13("b") == "o"
assert char_rot_13("c") == "p"
assert char_rot_13("A") == "N"
assert char_rot_13("B") == "O"
assert char_rot_13("C") == "P"


#Performs a ROT13 encryption for a string
def str_rot_13(mystr):
    string = ""
    for i in mystr:
        string=string+(char_rot_13(i))

    return string 

assert str_rot_13('python') == 'clguba'
assert str_rot_13('PYTHON') == 'CLGUBA'
assert str_rot_13('javascript') == 'wninfpevcg'
assert str_rot_13('JAVASCRIPT') == 'WNINFPEVCG'
assert str_rot_13('csharp') == 'pfunec'
assert str_rot_13('CSHARP') == 'PFUNEC'


#Replaces all instances of a specified letter in a string with a substitution letter
def str_translate_101(mystr,old,new):
    string = ""
    for i in mystr:
        if i == old:
            string = string + new
        else:
            string = string + i

    return string

assert str_translate_101("abcdcba","a","x") == 'xbcdcbx'
assert str_translate_101("qwertqwert","q","a") == 'awertawert'
assert str_translate_101("rtyuirtyui","y","p") == 'rtpuirtpui'
assert str_translate_101("uiopuiop","o","j") == 'uijpuijp'
assert str_translate_101("ghjkghjk","j","a") == 'ghakghak'
assert str_translate_101("vbnmvbnm","n","y") == 'vbymvbym'


#Adds two polynomials together
def poly_add2(poly1,poly2):
    newlist=[]
    newlist.append(int(poly1[0])+int(poly2[0]))
    newlist.append(int(poly1[1])+int(poly2[1]))
    newlist.append(int(poly1[2])+int(poly2[2]))
    return newlist

assert poly_add2([0,1,2],[3,4,5]) == [3,5,7]
assert poly_add2([1,2,3],[4,5,6]) == [5,7,9]
assert poly_add2([2,3,4],[5,6,7]) == [7,9,11]
assert poly_add2([3,4,5],[6,7,8]) == [9,11,13]
assert poly_add2([4,5,6],[7,8,9]) == [11,13,15]
assert poly_add2([5,6,7],[8,9,10]) == [13,15,17]


#Multiplies two polynomials together
def poly_mult2(poly1,poly2):
    newlist2=[]
    newlist2.append(int(poly1[0])*int(poly2[0]))
    newlist2.append(int(poly1[0])*int(poly2[1]) + int(poly1[1])*int(poly2[0]))
    newlist2.append(int(poly1[0])*int(poly2[2]) + int(poly1[1])*int(poly2[1]) + int(poly1[2])*int(poly2[0]))
    newlist2.append(int(poly1[1])*int(poly2[2]) + int(poly1[2])*int(poly2[1]))
    newlist2.append(int(poly1[2])*int(poly2[2]))
    return newlist2

assert poly_mult2([0,1,2],[3,4,5]) == [0, 3, 10, 13, 10]
assert poly_mult2([1,2,3],[4,5,6]) == [4, 13, 28, 27, 18]
assert poly_mult2([2,3,4],[5,6,7]) == [10, 27, 52, 45, 28]
assert poly_mult2([3,4,5],[6,7,8]) == [18, 45, 82, 67, 40]
assert poly_mult2([4,5,6],[7,8,9]) == [28, 67, 118, 93, 54]
assert poly_mult2([5,6,7],[8,9,10]) == [40, 93, 160, 123, 70]