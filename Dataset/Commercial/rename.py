import os 
  
# Function to rename multiple files 
def main(): 
  
    for count, filename in enumerate(os.listdir("Boeing_747")): 
        dst ="Commercial-Boeing_747-" + str(count+1) + ".jpg"
        src ='Boeing_747/'+ filename 
        dst ='Boeing_747/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 