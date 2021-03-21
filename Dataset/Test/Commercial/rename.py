import os 
  
# Function to rename multiple files 
def main(): 
  
    for count, filename in enumerate(os.listdir("Falcon_8x")): 
        dst ="Commercial-Falcon_8x-" + str(count+1) + ".jpg"
        src ='Falcon_8x/'+ filename 
        dst ='Falcon_8x/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 