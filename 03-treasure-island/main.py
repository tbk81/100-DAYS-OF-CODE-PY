print(r'''
                                           .""--.._
                                           []      `'--.._
                                           ||__           `'-,
                                         `)||_ ```'--..       \
                     _                    /|//}        ``--._  |
                  .'` `'.                /////}              `\/
                 /  .""".\              //{///    
                /  /_  _`\\            // `||
                | |(_)(_)||          _//   ||
                | |  /\  )|        _///\   ||
                | |L====J |       / |/ |   ||
               /  /'-..-' /    .'`  \  |   ||
              /   |  :: | |_.-`      |  \  ||
             /|   `\-::.| |          \   | ||
           /` `|   /    | |          |   / ||
         |`    \   |    / /          \  |  ||
        |       `\_|    |/      ,.__. \ |  ||
        /                     /`    `\ ||  ||
       |           .         /        \||  ||
       |                     |         |/  ||
       /         /           |         (   ||
      /          .           /          )  ||
     |            \          |             ||
    /             |          /             ||
   |\            /          |              ||
   \ `-._       |           /              ||
    \ ,//`\    /`           |              ||
     ///\  \  |             \              ||
    |||| ) |__/             |              ||
    |||| `.(                |              ||
    `\\` /`                 /              ||
       /`                   /              ||
      /                     |              ||
     |                      \              ||
    /                        |             ||
  /`                          \            ||
/`                            |            ||
`-.___,-.      .-.        ___,'            ||
         `---'`   `'----'`

''')

print("Welcome to Treasure Island\nYour mission is to find the treasure.")

choice = input("You're at a crossroad. Where do you want to go?\nType left or right.\n").lower()

if choice == "left":
    print("You've come to a lake. There is an island in the middle of the lake")
    choice = input("Type \"wait\" to wait for a boat or type \"swim\" to swim across\n").lower()
    if choice == "wait":
        print("You've come to 3 colored doors. red, blue, and yellow").lower()
        choice = input("Type \"red\", \"blue\", \"yellow\"\n")
        if choice == "red":
            print("You faced the grim reaper and died")
        elif choice == "blue":
            print("You were mauled by a bear")
        else:
            print("You found the treasure!")
    else:
        print("You were eaten by a shark")
else:
    print("You fell off a cliff and died!")