# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("YWhat is your age? "))
#     if 45 <= age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     elif age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#
#     print(f"Your final bill is {bill}")
#
# else:
#     print("Sorry, you have to grow taller before you can ride.")

print('''
                         _.._           
                  __.--"" __ ""--.__    
                .'//   .-"  "-.   \\`,  
               : :'  .'.  :;  ,`.  `; ; 
              /; ;  /  T. $$ ,P  \  : : 
             /: :  ;    T.:;,P    :  ; ;
             )| | :      `  '      ; | |
             `j | :.--------------.: | |
              ; ; |                | : :
              ; ; |                | : :
              | | |                | | |
              | | |                | | |
              : : |                | ; ;
              : : :________________: ; ;
               ; ;__    _...._    __: : 
               | ;  "-./ ,--, \,-"  : | 
               | '._   \ ;  : /   _.' | 
               :  __`-. `."",' .-'__  ; 
                ;`.__> `.J__L.' <__.':  
                ;.--._   .--.   _.--,:  
                |`.__.' `.__.' `.__.'|  
                |.--._   .--.   _.--,|  
                |`.__.' `.__.' `.__.'|  
                |.--._   .--.   _.--,|  
                ;`.__.' `.__.' `.__.':  
               : .--._   .--.   _.--, ; 
               ; `.__.' `.__.' `.__.' : 
               ;                      : 
               '--..__          __..--' 
                      """"""""""    
''')
print("Welcome to Lost Island.")
print("Your mission is to find the phone and then to call for a rescue.")

choice_1 = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\".\n").lower()

if choice_1 == "left":
    print("You found out that island isn't fully abandoned. There were poisonous snakes. You are dead x_x")
else:
    choice_2 = input("You come to the big red castle. Probably the phone is inside the castle. "
                     "But how knows is it true and how creatures there are. \nType \"go\" to go inside the castle. "
                     "Type \"circumvent\" to get around the building and find another way to the phone.\n").lower()
    if choice_2 == "go":
        print("You decided to go inside the castle. Stepping in the dark you didn't notice a big hole in the floor. "
              "You fell in it. You are dead x_x")
    else:
        choice_3 = input("You are stepping in the rainforest. "
                         "Suddenly you head a song of Adele \"Set fire to the rain\" from the nearest tree.\n"
                         "Type \"inside\" to look inside the big nest in the tree and probably find the phone.\n"
                         "Type \"outside\" to look outside the tree and probably find the phone.\n"
                         "Type \"forward\" to go straight forward into the forest because this "
                         "song is just in your head.\n").lower()
        if choice_3 == "inside":
            print("You found out the phone and some food. You called to the emergency and finally returned home. "
                  "Congratulations!")
        elif choice_3 == "forward":
            print("You went into the dragon nest. You are dead x_x")
        else:
            print("You were crushed by a fallen tree branch while you were looking at a place near the tree. "
                  "You are dead x_x")