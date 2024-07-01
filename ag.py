import sys  

def get_arguments():
    if len(sys.argv) < 2 or len(sys.argv) > 3:  
        print("Usage: ag PATTERN [PATH]")  
        sys.exit(1)  

    pattern = sys.argv[1]  
    path = sys.argv[2] if len(sys.argv) > 2 else "."  
    return pattern, path  

pattern, path = get_arguments() 
print(f"Pattern: {pattern}, Path: {path}")  
