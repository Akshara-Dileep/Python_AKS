'''In a town, the percentage of men is 52.
 The percentage of total literacy is 48. If total percentage of literate men is 35 of the total population, 
 write a program to find the total number of illiterate men and women if the population of the town is 80,000.
'''
total=80000
total_men=(52*total)/100
total_women=total-total_men
total_lit=(48*total)/100
lit_men=(35*total)/100
lit_women=total_lit-lit_men
unlitmen=total_men-lit_men
unlitwomen=total_women-lit_women
print("Total Population          : ",total)
print("Total Mens                : ",total_men)
print("Total Womens              : ",total_women)
print("Total Literacy            : ",total_lit)
print("Total Literacy Mens       : ",lit_men)
print("Total Literacy Womens     : ",lit_women)
print("Total Not Literacy Mens   : ",unlitmen)
print("Total Not Literacy Womens : ",unlitwomen)

'''output
Total Population          :  80000
Total Mens                :  41600.0
Total Womens              :  38400.0
Total Literacy            :  38400.0
Total Literacy Mens       :  28000.0
Total Literacy Womens     :  10400.0
Total Not Literacy Mens   :  13600.0
Total Not Literacy Womens :  28000.0'''