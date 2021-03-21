import os 
  
# Function to rename multiple files 
def main(): 
  
    for count, filename in enumerate(os.listdir("Rafale")): 
        dst ="Military-Rafale-" + str(count+1) + ".jpg"
        src ='Rafale/'+ filename 
        dst ='Rafale/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 