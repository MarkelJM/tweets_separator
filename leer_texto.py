from setting import  SIGN_1_LEVEL, SIGN_2_LEVEL

class IdentificateCutPoint():
    
    
    def compare_signs(self, lim_down, lim_up, text): #ya que queremos usar tests no usaremos self.text(los test tiene su propio texto) 
        
        index = 0
        sign_flag = False
        self.text = text
        """
        leera si entre los limites facilitados hay signos o no
        """
        
        #comparara si entre los limites logicos del texto hay signos de cortes
        for pos in range(lim_down, lim_up):
            #identifica signos de cortes
            if self.is_cutter(pos, self.text) == True:# compara si es un signo o no///self.text  is not neccfessary, but we need it for the test
                index = pos 
                sign_flag = True
            
        return index, sign_flag
            
            #añade la posicion del corte a la lista

    def is_cutter(self, pos, text):
        self.direct_cutter = SIGN_1_LEVEL
        self.undirect_cutter = SIGN_2_LEVEL
        if text[pos] in self.direct_cutter or text[pos] in self.undirect_cutter:
            return True
        else:
            return False

    def seek_last_space(self,  lim_down, lim_up):
        #str_space = " "
        for pos in range(lim_down, lim_up, -1): 
            if self.text[pos] == " ":
                return pos

