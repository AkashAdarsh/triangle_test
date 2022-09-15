
def triangle_type(a,b,c):
    print("Enter lenghts of triangle sides:")
    if a<0 or b<0 or c<0:
        return "its an error"
    else:
        if a+b>c and a+c>b and b+c>a:
            if a==b==c:
                return "its equilateral"
            elif a==b or a==c or b==c:
                return "its isosceles"
            else:
                return "its scalene"
        else:
            return "its an error"