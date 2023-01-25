def string_triangle(str_value):
    ''' takes a string and makes a triangle out of the letters... sort of '''
    str_list = list(str_value)
    for amplitude, letter in enumerate(str_list):
        print(letter * (amplitude + 1))

def main():
    name = input("Enter your name: ")
    string_triangle(name)

if __name__ == "__main__":
    main()
