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
    
    def check_continue_spaces(self, list):
        """
        busca eliminar las posiciones  de espacios seguidos
        """
        last_pos = list[0]
        continue_numer_index = 0
        list_continued = []
        list_repeated_spaces = []
        for i in list:            
            if last_pos  + continue_numer_index == i :
                if  continue_numer_index == 0:
                    #añadir a la lista de posicionws
                    list_continued.append(i)
                    # +1 al contador
                    continue_numer_index += 1
                else:
                    #comrpobar si es el ultimo elemento si lo es añadir el contador a su lista
                    if i == list[-1]:
                      list_repeated_spaces.append(continue_numer_index)  
                    # +1 al contador
                    else:
                        continue_numer_index += 1            
            else: # no sigue la continuidad de los espacios --> hay palabras en medio
                last_pos = i
                # añadir a la lista el contador -1(para restar la ultima suma que ha hecho y que no  era continuio)   
                if continue_numer_index > 0:
                    continue_numer_index -= 1
                    list_repeated_spaces.append(continue_numer_index)
                    list_continued.append(i)
                    # reiniciar contador a 0
                    continue_numer_index = 1
                
                  
                    
        return list_continued, list_repeated_spaces
            






