#Crea un programa que sea capaz de transformar texto natural a código morse y viceversa. - 
# Debe detectar automáticamente de qué tipo se trata y realizar la conversión. - 
# En morse se soporta raya '—', punto '.', un espacio ' ' entre letras o símbolos 
# y dos espacios entre palabras ' '. - 
# El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

codigo_morse = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", 
    "g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", "l": ".-..", 
    "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".__.", "q": "--.-",
    "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--..",
    
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", 
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    
    ".": ".-.-.-", ",": "-.-.--", "?": "..--..", "\"": ".-..-."
}
codigo_morse_vice = {
    ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", 
    "--.": "g", "....": "h", "..": "i", "·---": "j", "-.-": "k", ".-..": "l", 
    "--": "m", "-.": "n", "--.--": "ñ", "---": "o", ".__.": "p", "--.-": "q",
    ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w",
    "-..-": "x", "-.--": "y", "--..": "z",
    
    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4", 
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",
    
    ".-.-.-": ".", "-.-.--": ",", "..--..": "?", ".-..-.": "\""
}
texto_codificado = ""
palabra = input("Ingrese una palabra o texto a codificar: ")
for c in palabra:
    if c != " " and c.lower() in codigo_morse:
        texto_codificado += codigo_morse[c.lower()]
    else:
        texto_codificado += c
print("Texto codificado: {}".format(texto_codificado))
texto_codificado_dos = ""
palabra_Dos = input("Ingrese una palabra o texto a codificar: ")
for c in palabra:
    if c != " " and c.lower() in codigo_morse_vice:
        texto_codificado_dos += codigo_morse_vice[c.lower()]
    else:
        texto_codificado_dos += c
    
print("Texto codificado: {}".format(texto_codificado_dos))
