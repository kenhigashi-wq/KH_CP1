# KH 2nd crew share
earned = float(input("How much was earned:"))
crew_mem = int(input("How many crew members are there (not including the captain and first mate):"))

total_share = 7 + 3 + crew_mem
one_share = earned / total_share 
captain = one_share * 7
first = one_share * 3
crew_guy = one_share - 500

print("The captain gets: $" + str(round(captain, 2))) # captains share
print("The first mate gets: $" + str(round(first, 2))) # first mates share
print("The crew still needs(individually): $" + str(round(crew_guy, 2))) # crew mans money
