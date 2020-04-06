#!/usr/bin/python3
def main():
    print('here')
    num = 2000
    total = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            total = total + i
    print(total)
    
if __name__ == '__main__':
    main()
