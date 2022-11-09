from input import ObtainText
from lista_lugares import LimitPoints
from cortar_tweet import CutTweets
from  extra_espacios import EliminatedSpaces

if __name__ == "__main__":
    text = ObtainText()
    text_len_checker = text.is_text_too_long()
    lista_signos = LimitPoints()
    cut_text = CutTweets()
    spaces = EliminatedSpaces()
    if text_len_checker[0] == False:
        pass
    else:
        try:
            texto = spaces.clean_clone_text(text_len_checker[1])
            tweets = cut_text.read_all_text(texto,lista_signos.run_loop(texto))#para cortar pide el texto y !!!!
            print("comienza")
            print(tweets)
        except:
            tweets = cut_text.read_all_text(text_len_checker[1],lista_signos.run_loop(text_len_checker[1]))#para cortar pide el texto y !!!!
            print("comienza")
            print(tweets)
    
    