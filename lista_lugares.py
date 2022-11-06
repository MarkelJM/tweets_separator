from setting import LIMIT_DOWN, LIMIT_UP, MARGIN,REDUCE_LIMIT, INCREASE_LIMIT
from leer_texto import IdentificateCutPoint
from input import ObtainText

class LimitPoints():
    def __init__(self) -> None:
        
        self.limit_2 = LIMIT_UP
        
        self.index = IdentificateCutPoint()
        
        

    
    
    def run_loop(self, text):
        list_sign = [0] #debe comenzar con el primer caracter
        
        """
        Bucle principal donde se debe saber si entre limite maximo y minimo de tweet hay signos  
        o hay que reducir el limite inferior para buscar
        """
        stop = False
        #bucle principal
        while not stop:
            if self.limit_2 >= len(text):#pa identificar al llegar al final o si el tweet es "corto" y evitar trabajo
                list_sign.append(len(text))
                break
            #llamar a la clase que identificaç
            identificate_limit = self.index.compare_signs(self.reduce_margin(self.limit_2), self.limit_2, text)
            """devuelve una tupla la posicion del ultimo signo y  True si lo hay  o 0 y False si no hay signos"""
            #si hay signos siguiente paso 
            if identificate_limit[1] == True:
                if self.is_pos_repeated(identificate_limit[0], list_sign) == False:
                    list_sign.append(identificate_limit[0])
                    #aumentamos limites para siguiente tweet
                    self.limit_2 = self.increase_limit( identificate_limit[0], text)
                    
                elif self.is_pos_repeated(identificate_limit[0], list_sign):
                    """despues aumenta el limite si en 140 caracteres no hay signos llegará al último 
                    punto de partira identificando el ultimos signo o espacio(repitiendolo) para evitar esto
                    creamos esta sección
                    """
                    index = self.index.seek_last_space(self.reduce_margin(self.limit_2), self.limit_2, text)
                    list_sign.append(index) 
                    self.limit_2 = self.increase_limit(index, text)
            #no hay limite? reducir limite inferior hasta encontrar un signo
            elif identificate_limit[1] == False:
                self.limit_2 = self.decrease_limit(self.reduce_margin(self.limit_2))
                #si en los 140 caracteres no hay signos identificar el ultimo espacio para cortar ahí
                if self.limit_2 == 0:
                    index = self.index.seek_last_space(self.reduce_margin(self.limit_2), self.limit_2, text)
                    list_sign.append(index)         
        list_sign.append(len(text))  #ultima posicion para cortar debe ser ultimo caracter 
        return list_sign

    def increase_limit(self, pos2, text):
        increaser = INCREASE_LIMIT
        new_lim_up = pos2 + increaser
        if new_lim_up >= len(text):
            new_lim_up = len(text)
            return new_lim_up
        else:  
            return new_lim_up
    def decrease_limit(self, pos1):        
        new_lim_low = self.reduce_margin(pos1) 
        if new_lim_low <= 0:
            new_lim_low = 0
            return new_lim_low
        else:
            return new_lim_low

    def reduce_margin(self, pos):
        margin = MARGIN
        return pos - margin

    def is_pos_repeated(self, pos, list):
        if pos in list:

            return True
        else:
            return False