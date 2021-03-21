import os 
  
# Function to rename multiple files 
def main(): 
  
    for count, filename in enumerate(os.listdir("F-35")): 
        dst ="Commercial-F35-" + str(count+1) + ".jpg"
        src ='F-35/'+ filename 
        dst ='F-35/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 