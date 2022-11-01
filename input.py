from setting import  LIMIT_UP, MAX_CHARACTERS
class ObtainText():
    def __init__(self) :
        self.limit_up = LIMIT_UP
        self.max_char = MAX_CHARACTERS
        
    def request_text(self):
        text = input("Escribe el texto que quieres separar(recuerda escribir con signos, sino se cortará feo...): ")
        print("te lo devolveremos cortado a trocitos")
        return text

    def check_text_len(self, text):
        if len(self.request_text()) >= self.max_char:
            return True
        else:
            return False

    def is_text_too_long(self):
        
        text = self.request_text()#otro archivo donde pediremos el texto
        if self.check_text_len(text) == True:
            print("texto es demasiado largo, divídelo en pares")
            return False, text
        else:
            return True, text
