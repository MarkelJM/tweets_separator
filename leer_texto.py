from setting import LIMIT_DOWN, LIMIT_UP, REDUCE_LIMIT, SIGN_1_LEVEL, SIGN_2_LEVEL

class IdentificateCutPoint():
    
    def __init__(self, text) -> None:
        lim_down = LIMIT_DOWN #limite que podra reducirse para que el tweet sea lo mas largo posible
        lim_up = LIMIT_UP #numero maximo de caracteres de tweets
        lim_reducer = REDUCE_LIMIT
    def compare_signs(self):  
        stop = False
        
        """
        Un bucle que lee el texto y añadirá a una lista todos los puntos de corte
        """
        #bucle que controlara hasta que no se identifiquen los cortes no parara
        while not stop:
            #comparara si entre los limites logicos del texto hay signos de cortes
            pass
            #identifica signos de cortes
            #añade la posicion del corte a la lista