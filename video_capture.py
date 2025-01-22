import cv2
import torch
import numpy as np
import mss
import pyautogui 

model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp/weights/best.pt')  

def main():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  
        
        while True:
            screenshot = sct.grab(monitor)
            frame = np.array(screenshot)  

            results = model(frame)
            
            detections = results.pandas().xyxy[0]  
            screen_width, screen_height = pyautogui.size()

            for _, row in detections.iterrows():
                if row['name'] == 'youtube_skip_button' and row['confidence'] > 0.5: 
                    
                    x1, y1, x2, y2 = row['xmin'], row['ymin'], row['xmax'], row['ymax']
                    x_center = (x1 + x2) / 2
                    y_center = (y1 + y2) / 2

                    frame_height, frame_width, _ = frame.shape
                    mouse_x = int(x_center / frame_width * screen_width)
                    mouse_y = int(y_center / frame_height * screen_height)

                    pyautogui.moveTo(mouse_x, mouse_y)
                    pyautogui.click()
                    print(f"Clique no botão detectado em ({x_center}, {y_center})")
            

            results.render()
            cv2.imshow('Tela Capturada', np.array(results.ims[0])) 

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    cv2.destroyAllWindows()  
if __name__ == "__main__":
    main()
