def vowel_or_not():
    print("Enter only one alphabet")
    character=str(input("Enter :"))
    vowels='A','a','E','e','I','i','O','o','U','u'
    if character in vowels:
        print("The given character is vowel ")
    else:
        print("The given character is not vowel")
vowel_or_not()
