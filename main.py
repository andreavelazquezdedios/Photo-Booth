import cv2
import time
import argparse
import numpy as np
import matplotlib as mpl
import matplotlib.cm as mtpltcm

if __name__ == '__main__':
    print("1 --> Sin filtro")
    print("2 --> Inversión de colores")
    print("3 --> Difuminado de imagen")
    print("4 --> De cabeza")
    print("5 --> Resaltado de color piel")
    print("6 --> Escala de grises")
    print("7 --> Efecto acuarela")
    print("8 --> Filtro de calor")
    
    filtro = int(input("Elija el filtro de su preferencia: ", ))

    script_start_time = time.time()

    parser = argparse.ArgumentParser(description='Camera visualization')

    ### Positional arguments
    parser.add_argument('-i', '--cameraSource', default=0, help="Introduce number or camera path, default is 0 (default cam)")

    args = vars(parser.parse_args())

    cap = cv2.VideoCapture(args["cameraSource"]) #0 local o primary camera
    
    while cap.isOpened():
        
        if filtro == 1:
            a = "camara sin efecto"
            success,img = cap.read()    
            
            if not success:
                break
            if img is None:
                break
            
        elif filtro ==2:
            a = "inversion de colores"
            ret, frame = cap.read()
            img = cv2.bitwise_not(frame)
            if not ret:
                break
            if img is None:
                break
            
        elif filtro ==3:
            a = "difuminado"
            success,frame = cap.read() 
            kernel = np.ones((5,5),np.float32)/25
            img = cv2.filter2D(frame,-1,kernel)
        
        elif filtro ==4:
            a = "de cabeza"
            success,img = cap.read()    
            img = cv2.flip(img,0)
            if not success:
                break
            if img is None:
                break
            
        elif filtro == 5:
            a = "resaltar color"
            success, img = cap.read()
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            lower = np.array([0, 133, 77])
            upper = np.array([255, 173, 127])
            mask = cv2.inRange(hsv, lower, upper)
            img = cv2.bitwise_and(img, img, mask=mask)
            
        elif filtro ==6:
            a = "escala de grises"
            success,img = cap.read()    
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            if not success:
                break
            if img is None:
                break
            
        elif filtro ==7:
            a = "acuarela"
            success,img = cap.read() 
            img = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
            if not success:
                break
            if img is None:
                break
                
        elif filtro ==8:
            cap = cv2.VideoCapture(0)
            colormap = mpl.cm.jet
            cNorm = mpl.colors.Normalize(vmin=0, vmax=255)
            scalarMap = mtpltcm.ScalarMappable(norm=cNorm, cmap=colormap)
            a = "filtro de calor"
            success, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray,(15,15),0)
            img = scalarMap.to_rgba(blur, bytes=False)
        
        else:
            print("Error en la selección")
            break
        
        flip = cv2.flip(img,1)
        cv2.imshow(a,flip)
        k = cv2.waitKey(10)
        if k==27:
            break

    cap.release()
    cv2.destroyAllWindows()

    print('Script took %f seconds.' % (time.time() - script_start_time))
