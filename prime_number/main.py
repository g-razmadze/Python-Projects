def prime_number():
      nums = (input("Please enter comma-seperated numbers: ")).split(",")
      for num in nums:
          num = int(num)
          if num > 1:
              for i in range(2, int(num/2)+1):
                  if (num % i) == 0:
                      print(num, "is not a prime number")
                      break
              else:
                  print(num, "is a prime number")
          else:
              print(num, "is not a prime number")

def main():
    prime_number()


if __name__ == "__main__":
    main()
