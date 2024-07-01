import sys  

def get_arguments():
    if len(sys.argv) < 2 or len(sys.argv) > 3:  
        print("Usage: ag PATTERN [PATH]")  
        sys.exit(1)  

    pattern = sys.argv[1]  
    path = sys.argv[2] if len(sys.argv) > 2 else "."  
    return pattern, path  

def search_in_file(pattern, filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        for lineno, line in enumerate(file, start=1):
            if pattern in line:
                print(f"{filepath}\n{lineno}:{line.strip()}")

pattern, path = get_arguments() 
# print(f"Pattern: {pattern}, Path: {path}")  
search_in_file(pattern, path)
