#                                                           ideas/scrapped ideas
# nested if else loops
# storing information in dictionaries and indexing them to their values
# find out how to use format specifiers to find levels of pokemon and other shit
# define items into functions(potions,)
# make a gym leader randomizer
# you can win the game by using specific types of pokemon to win against specific types of gym leaders
# very effective moves will win the gym battle
# winning the game requires you to beat all the gym leaders
# pop the gym leader off if you beat him
# print a pokemon champions trophy in the end if you win
# probability win by computer according to weaknesses
# types levels probability preference
import random as rd
starting_pokemon = ["charmander","bulbasaur","squirtle"]
gym_badges = 0
pokemon_choices= ["bulbasaur","ivysaur","venusaur","charmander","charmeleon","charizard","squirtle","wartortle","blastoise","caterpie","metapod","butterfree","weedle","kakuna","beedrill","pidgey","pidgeotto","pidgeot","rattata","raticate","spearow","fearow","ekans","arbok","pikachu","raichu","sandshrew","sandslash","nidoran♀","nidorina","nidoqueen","nidoran♂","nidorino","nidoking","clefairy","clefable","vulpix","ninetales","jigglypuff","wigglytuff","zubat","golbat","oddish","gloom","vileplume","paras","parasect","venonat","venomoth","diglett","dugtrio","meowth","persian","psyduck","golduck","mankey","primeape","growlithe","arcanine","poliwag","poliwhirl","poliwrath","abra","kadabra","alakazam","machop","machoke","machamp","bellsprout","weepinbell","victreebel","tentacool","tentacruel","geodude","graveler","golem","ponyta","rapidash","slowpoke","slowbro","magnemite","magneton","farfetch’d","doduo","dodrio","seel","dewgong","grimer","muk","shellder","cloyster","gastly","haunter","gengar","onix","drowzee","hypno","krabby","kingler","voltorb","electrode","exeggcute","exeggutor","cubone","marowak","hitmonlee","hitmonchan","lickitung","koffing","weezing","rhyhorn","rhydon","chansey","tangela","kangaskhan","horsea","seadra","goldeen","seaking","staryu","starmie","mr. mime","scyther","jynx","electabuzz","magmar","pinsir","tauros","magikarp","gyarados","lapras","ditto","eevee","vaporeon","jolteon","flareon","porygon","omanyte","omastar","kabuto","kabutops","aerodactyl","snorlax","articuno","zapdos","moltres","dratini","dragonair","dragonite","mewtwo","mew"]
pokemon= ["bulbasaur","ivysaur","venusaur","charmander","charmeleon","charizard","squirtle","wartortle","blastoise","caterpie","metapod","butterfree","weedle","kakuna","beedrill","pidgey","pidgeotto","pidgeot","rattata","raticate","spearow","fearow","ekans","arbok","pikachu","raichu","sandshrew","sandslash","nidoran♀","nidorina","nidoqueen","nidoran♂","nidorino","nidoking","clefairy","clefable","vulpix","ninetales","jigglypuff","wigglytuff","zubat","golbat","oddish","gloom","vileplume","paras","parasect","venonat","venomoth","diglett","dugtrio","meowth","persian","psyduck","golduck","mankey","primeape","growlithe","arcanine","poliwag","poliwhirl","poliwrath","abra","kadabra","alakazam","machop","machoke","machamp","bellsprout","weepinbell","victreebel","tentacool","tentacruel","geodude","graveler","golem","ponyta","rapidash","slowpoke","slowbro","magnemite","magneton","farfetch’d","doduo","dodrio","seel","dewgong","grimer","muk","shellder","cloyster","gastly","haunter","gengar","onix","drowzee","hypno","krabby","kingler","voltorb","electrode","exeggcute","exeggutor","cubone","marowak","hitmonlee","hitmonchan","lickitung","koffing","weezing","rhyhorn","rhydon","chansey","tangela","kangaskhan","horsea","seadra","goldeen","seaking","staryu","starmie","mr. mime","scyther","jynx","electabuzz","magmar","pinsir","tauros","magikarp","gyarados","lapras","ditto","eevee","vaporeon","jolteon","flareon","porygon","omanyte","omastar","kabuto","kabutops","aerodactyl","snorlax","articuno","zapdos","moltres","dratini","dragonair","dragonite","mewtwo","mew"]
pokemon_types = ["grass","grass","grass","fire","fire","fire","water","water","water","bug","bug","bug","bug","bug","bug","normal","normal","normal","normal","normal","normal","normal","poison","poison","electric","electric","ground","ground","poison","poison","poison","poison","poison","poison","fairy","fairy","fire","fire","normal","normal","poison","poison","grass","grass","grass","bug","bug","bug","bug","ground","ground","normal","normal","water","water","fighting","fighting","fire","fire","water","water","water","psychic","psychic","psychic","fighting","fighting","fighting","grass","grass","grass","water","water","rock","rock","rock","fire","fire","water","water","electric","electric","normal","normal","water","water","poison","poison","water","water","ghost","ghost","ghost","rock","psychic","psychic","water","water","electric","electric","grass","grass","ground","ground","fighting","fighting","normal","poison","poison","ground","ground","normal","grass","normal","water","water","water","water","water","water","psychic","bug","ice","electric","fire","bug","normal","water","water","water","normal","normal","water","electric","fire","normal","rock","rock","rock","rock","rock","normal","ice","electric","fire","dragon","dragon","dragon","psychic","psychic"]
pokedex = [None,None,None,None,None,None]
gym_leaders = ["Brock","Misty","Lt. Surge","Erika","Koga","Sabrina","Blaine","Giovanni"]
battle_number_range = [1,2,3,4,5,6,7,8]
brock_weaknesses = ["water","ground","grass","fighting"]
misty_weaknesses = ["electric","grass"]
ltsurge_weaknesses = ["ground"]
erika_weaknesses = ["flying","fire","bug","ice","poison"]
koga_weaknesses = ["psychic","ground"]
sabrina_weaknesses = ["ghost","bug"]
blaine_weaknesses = ["water","ground","rock"]
giovanni_weaknesses = ["water","ice","grass"]
bag = {}
print("\n Welcome to the world of pokémon! My name is Oak! People call me the pokémon Prof! This world is inhabited by creatures called pokémon! \n In this universe you will meet pokemon and form strong bonds and fight other pokemon trainers. \n ")
ready = input("are you ready to join this universe of pokemon creatures? (yes/no)").lower()

