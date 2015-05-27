import sys
import webbrowser

try:
    current_comic = open('config.txt', 'r+') # Try to open text file
    
except IOError: #If cant open, create new
    current_comic = open('config.txt', 'w')

try:
    current = current_comic.readline() #Try to read text in file
    
    temp = input('Do you want to open comic ' + current + '?\n>>> ') #Confirm comic number
    
    if 'y' in temp.lower(): #Confirmed
        comic = current
    
    elif 'n' in temp.lower(): #Open different comic
        comic = input('Which comic would you like to open?\n>>> ')
    
    else:
        print('This is not a valid answer. Please answer with Yes or No.')    

except IOError: #If no text, assume starting on comic no. 1
    temp = input('Do you want to read the first comic?\n>>> ')
    
    if 'y' in temp.lower():
        comic = '1'
    
    elif 'n' in temp.lower(): #If not comic no. 1, which comic?
        comic = input('Which comic do you want to open? (Type \'new\' for the newest comic)\n>>> ') #Add in the option for latest
    
    else:
        print('This is not a valid answer. Please answer with Yes or No.') #If invalid answer
    
if 'w' in comic.lower():
    webbrowser.open('http://xkcd.com/') #Opens website (Will always be latest comic)
    
else:
    webbrowser.open('http://xkcd.com/' + comic + '/') #Opens website to selected comic
    
    #Rewrites text file with comic for next time
    current_comic.close()
    current_comic = open('config.txt', 'w')
    current_comic.write(str(comic + 1))
        
comic = int(input('What comic did you finish on?\n>>> ')) #Asks for ending comic

#Rewrites text file with comic for next time
current_comic.close()
current_comic = open('config.txt', 'w')
current_comic.write(str(comic + 1))
current_comic.close()