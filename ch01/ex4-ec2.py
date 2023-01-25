def string_triangle(str_value):
    str_list = list(str_value) 
    for x, letter in enumerate(str_list):
        print(letter * (x + 1))

def main():
    name = input("Enter your name: ")
    string_triangle(name)

if __name__ == "__main__":
    main()
