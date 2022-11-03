

class CutTweets():

    def __init__(self) -> None:
        pass

    def read_all_text(self, text, list):
        tweet = []
        for pos in range(len(list)):
            lim_low = list[pos]
            if lim_low != list[-1]:#añadir a la lista siempre que no se llegue al ultimo elemento
                lim_up = list[pos +1 ]
                tweet.append(self.select_text(text, lim_low, lim_up))

            else:
                pass
        return tweet
            
    def select_text(self, text, lim1, lim2):
        return text[ lim1 : lim2 ]