import cv2
import dropbox
import time
import random


start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)

    videoCaptureOb = cv2.VideoCapture(0)
    result = True

    while(result):
        ret,frame = videoCaptureOb.read()
        img_name = "img"+str(number)+".jpeg"
        cv2.imwrite(img_name,frame)
        start_time = time.time()
        result = False

    return img_name
    print('Snapshot Taken!')
    videoCaptureOb.release()
    cv2.destroyAllWindows()

def upload_files(img_name):
    access_token = 'sl.BH7UMyU-20PgLdQ1DMdFvNbJ27ima6VRjFcQU44bug3EjDDWt1de10BcLkovpX07WycUiguqltX3zhRUP_tHluD5DVJwxnZAdOkRzi0ifZyMIZ3AUxTdsloAxY8ML0VpE8rcA1I9C4qd'
    file = img_name
    file_from = file
    file_to = '/Dropbox/Sample_1/'+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(),file_to)

    print("File Loaded!")


def main():
    while(True):
      if((time.time()-start_time)>=5):
         name = take_snapshot()
         upload_files(name)


main()


    
