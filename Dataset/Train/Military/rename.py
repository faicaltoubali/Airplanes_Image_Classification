import os 
  
# Function to rename multiple files 
def main(): 
  
    for count, filename in enumerate(os.listdir("Eurofighter_Typhoon")): 
        dst ="Military-Eurofighter_Typhoon-" + str(count+1) + ".jpg"
        src ='Eurofighter_Typhoon/'+ filename 
        dst ='Eurofighter_Typhoon/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 