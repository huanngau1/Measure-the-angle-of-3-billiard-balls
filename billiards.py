import numpy as np
import cv2
import math
  
# returns square of distance b/w two points 
def lengthSquare(X, Y): 
    xDiff = X[0] - Y[0] 
    yDiff = X[1] - Y[1] 
    return xDiff * xDiff + yDiff * yDiff

def printAngle(A, B, C): 
      
    # Square of lengths be a2, b2, c2 
    a2 = lengthSquare(B, C) 
    b2 = lengthSquare(A, C) 
    c2 = lengthSquare(A, B) 
  
    # length of sides be a, b, c 
    a = math.sqrt(a2); 
    b = math.sqrt(b2); 
    c = math.sqrt(c2); 
  
    # From Cosine law 
    alpha = math.acos((b2 + c2 - a2) /
                         (2 * b * c)); 
    betta = math.acos((a2 + c2 - b2) / 
                         (2 * a * c)); 
    gamma = math.acos((a2 + b2 - c2) / 
                         (2 * a * b)); 
  
    # Converting to degree 
    alpha = alpha * 180 / math.pi; 
    betta = betta * 180 / math.pi; 
    gamma = gamma * 180 / math.pi; 
  
    # printing all the angles 
    print("A : %f" %(alpha)) 
    print("B : %f" %(betta))
    print("C : %f" %(gamma))
    cv2.putText(img, str(round(alpha))+ "*", (locate[0][0]+10,locate[0][1]+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    cv2.putText(img, str(round(betta))+ "*", (locate[1][0]+10,locate[1][1]+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    cv2.putText(img, str(round(gamma))+ "*", (locate[2][0]+10,locate[2][1]+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)


locate = []

# read file image from folder
img = cv2.imread("billiards.jpg")
# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),15,(255,0,0),1)
        print(x,y)
        xy= [x,y]
        locate.append(xy)
        print(locate)
        print(len(locate))
        if(len(locate)<3):
        	text = "{0} bida".format(len(locate))
        	cv2.putText(img, text, (200,50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)
        else:
        	A = (locate[0][0],locate[0][1])
	        B = (locate[1][0],locate[1][1])
	        C = (locate[2][0],locate[2][1])
	        cv2.line(img, (locate[0][0],locate[0][1]),(locate[1][0],locate[1][1]),(0,0,255),2)
	        cv2.line(img, (locate[0][0],locate[0][1]),(locate[2][0],locate[2][1]),(0,0,255),2)
	        cv2.line(img, (locate[1][0],locate[1][1]),(locate[2][0],locate[2][1]),(0,0,255),2)
	        printAngle(A, B, C)
        	
# Create a black image, a window and bind the function to window
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
#cv2.imshow('image',img)
#cv2.waitKey(0)
cv2.destroyAllWindows()