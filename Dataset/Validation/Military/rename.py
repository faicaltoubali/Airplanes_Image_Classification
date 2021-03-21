import os 
  
# Function to rename multiple files 
def main(): 
  
    for count, filename in enumerate(os.listdir("Su-57")): 
        dst ="Military-Su57-" + str(count+1) + ".jpg"
        src ='Su-57/'+ filename 
        dst ='Su-57/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 