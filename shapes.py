import math

def circle (r):
    area=(math.pi)*r**2
    print("the value of the area is : ", area)
    return area
def triangle (b,h):
    area = (b*h)/2
    print("the area of the triangle is ", area)
    return area
def rect(br,hr):
    area = br*hr
    print("the area of the rectangular is ", area)
    return area
def sqr (size):
    area = size**2
    print("the area of the square is ", area)

if __name__ == "__main__":
    #area of triangle
    print("shapes program")
    r = float(input(f"insert the radius :"))
    circle(r)
    #area of triangle
    print("triangle area program")
    b=float(input("insert base of triangle: "))
    h = float(input("insert height of triangle: "))
    triangle(b,h)
    ##area for recatangular
    br = float(input("insert base of rectangular: "))
    hr = float(input("insert height of rectangular: "))
    rect(br, hr)
    ##area for square
    size=float(input("insert size of the square:"))
    sqr(size)








