n = int(input("Enter n: ").strip());

if n%2 != 0 or (6<=n<=20 and n%2 == 0):
    print("Wierd");

if n%2 == 0 and (2<=n<=5 or n>20):
    print("Not Wierd");
