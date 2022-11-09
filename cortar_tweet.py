

class CutTweets():

    def __init__(self) -> None:
        pass
        
    def read_all_text(self, text, list):
        """
        añade a una lista las partes del texto que indicamos en la lista. 
        La lista contiene int que indica los limites
        """
        tweet = []
        for pos in range(len(list)):
            lim_low = list[pos]
            if lim_low != list[-1]:#añadir a la lista siempre que no se llegue al ultimo elemento
                lim_up = list[pos +1 ]
                if self.is_list_empty(tweet) == False:
                    tweet.append(self.select_text(text, lim_low +1, lim_up +1))
                else:
                    tweet.append(self.select_text(text, lim_low , lim_up +1))

            else:
                pass

        return tweet
         
            
    def select_text(self, text, lim1, lim2):
        return text[ lim1 : lim2 ]

    
        # function to check whether the list is empty or not
    def is_list_empty(self, list):
        # checking the length
        if len(list) == 0:
            # returning true as length is 0
            return True
        # returning false as length is greater than 0
        return False

    