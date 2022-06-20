import DataContext as Dc

print("welcome to this application")

decide = int(input("what are you looking for 1.everything 2.Specific season"))

if decide == 1:
    Dc.main()

elif decide == 2:
    Dc.main()

else:
    print("you have not entered a valid response to the question")
