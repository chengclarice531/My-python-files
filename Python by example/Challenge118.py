def enter_num():
    num = int(input("Enter a number: "))
    return num
def count_num(num):
    i = 1
    while i <= num:
        print(i)
        i += 1
def main():
    num = enter_num()
    count_num(num)
main()