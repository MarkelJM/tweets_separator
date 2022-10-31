from setting import LIMIT_DOWN, LIMIT_UP, REDUCE_LIMIT, SIGN_1_LEVEL, SIGN_2_LEVEL

class IdentificateCutPoint():
    
    
    def compare_signs(self, lim_down, lim_up, text):  
        
        index = 0
        sign_flag = False
        """
        leera si entre los limites facilitados hay signos o no
        """
        
        #comparara si entre los limites logicos del texto hay signos de cortes
        for pos in range(lim_down, lim_up):
            #identifica signos de cortes
            if self.is_cutter(pos, text):#self.text  is not neccfessary, but we need it for the test
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
            False
