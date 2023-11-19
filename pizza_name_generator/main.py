""" 
@Program: master
@Author: Donald Osgood
@Last Date: 2023-11-17 19:32:42
@Purpose:Donald Osgood
"""
from olipy.queneau import (
    WordAssembler,
)
from olipy import corpora


def main():
    dinosaurs = corpora.animals.dinosaurs["dinosaurs"]
    assembler = WordAssembler(dinosaurs)
    assembler.add("Donald")
    dinos = []
    
    for source in corpora.get_categories():
        print(source)
        
    
    for i in range(2):
        dino = assembler.assemble_word()
        if dino[0] in "AEIO":
            dino = "an " + dino
        else:
            dino = "a " + dino
        dinos.append(dino)
    print("Look! Behind that ridge! It's %s fighting %s!" % tuple(dinos))


if __name__ == "__main__":
    main()