import os 
  
# Function to rename multiple files 
def main(): 
  
    for count, filename in enumerate(os.listdir("A400M")): 
        dst ="Military-A400M-" + str(count+1) + ".jpg"
        src ='A400M/'+ filename 
        dst ='A400M/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 