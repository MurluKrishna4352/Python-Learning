#pythagorus theorem

print("\n PYTHAGORUS  THEOREM ") 

# repeatition

calculate = int(input("how_many_times_do_you_want_to_repeat_this_calculation: "))

for i in range(calculate):
     
     user_find  = str(input("\n what_do_you_want_to_find: ")) #  user input what to find
   #  if (user_find != "perpendicular" or user_find != "hypotenuse" or user_find != "base"):
        #  print("please_enter_a_valid_input")
          

    # perpendicular = ""
    # hypotenuse = ""
    # base = ""

     #perpendicular

     if (user_find == "perpendicular"):
          hypotenuse_var = float(input("\n Enter_the_length_of_hypotenuse: "))
          base_var = float(input("Enter_the_length_of_base: "))
          print("\n here is your perpendicular: ")
          print("answer without puthing root: "  ,  (hypotenuse_var**2 - base_var**2))
          print("answer with root: " ,   (hypotenuse_var**2 - base_var**2)**0.5)


     # hypotenuse

     if (user_find == "hypotenuse"):
          perpendicular_var = float(input("\n Enter_the_length_of_perpendicular: "))
          base_var = float(input("Enter_the_length_of_base: "))
          print("\n here is your hypotenuse: ")
          print("answer without puthing root: "  ,  (perpendicular_var**2 + base_var**2))
          print("answer with root: " ,   (perpendicular_var**2 + base_var**2)**0.5)


     # base

     if (user_find == "base"):
          perpendicular_var = float(input("\n Enter_the_length_of_perpendicular: "))
          hypotenuse_var = float(input("Enter_the_length_of_hypotenuse: "))
          print("\n here is your base: ")
          print("answer without puthing root: "  ,  (hypotenuse_var**2 - perpendicular_var**2))
          print("answer with root: " ,  (hypotenuse_var**2 - perpendicular_var**2)**0.5)

