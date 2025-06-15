nums =[]
i = 0
while i < 3:
    num = int(input("Enter a number: "))
    nums.append(num)
    print(nums)
    i += 1
want = input("Do you want the last number to be saved? (yes/no) ").lower()
if want == "no":
    del nums[-1]
print(f"The numbers you have entered are: {nums}")