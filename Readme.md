# 🖼️ JPG to PNG Batch Converter

A lightweight, robust Python automation script to seamlessly convert `.jpg` and `.jpeg` images into `.png` format. 

Whether you need to convert a single image or process an entire directory of hundreds of files, this tool handles the conversion efficiently while preserving the original files and providing clear, user-friendly error handling.

## ✨ Features
* **Dual Functionality:** Automatically detects whether the input is a single file or a full directory and processes it accordingly.
* **Non-Destructive:** Creates new `.png` files in your specified output folder without altering or deleting the original `.jpg` files.
* **Built-in Error Handling:** Gracefully skips non-image files, warns about invalid paths, and provides clear terminal instructions if arguments are missing.
* **Space-Friendly Pathing:** Designed to handle complex Windows/Mac folder paths that contain spaces.

🛠️ Prerequisites
Before running the script, ensure you have Python installed along with the Pillow library (Python Imaging Library).

```Bash```
`pip install Pillow`

🚀 Usage Guide
Run the script from your command line terminal. The script requires two arguments: the source (a file or a folder) and the destination folder..

General Syntax
```Bash```
```python JgptoPNGconverter.py <source_path> <destination_folder>```

1. Converting a Full Folder
To convert all .jpg files within a specific folder:

```Bash```
```python JgptoPNGconverter.py "C:\Images\Input Folder" "C:\Images\Output Folder"```

2. Converting a Single File
To convert just one specific image:

```Bash```
```python JgptoPNGconverter.py "C:\Images\Input Folder\photo.jpg" "C:\Images\Output Folder"```

⚠️ Important Note on File Paths
If your folder or file names contain spaces (e.g., Image Processing), you must wrap the paths in double quotes so the command line interprets the path correctly.
