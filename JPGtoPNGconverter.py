import sys
import os
from PIL import Image, UnidentifiedImageError

# --- 1. USER GUIDANCE & ERROR HANDLING ---
if len(sys.argv) < 3:
    print("\n" + "="*50)
    print("JPG to PNG CONVERTER - USAGE GUIDE")
    print("="*50)
    print("Command: python jpgtopngconverter.py <source> <destination>")
    print("\nEXAMPLE (Single File):")
    print('python jpgtopngconverter.py "C:\\My Photos\\image.jpg" "C:\\Output Folder"')
    print("\nEXAMPLE (Full Folder):")
    print('python jpgtopngconverter.py "C:\\Input Folder" "C:\\Output Folder"')
    print("\nIMPORTANT: If your folder names have spaces, you MUST wrap them")
    print('in double quotes (e.g., "My Folder") so the computer reads it correctly.')
    print("="*50 + "\n")
    sys.exit()

source = sys.argv[1]
output_dir = sys.argv[2]

# --- 2. SETUP ---
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def convert_and_save(input_path, output_folder):
    try:
        clean_name = os.path.splitext(os.path.basename(input_path))[0]
        output_path = os.path.join(output_folder, f"{clean_name}.png")
        
        with Image.open(input_path) as img:
            img.save(output_path, 'png')
            print(f"Converted: {os.path.basename(input_path)} -> {clean_name}.png")
            return True
    except UnidentifiedImageError:
        print(f"Skipped: {input_path} (Not a valid image file)")
    except Exception as e:
        print(f"Error: {e}")
    return False

# --- 3. EXECUTION LOGIC ---
if os.path.isfile(source):
    if source.lower().endswith(('.jpg', '.jpeg')):
        convert_and_save(source, output_dir)
    else:
        print("Error: Source file must be a .jpg or .jpeg")

elif os.path.isdir(source):
    count = 0
    files = os.listdir(source)
    for filename in files:
        if filename.lower().endswith(('.jpg', '.jpeg')):
            if convert_and_save(os.path.join(source, filename), output_dir):
                count += 1
    print(f"\nDone! Processed {count} images.")

else:
    print(f"Error: Path '{source}' not found. Check your spelling and quotes!")