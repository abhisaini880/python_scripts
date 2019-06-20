#!/usr/bin/python3.7
#########################################################
# Script to organize junk file and directories		#
#							#
#				- Abhishek saini	#
#							#
#########################################################


# Importing Libraries
import os 
#from scandir import scandir
from pathlib import Path

# Creating directories for categorizing files
DIRECTORIES = {  "HTML": [".html5", ".html", ".htm", ".xhtml"],
                 "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", ".heif", ".psd"],
	         "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
   		 "DOCS": [".oxps", ".epub", ".pages", ".docx", ".doc",".csv", ".fdf", ".ods",".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                 		 ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx"],
  	         "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
   		 "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
   		 "FILES": [".txt", ".in", ".out"],
   		 "PDF": [".pdf"],
   		 "PYTHON SCRIPTS": [".py"],
   		 "XML": [".xml"],
   		 "EXE": [".exe"],
   		 "SHELL SCRIPTS": [".sh"],
		 "PHP": [".php"],
		 "LOGS": [".log", ".log.1", ".log.3", ".log.4"],
		 "CSS": [".css"]
}


FILE_FORMATS = {file_format: directory 
                for directory, file_formats in DIRECTORIES.items() 
                for file_format in file_formats} 

def organize_junk(): 
    for entry in os.scandir(): 
        if entry.is_dir(): 
            continue
        file_path = Path(entry) 
        file_format = file_path.suffix.lower() 
        if file_format in FILE_FORMATS: 
            directory_path = Path(FILE_FORMATS[file_format]) 
            directory_path.mkdir(exist_ok=True) 
            file_path.rename(directory_path.joinpath(file_path)) 
  
        for dir in os.scandir(): 
            try: 
                os.rmdir(dir) 
            except: 
                pass
  
if __name__ == "__main__": 
    organize_junk() 



