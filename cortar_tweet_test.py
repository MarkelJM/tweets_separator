import pytest
from cortar_tweet import CutTweets

def test_read_all_text():
    lista = [5,10,14,19]
    texto = "Mendian gora haritza ahunntzak aizean dabiltza"
    a = CutTweets

    assert a.read_all_text(texto, lista) == ['n gor','a har','itza ']


         
            
def test_is_list_empty():
    lista = []
    lista_2 = [1,2,3,4,4]
    
    a = CutTweets
    assert a.is_list_empty(lista) == True
    assert a.is_list_empty(lista_2) == False

    
