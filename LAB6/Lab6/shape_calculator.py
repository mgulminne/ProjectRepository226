import geometry_utils

def main():
    print("Available shapes: circle, rectangle, triangle")
    print("Available calculations: Area, Perimeter")

    operation = input("Enter the operation you want like: circle_area").strip().lower()

   # if-else yerine dictionary kullanıyoruz
    operations_dic = {
       "circle_area": geometry_utils.circle_area,
       "circle_perimeter": geometry_utils.circle_perimeter,
       "rectangle_area": geometry_utils.rectangle_area(),
       "rectangle_perimeter": geometry_utils.rectangle_perimeter,
       "triangle_area": geometry_utils.triangle_area(),
    }

    if operation not in operations_dic:
        print(" Operation must be in operations")
        return


    #operation: triangle area operationsdic=0,5*a*b  function = trianglearea(a,b)
    function = operations_dic[operation]

    try:
        if "circle" in operation:
            r = float(input("Enter the radius of the circle: "))
            result = function(r)
        elif "rectangle" in operation:
            a = float(input("Enter the a(width): "))
            b = float(input("Enter the b(height): "))
            result = function(a, b)
        elif "triangle" in operation:
            base = float(input("Enter the base: "))
            height = float(input("Enter the height: "))
            result = function(base, height)
        print("Result: ", result)

    except ValueError as e:
        if "could not convert" in str(e):
            print("Input Error: Please enter numeric values.")
        else:
            print(f"Input Error: {e}")

if __name__ == "__main__":
    main()
