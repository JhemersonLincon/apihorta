from utils import DataSet
from algorithms import Algorithm
from tensorflow.keras.models import load_model
import numpy as np
class Apple:
 
    classes = ['Desconhecido', 'Planta']
    model = load_model('classificator/classification_plant.h5')
    
    def verificar(self, image):
        plant = DataSet()
        
        img = plant.load_image(image)
        predictions = self.model.predict(np.array([img]))
        if(predictions[0] >= 0.5):
            return True
        return False
    
        
        
        