import numpy as np
import pyautogui
import cv2


#name of recording file
filename = r"D:\trading/recording1.avi"
codec = cv2.VideoWriter_fourcc(*"XVID")
resolution = tuple(pyautogui.size())
#frames per second
fps = 60

out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()
  
    # Convert the screenshot to a numpy array
    frame = np.array(img)
  
    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  
    # Write it to the output file
    out.write(frame)
      
    # Optional: Display the recording screen
    cv2.imshow('Live', frame)
      
    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break
  
# Release the Video writer
out.release()
  
# Destroy all windows
cv2.destroyAllWindows()