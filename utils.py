from tempfile import NamedTemporaryFile
import cv2
import numpy as np
class DataSet:
    
    
    def load_image(self, image):
        with NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
            image.save(temp.name)
            temp_path = temp.name
        img = cv2.imread(temp_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img,  (224, 224))
        
        return np.array(img)
        
        