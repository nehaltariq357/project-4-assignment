# Write a function that takes two numbers and finds the average between the two.

def average(num1:float,num2:float):
    sum= num1 + num2 
    return sum /2



def main():
    avg_1 = average(5,10)
    avg_2 = average(6,8)
    final = average(avg_1,avg_2)
    print("avg_1", avg_1)
    print("avg_2", avg_2)
    print("final", final)

if __name__ == '__main__':
    main()