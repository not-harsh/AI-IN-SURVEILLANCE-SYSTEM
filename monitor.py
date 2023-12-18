import cv2
from datetime import datetime
import matplotlib.pyplot as plt

def monitor():

    video=cv2.VideoCapture(0)
    facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #count=0
    while True:
        ret,frame=video.read()
        faces=facedetect.detectMultiScale(frame,1.3,5)
      
      
        cv2.putText(frame, f'{datetime.now().strftime("%D - %H : %M : %S")}', (50,50), cv2.FONT_HERSHEY_COMPLEX,
                            0.6, (255,255,255), 2)

        #out.write(frame)
            

        #cv2.imshow("esc. to stop", frame)

        
        for x,y,w,h in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
            #count=count+1
            #name='./images/face_without_mask/'+str(count)+'.jpg'
            #print("Creating Images... "+name)
            #cv2.imwrite(name,frame[y:y+h,x:x+w])
            
        cv2.imshow("WindowFrame",frame)
        #k=cv2.waitKey(1)
        #img = cv2.imread('path_to_image')
        #plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
        #plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
        #plt.show()
        
      
        if cv2.waitKey(1) == 27:
            video.release()
            cv2.destroyAllWindows()
            break 
    video.release()
    cv2.destroyAllWindows()
