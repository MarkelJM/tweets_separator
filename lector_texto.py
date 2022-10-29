class Lector:
    def __init__(self):
        self.signos = [".", ";", ":", "!", "?"]
        self.cortes = []
    
    def identificador_signos(self, texto):
        lim_min = 130
        lim_max = 140
        reduccir_lim = 20
        salir = False
        while not salir:
            for i in range(lim_min, lim_max +1): #para que recorra el tweet de atras hacia delante
                if  texto[i] in self.signos:                
                    self.cortes.append(i) #podemos meter el texto aquí, pero es más interesante usar una nueva funcion para eso
                    if lim_max > len(texto) +1:
                        salir = True
                        continue
                    if self.cortes == []: # len(self.cortes) == null
                        lim_min = 0
                        self.cortes.append(self.cortar_tweets(lim_min, lim_max))
                    else:
                        self.cortes.append(self.cortar_tweets(lim_min, lim_max))
                    
                    lim_min = i +1
                    lim_max += 140
                    
            if lim_max > len(texto) +1:
                lim_max = len(texto)+1
            else:
                lim_min = lim_min - reduccir_lim
                lim_max = lim_max - reduccir_lim
                
                
   
                
    def cortar_tweets (self, limitador_inferior, limitador_superior):  #funcion para cortar
        tweet = []
        for i in range(lim_min, lim_max +1):
                tweet.append(i)
        return tweet