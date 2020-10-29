import cv2
from .api import update_ticket

class Scanner:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.detector = cv2.QRCodeDetector()
        
    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()
        
    
    def polling(self):
        while True:
            _, img = self.cap.read()
            data, bbox, _ = self.detector.detectAndDecode(img)
            
            if(bbox is not None):
                for i in range(len(bbox)):
                    cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255,
                             0, 255), thickness=2)
                cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (0, 255, 0), 2)
                if data:
                    print("data found: ", data)
                    if update_ticket(data) == 200:
                        cv2.rectangle(img,(0,0),(640,480),(0,138,0),-1)
                        cv2.putText(img, "Success", (60,240), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2 )
                        print("ticket updated")
                                           
            cv2.imshow("Squid-QR-Scanner", img)
            if(cv2.waitKey(1) == ord("q")):
                break
