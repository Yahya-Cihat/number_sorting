def main():
    with open('C:\\Users\\Cihat\\Desktop\\hello.txt') as file:
        x = file.read()
        firstline = x[0:13]
        secondline = x[14:27]
        thirdline = x[28:41]
        fourthline = x[42:55]
        fifthline = x[56:69]
        numbers = [firstline,secondline,thirdline,fourthline,fifthline]
        a = sorted(numbers)
        num1 = a[0]
        num2 = a[1]
        num3 = a[2]
        num4 = a[3]
        num5 = a[4]
        b = str(num1)+"\n"+str(num2)+"\n"+str(num3)+"\n"+str(num4)+"\n"+str(num5)
    with open('C:\\Users\\Cihat\\Desktop\\hello.txt','w') as file:
        file.write(b)
    print("done")

if __name__ == "__main__":
    main()
