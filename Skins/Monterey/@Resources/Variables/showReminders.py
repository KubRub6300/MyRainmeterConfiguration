import os

def replace_item(input_file, output_file):
    with open(input_file) as f:
        content = f.read()

    # Replace all occurrences of 'item' with empty string
    content = content.replace('item', '')
    
    with open(output_file, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    
    replace_item(input_file, output_file)