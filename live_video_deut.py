import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while True:
    _, frame = cap.read()
    _, img = cap.read()
    sz1,sz2,_ = frame.shape
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    #print(hsv)
    b,g,r    = cv2.split(frame)
    #frame1 = cv2.merge((b,g,r))

    for x in range(sz1):
        for y in range(sz2):
           # if np.any(frame1[x,y,2]) > 0 : 
            #    frame1[x,y,0] = 0
             #   frame1[x,y,1] = 0
            blue = img.item(x,y,0)
            green = img.item(x,y,1)
            red = img.item(x,y,2)
            rg1 = abs(red - green)
            rg = red - green
            rb = abs(red - blue)
            rb1 = red - blue
            gb = abs(green - blue)
            gb1 = green - blue
            br = blue - red  
        
            if((rg1<=60 and rb<=60 and gb<=60) and (rg1<30) or (rb1>=50 and rb1<=107 and gb1>=12 and gb1<=55)): # Leaving Grayscale and skin tone as it is.
                continue
        
            elif(br>0 and br<=69 and red>100 and blue>110 and green<=110): # Recoloring purple shade by contrast enhancement
                green = green + 100
                if(green>255):
                    green = 255
                img.itemset((x,y,1),green)
                img.itemset((x,y,0),blue+50)
        
            # Leaving yellow and blue shade as it is.
        
            elif((rg1<=60 and blue<=110 and red>=145)  or (red<=70 and green<=90 and blue>=105) or (red<=130 and green<=150 and blue>=150)):
                continue
        
            else:
                       
                if(rg>0): # Check if red is greater than green                    
                                  
                    red = red + 80  # Increase red component
                    if(red>255):
                        red = 255
                    img.itemset((x,y,0),red)    # Set new red component
                    
                    blue = blue + 50    # Increase blue component marginally
                    if(blue>255):
                        blue = 255
                    img.itemset((x,y,0),blue)   # Set new blue component
            
                elif(rg==0): # If red and green are equal, leave it.
                    continue
            
                else:
                    # Now for green greater than red
                    blue = blue + 100    # Increase blue component significantly
                    green = green + 25  # Increase green component marginally
                
                    if(blue>255):
                        blue = 255
                    img.itemset((x,y,0),blue)   # Set blue component
                
                    if(green>255):
                        green = 255
                    img.itemset((x,y,1),green)  # Set green component
        
        
    #cv2.imshow('test', test)
    #hsv hue sat value
    lower_red = np.array([100,100,100])
    upper_red = np.array([255,255,255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame,mask = mask)
    out.write(img)
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('resb', img)
    #cv2.imshow('resg', g)
    #cv2.imshow('resr', r)
    
    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break
        
cv2.destroyAllWindows()
cap.release()
out.release()
