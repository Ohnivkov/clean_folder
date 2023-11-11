import pathlib
import os
import shutil
import sys
from threading import Thread
import time
path = sys.argv[1] # dir_name
path_img = os.path.join(path,'images')
path_video = os.path.join(path ,'video')
path_documents = os.path.join(path ,'documents')
path_archives = os.path.join(path,  'archives')
path_audio = os.path.join(path,'audio')
os.chdir(path)
folders=[]
def normalize(filename, suffix):  # filename normalization
    global TRANS
    new_filename = ''
    for i in filename:
        if i.isdigit():
            new_filename += i
        elif i.isalpha():
            i = i.translate(TRANS)
            new_filename += i
        else:
            new_filename += '_'
    return new_filename + suffix

def move_file(file):
    if file.is_file():
        try:
            if file.suffix == ".zip" or file.suffix == ".tar" or file.suffix == ".gz":
                shutil.unpack_archive(file, os.path.join("archives", file.stem))
                os.remove(file)
            else:
                shutil.move(file, os.path.join(path_dict[file.suffix.lower()], file.name))
                os.rename(
                    os.path.join(path_dict[file.suffix.lower()], file.name),
                    os.path.join(
                        path_dict[file.suffix.lower()], normalize(file.stem, file.suffix)
                    ),
                )
        except KeyError:
            pass
def grab_folder(path):
    path=pathlib.Path(path)
    for i in path.iterdir():
        if i.is_dir():
            folders.append(i)
            grab_folder(i)


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

path_dict = {'.png': path_img,
             '.jpg': path_img,
             '.jpeg': path_img,
             '.svg': path_img,
             '.avi': path_video,
             '.mp4': path_video,
             '.mov': path_video,
             '.mkv': path_video,
             '.doc': path_documents,
             '.docx': path_documents,
             '.txt': path_documents,
             '.pdf': path_documents,
             '.xlsx': path_documents,
             '.pptx': path_documents,
             'mp3': path_audio,
             'ogg': path_audio,
             'wav': path_audio,
             'amr': path_audio, }
list_dir = ['audio', 'video', 'documents', 'archives', 'images']

def main():
    grab_folder(path)
    treads=[]
    for folder in folders:
        tread=Thread(target=move_file,args=(folder,))
        tread.start()
        treads.append(tread)
    [el.join() for el in treads]