if ready == "yes":
    print("Welcome to the world of Pokemon\n")
    for i in range (0,6):
         pokemon_choice = input("What Pokemon do you want to want to join your squad?(%d) (Type any Kanto Pokemon)" % (i+1)).lower()
         if pokemon_choice not in pokemon:
              print("Please select a Pokemon which is in the Pokedex. ")
         elif pokemon_choice in pokemon:
          pokedex[i] = pokemon_choice
    print(pokedex)
    bank = 100000
    # shop = input("What would you like to have in your bag?, you have %d Pokédollars! \n you can purchase: \n potion \n coffee " % bank)
    #buy stuff subtract money
    gym_time = input("Are you ready to face the Gym Leaders of the Kanto region?, you cannot go back to the pokemon selection sequence again (yes/no) ")
    
    if gym_time == "yes":
         print("The gym leaders of the Kanto region are fierce and have specialized in various types of Pokemon. You will need to carefully pick Pokemon that are suited for these battles")
         while gym_badges != 8:
              battle_number = rd.choice(battle_number_range)
              #Brock
              if battle_number == 1:
                   print("You have challenged the gym leader of Pewter City, Brock.\n Brock is a leader who specializes in rock type pokemon \n The weaknesses of Rock Pokemon include Water,Ground,Fighting,Grass\n")
                   print(pokedex)
                   pokemon_for_brock = input("Which pokemon would you like to choose?\n ")
                   if pokemon_for_brock in pokedex:
                        print("Brock has pulled out his giant 210 kgs Onix and you have chosen %s " % pokemon_for_brock)
                        if pokemon_types[pokemon.index(pokemon_for_brock)].lower() in brock_weaknesses: 
                             #i dont know what the issue is but why doesnt this work? the index im refering to is corresponding to the chosen pokemon's type and comparing it to the weakness of the types
                             print("Your %s has super effective moves against Brock's Onix, You will easily defeat him \n Onix fainted! \n" % pokemon_for_brock)
                             gym_badges += 1
                             print("You have won the Boulder Badge! %d/8\n" % gym_badges)
                             bank + 20000
                             gym_leaders.remove("Brock")
                             battle_number_range.remove(battle_number)
                        else:
                             print("Your %s does not have any super effective moves against Brock's Onix, so you lost. \n You will get another oppurtunity to challenge Brock another day." % pokemon_for_brock)
                             bank - 10000
                             continue
                   elif pokemon_for_brock not in pokedex:
                        print("Please enter a Pokemon from your current Pokedex next time")
                        continue     
              #Misty
              elif battle_number == 2:
                   print("You have challenged the gym leader of Cerulean City, Misty.\n Misty is a leader who specializes in water type pokemon \n The weaknesses of Water Pokemon include Electric,Grass,")
                   print(pokedex)
                   pokemon_for_misty = input("Which pokemon would you like to choose?\n ")
                   if pokemon_for_misty in pokedex:
                        print("Misty has sent out her shiny yellow Starmie and you have chosen %s " % pokemon_for_misty)
                        if pokemon_types[pokemon.index(pokemon_for_misty)].lower() in misty_weaknesses:
                             print("Your %s has super effective moves against Misty's Starmie, You will easily beat him \n Starmie fainted! \n" % pokemon_for_misty)
                             gym_badges += 1
                             print("You have won the Cascade Badge! %d/8\n" % gym_badges)
                             bank + 20000
                             gym_leaders.remove("Misty")
                             battle_number_range.remove(battle_number)
                             continue
                        else:
                             print("Your %s does not have any super effective moves against Misty's Starmie, so you lost. \n You will get another oppurtunity to challenge Misty another day." % pokemon_for_misty)
                             bank - 10000
                             continue
                   elif pokemon_for_misty not in pokedex:
                        print("Please enter a Pokemon from your current Pokedex next time")
                        continue 
              #Lt. Surge 
              elif battle_number == 3:
                   print("You have challenged the gym leader of Vermillion City, Lt. Surge.\n Lt. Surge is a leader who specializes in Electric type pokemon and is a war veteran \n The weaknesses of Electric Pokemon include Ground")
                   print(pokedex)
                   pokemon_for_ltsurge = input("Which pokemon would you like to choose?\n ")
                   if pokemon_for_ltsurge in pokedex:
                        print("Lt. Surge has summoned his fat Raichu and you have chosen %s " % pokemon_for_ltsurge)
                        if pokemon_types[pokemon.index(pokemon_for_ltsurge)].lower() in ltsurge_weaknesses:
                             print("Your %s has super effective moves against Lt. Surge's Raichu, You will easily defeat him \n Raichu fainted! \n" % pokemon_for_ltsurge)
                             gym_badges += 1
                             print("You have won the Thunder Badge! %d/8\n" % gym_badges)
                             bank + 20000
                             gym_leaders.remove("Lt. Surge")
                             battle_number_range.remove(battle_number)
                             continue
                        else:
                             print("Your %s does not have any super effective moves against Lt. Surge's Raichu, so you lost. \n You will get another oppurtunity to challenge Surge another day." % pokemon_for_ltsurge)
                             bank - 10000
                             continue
                   elif pokemon_for_ltsurge not in pokedex:
                        print("Please enter a Pokemon from your current Pokedex next time")
                        continue     
              #Erika 
              elif battle_number == 4:
                   print("You have challenged the gym leader of Celadon City, Erika.\n Erika is a leader who specializes in Grass type pokemon \n The weaknesses of Grass Pokemon include Fire,Flying,Ice,Poison,Bug")
                   print(pokedex)
                   pokemon_for_erika = input("Which pokemon would you like to choose? ")
                   if pokemon_for_erika in pokedex:
                        print("Erika unleashed her big Vileplume and you have chosen %s " % pokemon_for_erika)
                        if pokemon_types[pokemon.index(pokemon_for_erika)].lower() in erika_weaknesses:
                             print("Your %s has super effective moves against Erika's Vileplume, You will easily defeat her \n Vileplume fainted! \n" % pokemon_for_erika)
                             gym_badges += 1
                             print("You have won the Rainbow Badge! %d/8\n" % gym_badges)
                             bank + 20000
                             gym_leaders.remove("Erika")
                             battle_number_range.remove(battle_number)
                             continue
                        else:
                             print("Your %s does not have any super effective moves against Erika's Vileplume, so you lost. \n You will get another oppurtunity to challenge Erika another day." % pokemon_for_erika)
                             bank - 10000
                             continue
                   elif pokemon_for_erika not in pokedex:
                        print("Please enter a Pokemon from your current Pokedex next time")
                        continue  
              #Koga               
              elif battle_number == 5:
                   print("You have challenged the gym leader of Fuschia City, Koga.\n Koga is a leader who specializes in poison type pokemon \n The weaknesses of Poison Pokemon include Ground,Psychic")
                   print(pokedex)
                   pokemon_for_koga = input("Which pokemon would you like to choose? ")
                   if pokemon_for_koga in pokedex:
                        print("Koga brought Weezing into battle and you have chosen %s " % pokemon_for_koga)
                        if pokemon_types[pokemon.index(pokemon_for_koga)].lower() in koga_weaknesses:
                             print("Your %s has super effective moves against Koga's Weezing, You will easily defeat him \n Weezing fainted! \n" % pokemon_for_koga)
                             gym_badges += 1
                             print("You have won the Soul Badge! %d/8\n" % gym_badges)
                             bank + 20000
                             gym_leaders.remove("Koga")
                             battle_number_range.remove(battle_number)
                             continue  
                        else:
                             print("Your %s does not have any super effective moves against Koga's Weezing, so you lost. \n You will get another oppurtunity to challenge Koga another day." % pokemon_for_koga)
                             bank - 10000
                             continue
                   elif pokemon_for_koga not in pokedex:
                        print("Please enter a Pokemon from your current Pokedex next time")
                        continue   
              #Sabrina 
              elif battle_number == 6:
                   print("You have challenged the gym leader of Saffron City, Sabrina.\n Sabrina is a leader who specializes in psychic type pokemon \n The weaknesses of Psychic Pokemon include Ghost,Bug")
                   print(pokedex)
                   pokemon_for_sabrina = input("Which pokemon would you like to choose? ")
                   if pokemon_for_sabrina in pokedex:
                        print("Sabrina has sent forth her focused Alakazam and you have chosen %s " % pokemon_for_sabrina)
                        if pokemon_types[pokemon.index(pokemon_for_sabrina)].lower() in sabrina_weaknesses:
                             print("Your %s has super effective moves against Sabrina's Alakazam, You will easily defeat her \n Alakazam fainted! \n" % pokemon_for_sabrina)
                             gym_badges += 1
                             print("You have won the Marsh Badge! %d/8\n" % gym_badges)
                             bank + 20000
                             gym_leaders.remove("Sabrina")
                             battle_number_range.remove(battle_number)
                             continue   
                        else:
                             print("Your %s does not have any super effective moves against Sabrina's Alakazam, so you lost. \n You will get another oppurtunity to challenge Sabrina another day." % pokemon_for_sabrina)
                             bank - 10000
                             continue
                   elif pokemon_for_sabrina not in pokedex:
                        print("Please enter a Pokemon from your current Pokedex next time")
                        continue   
              #Blaine
              elif battle_number == 7:
                   print("You have challenged the gym leader of Cinnabar Island, Blaine.\n Blaine is a leader who specializes in fire type pokemon \n The weaknesses of Fire Pokemon include Water,Ground,Rock")
                   print(pokedex)
                   pokemon_for_blaine = input("Which pokemon would you like to choose? ")
                   if pokemon_for_blaine in pokedex:
                        print("Blaine deployed his Magmortar on the battlefield and you have chosen %s " % pokemon_for_blaine)
                        if pokemon_types[pokemon.index(pokemon_for_blaine)].lower() in blaine_weaknesses :
                             print("Your %s has super effective moves against Blaine's Magmortar, You will easily defeat him \n Magmortar fainted! \n" % pokemon_for_blaine)
                             gym_badges += 1
                             print("You have won the Volcano Badge! %d/8\n" % gym_badges)
                             bank + 20000
                             gym_leaders.remove("Blaine")
                             battle_number_range.remove(battle_number)   
                             continue
                        else:
                             print("Your %s does not have any super effective moves against Blaine's Magmortar, so you lost. \n You will get another oppurtunity to challenge Blaine another day." % pokemon_for_blaine)
                             bank - 10000
                             continue
                   elif pokemon_for_blaine not in pokedex:
                        print("Please enter a Pokemon from your current Pokedex next time")
                        continue  
              #Giovanni
              elif battle_number == 8:
                   print("You have challenged the gym leader of Viridian City, Giovanni.\n Giovanni is a leader who specializes in ground type pokemon \n The weaknesses of Ground Pokemon include Water,Ice,Grass")
                   print(pokedex)
                   pokemon_for_giovanni = input("Which pokemon would you like to choose? ")
                   if pokemon_for_giovanni in pokedex:
                        print("Giovanni unleashed his studded Rhydon and you have chosen %s " % pokemon_for_giovanni)
                        if pokemon_types[pokemon.index(pokemon_for_giovanni)].lower() in giovanni_weaknesses:
                             print("Your %s has super effective moves against Giovanni's Rhydon, You will easily defeat him \n Rhydon fainted! \n" % pokemon_for_giovanni)
                             gym_badges += 1
                             print("You have won the Earth Badge! %d/8\n" % gym_badges)
                             bank + 20000
                             gym_leaders.remove("Giovanni")
                             battle_number_range.remove(battle_number)
                             continue   
                        else:
                             print("Your %s does not have any super effective moves against Giovanni's Rhydon, so you lost. \n You will get another oppurtunity to challenge Giovanni another day." % pokemon_for_giovanni)
                             bank - 10000
                             continue
                   elif pokemon_for_giovanni not in pokedex:
                        print("Please enter a Pokemon from your current Pokedex next time")
                        continue   
         if gym_badges == 8:
              print("""
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._""")
              print("You are the newest Pokemon CHAMPION!!!")      
    else:
         happy = "no"
         while happy != "yes":
              pokemon_change = input("Which Pokemon would you like to change? ")
              pokemon_replace = input("What Pokemon would you like to replace %s with? " % pokemon_change)
              pokedex[pokedex.index(pokemon_change)] = pokemon_replace
              print(pokedex)
              are_you_happy_now = input("Do you want to change another Pokemon? ")
              if are_you_happy_now == "yes":
                   continue
              else:
                   happy == "yes"
                   break
              
                  
else:
     print("\nWe'd love to watched you play! ")
     

                             
                        
                        
                   
                   
                   
                   

              



     



