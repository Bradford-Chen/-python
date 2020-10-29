# 陈祥锡 信管19-1 2019312256
# 2020/9/29

def main():
    s = input("Please input a phrase:")
    s1 = s.title()
    list1 = s1.split()
    for i in range(0, len(list1)):
        print(list1[i][0], end="")

    print("\n**********************\n")


main()


####

def main():
    plaintext = input("Please input the plaintext:")
    key = int(input("Please input the key:"))
    for ch in plaintext:
        print(chr(ord(ch) + key), end="")

    print("\n**********************\n")


main()


####

def main():
    s = input("Please input a sentence: ")
    s1 = s.split()
    a = 0
    for i in range(0, len(s1)):
        a = a + len(s1[i])

    print("The average length of word: ", a/len(s1))
    print("\n**********************\n")


main()

