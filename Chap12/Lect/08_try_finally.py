# its use basicaly come in function

def main():
  try:
    a = int(input("Enter The number : "))
    print(a)
    return

  except Exception as e:
    print(e)
    return

  finally:
    print("hye i am inside a finally")

main()

# its working even we return use