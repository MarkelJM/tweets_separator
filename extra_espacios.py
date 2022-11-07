from setting import SPACE

class EliminatedSpaces():

    def __init__(self, text) -> None:
        self.space = SPACE
        self.past_char = ""
        self.text = text
        
        


    def compare_last_char(self):
        list_repeated_space = []
        for pos in range(len(self.text)):
            
            if self.text[pos] == self.space and self.past_char == self.space:
                """
                añade a una lista si hay espacios seguidos, si antes tenia una elemento alfabetico no lo añadira
                """
                list_repeated_space.append(pos)
                
            self.past_char = self.text[pos]
        return list_repeated_space
    
    def check_repeated_spaces(self, list):
        """
        busca eliminar las posiciones  de espacios seguidos
        """

        last_pos = list[0]
        continue_numer_index = 0
        list_repeated = []
        for i in list:
            
            if last_pos  + continue_numer_index == i :
                
                if  continue_numer_index > 0:
                  
                
                
            else:
                last_pos = i
            
            






