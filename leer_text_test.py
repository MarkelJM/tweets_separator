import pytest
from leer_texto import *
from setting import SIGN_1_LEVEL, SIGN_2_LEVEL

def test_compare_signs():
    text = "Hello, World!."
    main = IdentificateCutPoint()

    assert main.compare_signs(0,13, text) == (13, True) 
    assert main.compare_signs(0,4, text) == False
    


def test_char_comparator():
    text = "Ha sido duro, muchas horas aprendiendo, leyendo, investigando y atascados en errores que costaba sacar adelante, pero que con dedicación, entusiasmo y perseverancia lo conseguí. Agradecer a Antonio González Bolaño todas las horas dedicaras a ayudar a entrar en este mundo tan apasionante. Las horas extras explicando conceptos, procedimientos, teoría y prácticas para que realmente saliesemos de la clase con la lección y tareas perfectamente aprendida. El proyecto final, qué decir, la primera vez que te encontrabas ante un programa desde cero. Lo encarabas con miedo, ilusión y al parecer solo(nada más lejos de la realidad), pero no ha sido así gracias a compañeros con los que compartí opiniones y perspectivas para afrontar los atascos...otra nueva lección aprendida, los programadores trabajamos en equipo."

    main = IdentificateCutPoint()
    
    assert main.is_cutter("a", text) == False
    assert main.is_cutter("!", text) == True
    assert main.is_cutter("a", text) == False
    assert main.is_cutter("", text) == False
    assert main.is_cutter(".", text) == True
    assert main.is_cutter(";", text) == True
    assert main.is_cutter(":", text) == True
    assert main.is_cutter("?", text) == True
    assert main.is_cutter(" ", text) == False