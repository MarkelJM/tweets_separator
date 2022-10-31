from setting import LIMIT_DOWN, LIMIT_UP, MARGIN,REDUCE_LIMIT, INCREASE_LIMIT
from leer_texto import IdentificateCutPoint

class LimitPoints():
    def __init__(self) -> None:
        
        self.limit_2 = LIMIT_UP
        
        self.index = IdentificateCutPoint()
        
        

    def get_text(self):
        text = request_text()#otro archivo donde pediremos el texto
        return text
    
    def run_loop(self, text=get_text()):
        list_sign = []
        
        """
        Bucle principal donde se debe saber si entre limite maximo y minimo de tweet hay signos  
        o hay que reducir el limite inferior para buscar
        """
        stop = False
        #bucle principal
        while not stop:
            #llamar a la clase que identificaç
            identificate_limit = self.index.compare_signs(self.reduce_margin(self.limit_2), self.limit_2, text)
            """devuelve posicion del ultimo signo y flag True si lo hay en tupla o 0 y False si no signos"""
            #si hay signos siguiente paso 
            if identificate_limit[1] == True:
                list_sign.append(identificate_limit[0])
                #aumentamos limites para siguiente tweet
                self.limit_2 = self.increase_limit( identificate_limit[0])
            #no hay limite? reducir limite inferior hasta encontrar un signo
            elif identificate_limit[1] == False:
                self.limit_2 = self.decrease_limit(self.reduce_margin(self.limit_2))
                
            #si en los 140 caracteres no hay signos identificar el ultimo espacio para cortar ahí
            else:
                pass 
            """que identifique el ultimo espacio!!!!!!!!!!!!!!!!!"""
       
        return list_sign

    def increase_limit(self, pos2):
        increaser = INCREASE_LIMIT
        return  pos2 +increaser

    def decrease_limit(self, pos1, pos2):
        decreaser = REDUCE_LIMIT
        return pos1 - decreaser 

    def reduce_margin(self, pos):
        margin = MARGIN
        return pos - margin
