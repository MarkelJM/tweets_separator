from input import ObtainText
from lista_lugares import LimitPoints
from cortar_tweet import CutTweets


if __name__ == "__main__":
    text = ObtainText()
    text_len_checker = text.is_text_too_long()
    lista_signos = LimitPoints()
    cut_text = CutTweets()
    if text_len_checker[0] == False:
        pass
    else:
        cut_text.read_all_text(text_len_checker[1],lista_signos.run_loop(text_len_checker[1]))#para cortar pide el texto y !!!!
        print("comienza")
    
    