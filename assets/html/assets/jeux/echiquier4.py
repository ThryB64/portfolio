echiquier=['a1','a2','a3','a4','a5','a6','a7','a8',
           'b1','b2','b3','b4','b5','b6','b7','b8',
           'c1','c2','c3','c4','c5','c6','c7','c8',
           'd1','d2','d3','d4','d5','d6','d7','d8',
           'e1','e2','e3','e4','e5','e6','e7','e8',
           'f1','f2','f3','f4','f5','f6','f7','f8',
           'g1','g2','g3','g4','g5','g6','g7','g8',
           'h1','h2','h3','h4','h5','h6','h7','h8',]


echiquierjeux=['ntour1','ncavalier1','nfous1','nreine','nroi'  ,'nfous2','ncavalier2','ntour2',
               'npion1','npion2'    ,'npion3','npion4','npion5','npion6','npion7'    ,'npion8',
                 'c1'  ,    'c2'    ,  'c3'  ,  'c4'  ,  'c5'  ,  'c6'  ,'c7'        ,  'c8'  ,
                 'd1'  ,    'd2'    ,  'd3'  ,  'd4'  ,  'd5'  ,  'd6'  ,'d7'        ,  'd8'  ,
                 'e1'  ,    'e2'    ,  'e3'  ,  'e4'  ,  'e5'  ,  'e6'  ,'e7'        ,  'e8'  ,
                 'f1'  ,    'f2'    ,  'f3'  ,  'f4'  ,  'f5'  ,  'f6'  ,'f7'        ,  'f8'  ,
               'bpion1',  'bpion2'  ,'bpion3','bpion4','bpion5','bpion6','bpion7'    ,'bpion8',
               'btour1','bcavalier1','bfous1','breine','broi'  ,'bfous2','bcavalier2','btour2',]

listepionsblanc=['bpion1','bpion2','bpion3','bpion4','bpion5','bpion6','bpion7','bpion8','btour1','btour2','bfous1','bfous2','bcavalier1','bcavalier2','breine','broi']
listecoordonnéespionblanc=['g1','g2','g3','g4','g5','g6','g7','g8','h1','h8','h3','h6','h2','h7','h4','h5']
bpioncoord={'bpion1':'g1','bpion2':'g2','bpion3':'g3','bpion4':'g4','bpion5':'g5','bpion6':'g6','bpion7':'g7','bpion8':'g8','btour1':'h1','btour2':'h8','bfous1':'h3','bfous2':'h6','bcavalier1':'h2','bcavalier2':'h7','breine':'h4','broi':'d2'}
listepionsmortblanc=[]
listepionsnoir=['npion1','npion2','npion3','npion4','npion5','npion6','npion7','npion8','ntour1','ntour2','nfous1','nfous2','ncavalier1','ncavalier2','nreine','nroi']
listecoordonnéespionnoir=['b1','b2','b3','b4','b5','b6','b7','b8','a1','a8','a3','a6','a2','a7','a4','a5']
npioncoord={'npion1':'b1','npion2':'b2','npion3':'b3','npion4':'b4','npion5':'b5','npion6':'b6','npion7':'b7','npion8':'b8','ntour1':'a1','ntour2':'a8','nfous1':'a3','nfous2':'a6','ncavalier1':'a2','ncavalier2':'a7','nreine':'a4','nroi':'e1'}
listepionsmortnoir=[]
demarrage=0

def jeux():
    demarrage=int(input("voulez vous jouez ?, si oui tapez 1 sinon 0: "))
    if demarrage==1:
        print('voici les coordonnées du jeux :\n',echiquier,'\n\n')
        print("jeux lancer, joueur blanc commencer")

        print(echiquierjeux)
        
        while demarrage==1 and checkmate()!='true':
            print('pions encore vivant:\n',listepionsblanc)
            mouvementblanc()
            checkmate()
            if checkmate()!='true':
                print('pions encore vivant:\n',listepionsnoir)
                mouvementnoir()
                checkmate()
            if checkmate()=='true':
                demarrage=0
            demarrage=int(input('si vous voulez arreter la partie tapez 0 sinon 1 : '))
            
    

def verification(coordfinal):
    if coordfinal in npioncoord.values():
        a = list(npioncoord.values())
        c=a.index(coordfinal)
        print(listepionsnoir[c])
        del npioncoord[listepionsnoir[c]]
        listepionsmortnoir.append(listepionsnoir[c])
        del listepionsnoir[c]
        
    
    if coordfinal in bpioncoord.values():
        a = list(bpioncoord.values())
        c=a.index(coordfinal)
        del bpioncoord[listepionsblanc[c]]
        listepionsmortblanc.append(listepionsblanc[c])
        del listepionsblanc[c]
        
    
        


def checkmate():
    if 'broi' in listepionsmortblanc :
        print('bravo joueur noir vous avez gagner la partie')
        return 'true'
    if 'nroi' in listepionsmortnoir :
        print('bravo joueur blanc vous avez gagner la partie')
        return 'true'







pioncoord={'bpion1':'g1','bpion2':'g2','bpion3':'g3','bpion4':'g4','bpion5':'g5','bpion6':'g6','bpion7':'g7','bpion8':'g8','btour1':'h1','btour2':'h8','bfous1':'h3','bfous2':'h6','bcavalier1':'h2','bcavalier2':'h7','breine':'h4','broi':'h5'}
def mouvementblanc():

    nompionb=str(input('joueur blanc: entrez le nom du pion que vous voulez déplacer :\n'))
    if nompionb=='bpion1':
        if bpioncoord['bpion1']=='g1':
            p1=(echiquier.index(bpioncoord.get('bpion1')))-16
            coord1=echiquier[p1]
            p2=(echiquier.index(bpioncoord.get('bpion1')))-8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2,", ",coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )

            if coordfinal == coord1 or coordfinal == coord2:
                verification(coordfinal)
                bpioncoord.update({'bpion1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')

        else:
            p3=(echiquier.index(bpioncoord.get('bpion1')))-8
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisisez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                bpioncoord.update({'bpion1':coordfinal})





    if nompionb=='bpion2':
      if bpioncoord['bpion2']=='g2':
            p1=(echiquier.index(bpioncoord.get('bpion2')))-16
            coord1=echiquier[p1]
            p2=(echiquier.index(bpioncoord.get('bpion2')))-8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2,", ",coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 or coordfinal == coord2:
                verification(coordfinal)
                bpioncoord.update({'bpion2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
      else:
            p3=(echiquier.index(bpioncoord.get('bpion2')))-8
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisisez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                bpioncoord.update({'bpion2':coordfinal})



    if nompionb=='bpion3':
        if bpioncoord['bpion3']=='g3':
            p1=(echiquier.index(bpioncoord.get('bpion3')))-16
            coord1=echiquier[p1]
            p2=(echiquier.index(bpioncoord.get('bpion3')))-8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2,", ",coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 or coordfinal == coord2:
                verification(coordfinal)
                bpioncoord.update({'bpion3':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            p3=(echiquier.index(bpioncoord.get('bpion3')))-8
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisisez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                bpioncoord.update({'bpion3':coordfinal})



    if nompionb=='bpion4':
        if bpioncoord['bpion4']=='g4':
            p1=(echiquier.index(bpioncoord.get('bpion4')))-16
            coord1=echiquier[p1]
            p2=(echiquier.index(bpioncoord.get('bpion4')))-8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2,", ",coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 or coordfinal == coord2:
                verification(coordfinal)
                bpioncoord.update({'bpion4':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            p3=(echiquier.index(bpioncoord.get('bpion4')))-8
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisisez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                bpioncoord.update({'bpion4':coordfinal})



    if nompionb=='bpion5':
       if bpioncoord['bpion5']=='g5':
            p1=(echiquier.index(bpioncoord.get('bpion5')))-16
            coord1=echiquier[p1]
            p2=(echiquier.index(bpioncoord.get('bpion5')))-8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2,", ",coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 or coordfinal == coord2:
                verification(coordfinal)
                bpioncoord.update({'bpion5':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
       else:
            p3=(echiquier.index(bpioncoord.get('bpion5')))-8
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisisez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                bpioncoord.update({'bpion5':coordfinal})



    if nompionb=='bpion6':
       if bpioncoord['bpion6']=='g6':
            p1=(echiquier.index(bpioncoord.get('bpion6')))-16
            coord1=echiquier[p1]
            p2=(echiquier.index(bpioncoord.get('bpion6')))-8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2,", ",coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 or coordfinal == coord2:
                verification(coordfinal)
                bpioncoord.update({'bpion6':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
       else:
            p3=(echiquier.index(bpioncoord.get('bpion6')))-8
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisisez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                bpioncoord.update({'bpion6':coordfinal})



    if nompionb=='bpion7':
        if bpioncoord['bpion7']=='g7':
            p1=(echiquier.index(bpioncoord.get('bpion7')))-16
            coord1=echiquier[p1]
            p2=(echiquier.index(bpioncoord.get('bpion7')))-8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2,", ",coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 or coordfinal == coord2:
                verification(coordfinal)
                bpioncoord.update({'bpion7':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            p3=(echiquier.index(bpioncoord.get('bpion7')))-8
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisisez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                bpioncoord.update({'bpion7':coordfinal})



    if nompionb=='bpion8':
        if bpioncoord['bpion8']=='g8':
            p1=(echiquier.index(bpioncoord.get('bpion8')))-16
            coord1=echiquier[p1]
            p2=(echiquier.index(bpioncoord.get('bpion8')))-8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2,", ",coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 or coordfinal == coord2:
                verification(coordfinal)
                bpioncoord.update({'bpion8':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            p3=(echiquier.index(bpioncoord.get('bpion8')))-8
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisisez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                bpioncoord.update({'bpion8':coordfinal})









    if nompionb=='btour1':
        deplacement=input("inscrivez la direction ou vous voulez déplacer ce pion, (devant, derriere, droite, gauche)")
        x=int(input('combien de case voulez-vous vous déplacer ?'))
        if deplacement == 'devant':        
            p1=(echiquier.index(bpioncoord.get('btour1')))-8*x
            coord1=echiquier[p1]
            print('votre pion peut aller :\n',coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 :
                verification(coordfinal)
                bpioncoord.update({'btour1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere':
            p2=(echiquier.index(bpioncoord.get('btour1')))+8*x
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord2:
                verification(coordfinal)
                bpioncoord.update({'btour1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'droite':
            p3=(echiquier.index(bpioncoord.get('btour1')))+x
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                bpioncoord.update({'btour1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'gauche':
            p4=(echiquier.index(bpioncoord.get('btour1')))-x
            coord4=echiquier[p4]
            print('votre pion peut aller :\n',coord4)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord4 :
                verification(coordfinal)
                bpioncoord.update({'btour1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            print('relancer le jeux car vous vous etes tromper dans lécriture')
            
            


    if nompionb=='btour2':
        deplacement=input("inscrivez la direction ou vous voulez déplacer ce pion, (devant, derriere, droite, gauche)")
        x=int(input('combien de case voulez-vous vous déplacer ?'))
        if deplacement == 'devant':        
            p1=(echiquier.index(bpioncoord.get('btour2')))-8*x
            coord1=echiquier[p1]
            print('votre pion peut aller :\n',coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 :
                verification(coordfinal)
                bpioncoord.update({'btour2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere':
            p2=(echiquier.index(bpioncoord.get('btour2')))+8*x
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord2:
                verification(coordfinal)
                bpioncoord.update({'btour2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'droite':
            p3=(echiquier.index(bpioncoord.get('btour2')))+x
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                bpioncoord.update({'btour2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'gauche':
            p4=(echiquier.index(bpioncoord.get('btour2')))-x
            coord4=echiquier[p4]
            print('votre pion peut aller :\n',coord4)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord4 :
                verification(coordfinal)
                bpioncoord.update({'btour2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            print('relancer le jeux car vous vous etes tromper dans lécriture')
        
        
        
        
        
        
        
        

        

    if nompionb=='bfous2':
        deplacement=input("inscrivez la direction ou vous voulez déplacer ce pion, (devant droit, devant gauche, derriere droit, derriere gauche)")
        x=int(input('combien de case voulez-vous vous déplacer ?'))
        if deplacement == 'devant droit':        
            p1=(echiquier.index(bpioncoord.get('bfous2')))-7*x
            coord1=echiquier[p1]
            print('votre pion peut aller :\n',coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 :
                verification(coordfinal)
                bpioncoord.update({'bfous2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'devant gauche':
            p2=(echiquier.index(bpioncoord.get('bfous2')))-9*x
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord2:
                verification(coordfinal)
                bpioncoord.update({'bfous2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere droit':
            p3=(echiquier.index(bpioncoord.get('bfous2')))+9*x
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                bpioncoord.update({'bfous2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere gauche':
            p4=(echiquier.index(bpioncoord.get('bfous2')))+7*x
            coord4=echiquier[p4]
            print('votre pion peut aller :\n',coord4)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord4 :
                verification(coordfinal)
                bpioncoord.update({'bfous2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            print('relancer le jeux car vous vous etes tromper dans lécriture')
            
            
            
            
    if nompionb=='bfous1':
        deplacement=input("inscrivez la direction ou vous voulez déplacer ce pion, (devant droit, devant gauche, derriere droit, derriere gauche)")
        x=int(input('combien de case voulez-vous vous déplacer ?'))
        if deplacement == 'devant droit':        
            p1=(echiquier.index(bpioncoord.get('bfous1')))-7*x
            coord1=echiquier[p1]
            print('votre pion peut aller :\n',coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 :
                verification(coordfinal)
                bpioncoord.update({'bfous1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'devant gauche':
            p2=(echiquier.index(bpioncoord.get('bfous1')))-9*x
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord2:
                verification(coordfinal)
                bpioncoord.update({'bfous1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere droit':
            p3=(echiquier.index(bpioncoord.get('bfous1')))+9*x
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                bpioncoord.update({'bfous1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere gauche':
            p4=(echiquier.index(bpioncoord.get('bfous1')))+7*x
            coord4=echiquier[p4]
            print('votre pion peut aller :\n',coord4)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord4 :
                verification(coordfinal)
                bpioncoord.update({'bfous1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            print('relancer le jeux car vous vous etes tromper dans lécriture')
            
            
            
            
            
    if nompionb=='bcavalier1':
        deplacement=input("inscrivez la direction ou vous voulez déplacer ce pion, (devant droit, devant gauche, derriere droit, derriere gauche, gauche droit, gauche gauche, droit gauche, droit droit)")
        if deplacement == 'devant droit':        
            p1=(echiquier.index(bpioncoord.get('bcavalier1')))-15
            coord1=echiquier[p1]
            print('votre pion peut aller :\n',coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 :
                verification(coordfinal)
                bpioncoord.update({'bcavalier1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'devant gauche':
            p2=(echiquier.index(bpioncoord.get('bcavalier1')))-17
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord2:
                verification(coordfinal)
                bpioncoord.update({'bcavalier1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere droit':
            p3=(echiquier.index(bpioncoord.get('bcavalier1')))+17
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                bpioncoord.update({'bcavalier1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere gauche':
            p4=(echiquier.index(bpioncoord.get('bcavalier1')))+15
            coord4=echiquier[p4]
            print('votre pion peut aller :\n',coord4)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord4 :
                verification(coordfinal)
                bpioncoord.update({'bcavalier1':coordfinal})
        if deplacement == 'gauche droit':
            p5=(echiquier.index(bpioncoord.get('bcavalier1')))-10
            coord5=echiquier[p5]
            print('votre pion peut aller :\n',coord5)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord5 :
                verification(coordfinal)
                bpioncoord.update({'bcavalier1':coordfinal})
        if deplacement == 'gauche gauche':
            p6=(echiquier.index(bpioncoord.get('bcavalier1')))+6
            coord6=echiquier[p6]
            print('votre pion peut aller :\n',coord6)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord6 :
                verification(coordfinal)
                bpioncoord.update({'bcavalier1':coordfinal})
        if deplacement == 'droit gauche':
            p7=(echiquier.index(bpioncoord.get('bcavalier1')))-6
            coord7=echiquier[p7]
            print('votre pion peut aller :\n',coord7)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord7 :
                verification(coordfinal)
                bpioncoord.update({'bcavalier1':coordfinal})
        if deplacement == 'droit droit':
            p8=(echiquier.index(bpioncoord.get('bcavalier1')))+10
            coord8=echiquier[p8]
            print('votre pion peut aller :\n',coord8)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord8 :
                verification(coordfinal)
                bpioncoord.update({'bcavalier1':coordfinal})
                
        
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            print('relancer le jeux car vous vous etes tromper dans lécriture')
            
            
            
            
    if nompionb=='bcavalier2':
        deplacement=input("inscrivez la direction ou vous voulez déplacer ce pion, (devant droit, devant gauche, derriere droit, derriere gauche, gauche droit, gauche gauche, droit gauche, droit droit)")
        if deplacement == 'devant droit':        
            p1=(echiquier.index(bpioncoord.get('bcavalier2')))-15
            coord1=echiquier[p1]
            print('votre pion peut aller :\n',coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 :
                verification(coordfinal)
                bpioncoord.update({'bcavalier2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'devant gauche':
            p2=(echiquier.index(bpioncoord.get('bcavalier2')))-17
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord2:
                verification(coordfinal)
                bpioncoord.update({'bcavalier2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere droit':
            p3=(echiquier.index(bpioncoord.get('bcavalier2')))+17
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                bpioncoord.update({'bcavalier2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere gauche':
            p4=(echiquier.index(bpioncoord.get('bcavalier2')))+15
            coord4=echiquier[p4]
            print('votre pion peut aller :\n',coord4)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord4 :
                verification(coordfinal)
                bpioncoord.update({'bcavalier2':coordfinal})
        if deplacement == 'gauche droit':
            p5=(echiquier.index(bpioncoord.get('bcavalier2')))-10
            coord5=echiquier[p5]
            print('votre pion peut aller :\n',coord5)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord5 :
                verification(coordfinal)
                bpioncoord.update({'bcavalier2':coordfinal})
        if deplacement == 'gauche gauche':
            p6=(echiquier.index(bpioncoord.get('bcavalier2')))+6
            coord6=echiquier[p6]
            print('votre pion peut aller :\n',coord6)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord6 :
                verification(coordfinal)
                bpioncoord.update({'bcavalier2':coordfinal})
        if deplacement == 'droit gauche':
            p7=(echiquier.index(bpioncoord.get('bcavalier2')))-6
            coord7=echiquier[p7]
            print('votre pion peut aller :\n',coord7)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord7 :
                verification(coordfinal)
                bpioncoord.update({'bcavalier2':coordfinal})
        if deplacement == 'droit droit':
            p8=(echiquier.index(bpioncoord.get('bcavalier2')))+10
            coord8=echiquier[p8]
            print('votre pion peut aller :\n',coord8)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord8 :
                verification(coordfinal)
                bpioncoord.update({'bcavalier2':coordfinal})
                
        
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            print('relancer le jeux car vous vous etes tromper dans lécriture')
            
            
            
            
    if nompionb=='breine':
        deplacement=input("inscrivez la direction ou vous voulez déplacer ce pion, (devant, derriere, droite, gauche, devant gauche, devant droit, derriere gauche, derriere droit)")
        x=int(input('combien de case voulez-vous vous déplacer ?'))
        if deplacement == 'devant':        
            p1=(echiquier.index(bpioncoord.get('breine')))-8*x
            coord1=echiquier[p1]
            print('votre pion peut aller :\n',coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 :
                verification(coordfinal)
                bpioncoord.update({'breine':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere':
            p2=(echiquier.index(bpioncoord.get('breine')))+8*x
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord2:
                verification(coordfinal)
                bpioncoord.update({'breine':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'droite':
            p3=(echiquier.index(bpioncoord.get('breine')))+x
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                bpioncoord.update({'breine':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'gauche':
            p4=(echiquier.index(bpioncoord.get('breine')))-x
            coord4=echiquier[p4]
            print('votre pion peut aller :\n',coord4)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord4 :
                verification(coordfinal)
                bpioncoord.update({'breine':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'devant droit':        
            p5=(echiquier.index(bpioncoord.get('breine')))-7*x
            coord5=echiquier[p5]
            print('votre pion peut aller :\n',coord5)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord5 :
                verification(coordfinal)
                bpioncoord.update({'breine':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'devant gauche':
            p6=(echiquier.index(bpioncoord.get('breine')))-9*x
            coord6=echiquier[p6]
            print('votre pion peut aller :\n',coord6)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord6:
                verification(coordfinal)
                bpioncoord.update({'breine':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere droit':
            p7=(echiquier.index(bpioncoord.get('breine')))+9*x
            coord7=echiquier[p7]
            print('votre pion peut aller :\n',coord7)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord7 :
                verification(coordfinal)
                bpioncoord.update({'breine':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere gauche':
            p8=(echiquier.index(bpioncoord.get('breine')))+7*x
            coord8=echiquier[p8]
            print('votre pion peut aller :\n',coord8)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord8 :
                verification(coordfinal)
                bpioncoord.update({'breine':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        
                
            
        else:
            print('relancer le jeux car vous vous etes tromper dans lécriture')
            
            
            
            
            
    if nompionb=='broi':
        deplacement=input("inscrivez la direction ou vous voulez déplacer ce pion, (devant, derriere, droite, gauche, devant gauche, devant droit, derriere gauche, derriere droit)")
        if deplacement == 'devant':        
            p1=(echiquier.index(bpioncoord.get('broi')))-8
            coord1=echiquier[p1]
            print('votre pion peut aller :\n',coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 :
                verification(coordfinal)
                bpioncoord.update({'broi':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere':
            p2=(echiquier.index(bpioncoord.get('broi')))+8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord2:
                verification(coordfinal)
                bpioncoord.update({'broi':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'droite':
            p3=(echiquier.index(bpioncoord.get('broi')))+1
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                bpioncoord.update({'broi':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'gauche':
            p4=(echiquier.index(bpioncoord.get('broi')))-1
            coord4=echiquier[p4]
            print('votre pion peut aller :\n',coord4)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord4 :
                verification(coordfinal)
                bpioncoord.update({'broi':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'devant droit':        
            p5=(echiquier.index(bpioncoord.get('broi')))-7
            coord5=echiquier[p5]
            print('votre pion peut aller :\n',coord5)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord5 :
                verification(coordfinal)
                bpioncoord.update({'broi':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'devant gauche':
            p6=(echiquier.index(bpioncoord.get('broi')))-9
            coord6=echiquier[p6]
            print('votre pion peut aller :\n',coord6)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord6:
                verification(coordfinal)
                bpioncoord.update({'broi':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere droit':
            p7=(echiquier.index(bpioncoord.get('broi')))+9
            coord7=echiquier[p7]
            print('votre pion peut aller :\n',coord7)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord7 :
                verification(coordfinal)
                bpioncoord.update({'broi':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere gauche':
            p8=(echiquier.index(bpioncoord.get('broi')))+7
            coord8=echiquier[p8]
            print('votre pion peut aller :\n',coord8)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord8 :
                verification(coordfinal)
                bpioncoord.update({'broi':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        
                
            
        else:
            print('relancer le jeux car vous vous etes tromper dans lécriture')
        




def mouvementnoir():

    nompionn=str(input('joueur noir: entrez le nom du pion que vous voulez déplacer :\n'))
    if nompionn=='npion1':
        if npioncoord['npion1']=='b1':
            p1=(echiquier.index(npioncoord.get('npion1')))+16
            coord1=echiquier[p1]
            p2=(echiquier.index(npioncoord.get('npion1')))+8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2,", ",coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )

            if coordfinal == coord1 or coordfinal == coord2:
                verification(coordfinal)
                npioncoord.update({'npion1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            p3=(echiquier.index(npioncoord.get('npion1')))+8
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisisez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                npioncoord.update({'npion1':coordfinal})





    if nompionn=='npion2':
      if npioncoord['npion2']=='b2':
            p1=(echiquier.index(npioncoord.get('npion2')))+16
            coord1=echiquier[p1]
            p2=(echiquier.index(npioncoord.get('npion2')))+8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2,", ",coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 or coordfinal == coord2:
                verification(coordfinal)
                npioncoord.update({'npion2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
      else:
            p3=(echiquier.index(npioncoord.get('npion2')))+8
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisisez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                npioncoord.update({'npion2':coordfinal})



    if nompionn=='npion3':
        if npioncoord['npion3']=='b3':
            p1=(echiquier.index(npioncoord.get('npion3')))+16
            coord1=echiquier[p1]
            p2=(echiquier.index(npioncoord.get('npion3')))+8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2,", ",coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 or coordfinal == coord2:
                verification(coordfinal)
                npioncoord.update({'npion3':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            p3=(echiquier.index(npioncoord.get('npion3')))+8
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisisez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                npioncoord.update({'npion3':coordfinal})



    if nompionn=='npion4':
        if npioncoord['npion4']=='b4':
            p1=(echiquier.index(npioncoord.get('npion4')))+16
            coord1=echiquier[p1]
            p2=(echiquier.index(npioncoord.get('npion4')))+8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2,", ",coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 or coordfinal == coord2:
                verification(coordfinal)
                npioncoord.update({'npion4':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            p3=(echiquier.index(npioncoord.get('npion4')))+8
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisisez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                npioncoord.update({'npion4':coordfinal})



    if nompionn=='npion5':
       if npioncoord['npion5']=='b5':
            p1=(echiquier.index(npioncoord.get('npion5')))+16
            coord1=echiquier[p1]
            p2=(echiquier.index(npioncoord.get('npion5')))+8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2,", ",coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 or coordfinal == coord2:
                verification(coordfinal)
                npioncoord.update({'npion5':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
       else:
            p3=(echiquier.index(npioncoord.get('npion5')))+8
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisisez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                npioncoord.update({'npion5':coordfinal})



    if nompionn=='npion6':
       if npioncoord['npion6']=='b6':
            p1=(echiquier.index(npioncoord.get('npion6')))+16
            coord1=echiquier[p1]
            p2=(echiquier.index(npioncoord.get('npion6')))+8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2,", ",coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 or coordfinal == coord2:
                verification(coordfinal)
                npioncoord.update({'npion6':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
       else:
            p3=(echiquier.index(npioncoord.get('npion6')))+8
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisisez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                npioncoord.update({'npion6':coordfinal})



    if nompionn=='npion7':
        if npioncoord['npion7']=='b7':
            p1=(echiquier.index(npioncoord.get('npion7')))+16
            coord1=echiquier[p1]
            p2=(echiquier.index(npioncoord.get('npion7')))+8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2,", ",coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 or coordfinal == coord2:
                verification(coordfinal)
                npioncoord.update({'npion7':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            p3=(echiquier.index(npioncoord.get('npion7')))+8
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisisez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                npioncoord.update({'npion7':coordfinal})



    if nompionn=='npion8':
        if npioncoord['npion8']=='b8':
            p1=(echiquier.index(npioncoord.get('npion8')))+16
            coord1=echiquier[p1]
            p2=(echiquier.index(npioncoord.get('npion8')))+8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2,", ",coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 or coordfinal == coord2:
                verification(coordfinal)
                npioncoord.update({'npion8':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            p3=(echiquier.index(npioncoord.get('npion8')))+8
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisisez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                npioncoord.update({'npion8':coordfinal})









    if nompionn=='ntour1':
        deplacement=input("inscrivez la direction ou vous voulez déplacer ce pion, (devant, derriere, droite, gauche)")
        x=int(input('combien de case voulez-vous vous déplacer ?'))
        if deplacement == 'devant':        
            p1=(echiquier.index(npioncoord.get('ntour1')))+8*x
            coord1=echiquier[p1]
            print('votre pion peut aller :\n',coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 :
                verification(coordfinal)
                npioncoord.update({'ntour1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere':
            p2=(echiquier.index(npioncoord.get('ntour1')))-8*x
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord2:
                verification(coordfinal)
                npioncoord.update({'ntour1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'droite':
            p3=(echiquier.index(npioncoord.get('ntour1')))-x
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                npioncoord.update({'ntour1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'gauche':
            p4=(echiquier.index(npioncoord.get('ntour1')))+x
            coord4=echiquier[p4]
            print('votre pion peut aller :\n',coord4)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord4 :
                verification(coordfinal)
                npioncoord.update({'ntour1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            print('relancer le jeux car vous vous etes tromper dans lécriture')
            
            


    if nompionn=='ntour2':
        deplacement=input("inscrivez la direction ou vous voulez déplacer ce pion, (devant, derriere, droite, gauche)")
        x=int(input('combien de case voulez-vous vous déplacer ?'))
        if deplacement == 'devant':        
            p1=(echiquier.index(npioncoord.get('ntour2')))+8*x
            coord1=echiquier[p1]
            print('votre pion peut aller :\n',coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 :
                verification(coordfinal)
                npioncoord.update({'ntour2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere':
            p2=(echiquier.index(npioncoord.get('ntour2')))-8*x
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord2:
                verification(coordfinal)
                npioncoord.update({'ntour2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'droite':
            p3=(echiquier.index(npioncoord.get('ntour2')))-x
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                npioncoord.update({'ntour2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'gauche':
            p4=(echiquier.index(npioncoord.get('ntour2')))+x
            coord4=echiquier[p4]
            print('votre pion peut aller :\n',coord4)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord4 :
                verification(coordfinal)
                npioncoord.update({'ntour2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            print('relancer le jeux car vous vous etes tromper dans lécriture')
        
        
        
        
        
        
        
        

        

    if nompionn=='nfous2':
        deplacement=input("inscrivez la direction ou vous voulez déplacer ce pion, (devant droit, devant gauche, derriere droit, derriere gauche)")
        x=int(input('combien de case voulez-vous vous déplacer ?'))
        if deplacement == 'devant droit':        
            p1=(echiquier.index(npioncoord.get('nfous2')))+7*x
            coord1=echiquier[p1]
            print('votre pion peut aller :\n',coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 :
                verification(coordfinal)
                npioncoord.update({'nfous2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'devant gauche':
            p2=(echiquier.index(npioncoord.get('nfous2')))+9*x
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord2:
                verification(coordfinal)
                npioncoord.update({'nfous2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere droit':
            p3=(echiquier.index(npioncoord.get('nfous2')))-9*x
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                npioncoord.update({'nfous2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere gauche':
            p4=(echiquier.index(npioncoord.get('nfous2')))-7*x
            coord4=echiquier[p4]
            print('votre pion peut aller :\n',coord4)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord4 :
                verification(coordfinal)
                npioncoord.update({'nfous2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            print('relancer le jeux car vous vous etes tromper dans lécriture')
            
            
            
            
    if nompionn=='nfous1':
        deplacement=input("inscrivez la direction ou vous voulez déplacer ce pion, (devant droit, devant gauche, derriere droit, derriere gauche)")
        x=int(input('combien de case voulez-vous vous déplacer ?'))
        if deplacement == 'devant droit':        
            p1=(echiquier.index(npioncoord.get('nfous1')))+7*x
            coord1=echiquier[p1]
            print('votre pion peut aller :\n',coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 :
                verification(coordfinal)
                npioncoord.update({'nfous1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'devant gauche':
            p2=(echiquier.index(npioncoord.get('nfous1')))+9*x
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord2:
                verification(coordfinal)
                npioncoord.update({'nfous1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere droit':
            p3=(echiquier.index(npioncoord.get('nfous1')))-9*x
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                npioncoord.update({'nfous1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere gauche':
            p4=(echiquier.index(npioncoord.get('nfous1')))-7*x
            coord4=echiquier[p4]
            print('votre pion peut aller :\n',coord4)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord4 :
                verification(coordfinal)
                npioncoord.update({'nfous1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            print('relancer le jeux car vous vous etes tromper dans lécriture')
            
            
            
            
            
    if nompionn=='ncavalier1':
        deplacement=input("inscrivez la direction ou vous voulez déplacer ce pion, (devant droit, devant gauche, derriere droit, derriere gauche, gauche droit, gauche gauche, droit gauche, droit droit)")
        if deplacement == 'devant droit':        
            p1=(echiquier.index(npioncoord.get('ncavalier1')))+15
            coord1=echiquier[p1]
            print('votre pion peut aller :\n',coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 :
                verification(coordfinal)
                npioncoord.update({'ncavalier1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'devant gauche':
            p2=(echiquier.index(npioncoord.get('ncavalier1')))+17
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord2:
                verification(coordfinal)
                npioncoord.update({'ncavalier1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere droit':
            p3=(echiquier.index(npioncoord.get('ncavalier1')))-17
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                npioncoord.update({'ncavalier1':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere gauche':
            p4=(echiquier.index(npioncoord.get('ncavalier1')))-15
            coord4=echiquier[p4]
            print('votre pion peut aller :\n',coord4)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord4 :
                verification(coordfinal)
                npioncoord.update({'ncavalier1':coordfinal})
        if deplacement == 'gauche droit':
            p5=(echiquier.index(npioncoord.get('ncavalier1')))+10
            coord5=echiquier[p5]
            print('votre pion peut aller :\n',coord5)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord5 :
                verification(coordfinal)
                npioncoord.update({'ncavalier1':coordfinal})
        if deplacement == 'gauche gauche':
            p6=(echiquier.index(npioncoord.get('ncavalier1')))-6
            coord6=echiquier[p6]
            print('votre pion peut aller :\n',coord6)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord6 :
                verification(coordfinal)
                npioncoord.update({'ncavalier1':coordfinal})
        if deplacement == 'droit gauche':
            p7=(echiquier.index(npioncoord.get('ncavalier1')))+6
            coord7=echiquier[p7]
            print('votre pion peut aller :\n',coord7)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord7 :
                verification(coordfinal)
                npioncoord.update({'ncavalier1':coordfinal})
        if deplacement == 'droit droit':
            p8=(echiquier.index(npioncoord.get('ncavalier1')))-10
            coord8=echiquier[p8]
            print('votre pion peut aller :\n',coord8)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord8 :
                verification(coordfinal)
                npioncoord.update({'ncavalier1':coordfinal})
                
        
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            print('relancer le jeux car vous vous etes tromper dans lécriture')
            
            
            
            
    if nompionn=='ncavalier2':
        deplacement=input("inscrivez la direction ou vous voulez déplacer ce pion, (devant droit, devant gauche, derriere droit, derriere gauche, gauche droit, gauche gauche, droit gauche, droit droit)")
        if deplacement == 'devant droit':        
            p1=(echiquier.index(npioncoord.get('ncavalier2')))+15
            coord1=echiquier[p1]
            print('votre pion peut aller :\n',coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 :
                verification(coordfinal)
                npioncoord.update({'ncavalier2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'devant gauche':
            p2=(echiquier.index(npioncoord.get('ncavalier2')))+17
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord2:
                verification(coordfinal)
                npioncoord.update({'ncavalier2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere droit':
            p3=(echiquier.index(npioncoord.get('ncavalier2')))-17
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                npioncoord.update({'ncavalier2':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere gauche':
            p4=(echiquier.index(npioncoord.get('ncavalier2')))-15
            coord4=echiquier[p4]
            print('votre pion peut aller :\n',coord4)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord4 :
                verification(coordfinal)
                npioncoord.update({'ncavalier2':coordfinal})
        if deplacement == 'gauche droit':
            p5=(echiquier.index(npioncoord.get('ncavalier2')))+10
            coord5=echiquier[p5]
            print('votre pion peut aller :\n',coord5)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord5 :
                verification(coordfinal)
                npioncoord.update({'ncavalier2':coordfinal})
        if deplacement == 'gauche gauche':
            p6=(echiquier.index(npioncoord.get('ncavalier2')))-6
            coord6=echiquier[p6]
            print('votre pion peut aller :\n',coord6)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord6 :
                verification(coordfinal)
                npioncoord.update({'ncavalier2':coordfinal})
        if deplacement == 'droit gauche':
            p7=(echiquier.index(npioncoord.get('ncavalier2')))+6
            coord7=echiquier[p7]
            print('votre pion peut aller :\n',coord7)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord7 :
                verification(coordfinal)
                npioncoord.update({'ncavalier2':coordfinal})
        if deplacement == 'droit droit':
            p8=(echiquier.index(npioncoord.get('ncavalier2')))-10
            coord8=echiquier[p8]
            print('votre pion peut aller :\n',coord8)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord8 :
                verification(coordfinal)
                npioncoord.update({'ncavalier2':coordfinal})
                
        
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        else:
            print('relancer le jeux car vous vous etes tromper dans lécriture')
            
            
            
            
    if nompionn=='nreine':
        deplacement=input("inscrivez la direction ou vous voulez déplacer ce pion, (devant, derriere, droite, gauche, devant gauche, devant droit, derriere gauche, derriere droit)")
        x=int(input('combien de case voulez-vous vous déplacer ?'))
        if deplacement == 'devant':        
            p1=(echiquier.index(npioncoord.get('nreine')))+8*x
            coord1=echiquier[p1]
            print('votre pion peut aller :\n',coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 :
                verification(coordfinal)
                npioncoord.update({'nreine':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere':
            p2=(echiquier.index(npioncoord.get('nreine')))-8*x
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord2:
                verification(coordfinal)
                npioncoord.update({'nreine':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'droite':
            p3=(echiquier.index(npioncoord.get('nreine')))-x
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                npioncoord.update({'nreine':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'gauche':
            p4=(echiquier.index(npioncoord.get('nreine')))+x
            coord4=echiquier[p4]
            print('votre pion peut aller :\n',coord4)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord4 :
                verification(coordfinal)
                npioncoord.update({'nreine':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'devant droit':        
            p5=(echiquier.index(npioncoord.get('nreine')))+7*x
            coord5=echiquier[p5]
            print('votre pion peut aller :\n',coord5)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord5 :
                verification(coordfinal)
                npioncoord.update({'nreine':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'devant gauche':
            p6=(echiquier.index(npioncoord.get('nreine')))+9*x
            coord6=echiquier[p6]
            print('votre pion peut aller :\n',coord6)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord6:
                verification(coordfinal)
                npioncoord.update({'nreine':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere droit':
            p7=(echiquier.index(npioncoord.get('nreine')))-9*x
            coord7=echiquier[p7]
            print('votre pion peut aller :\n',coord7)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord7 :
                verification(coordfinal)
                npioncoord.update({'nreine':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere gauche':
            p8=(echiquier.index(npioncoord.get('nreine')))-7*x
            coord8=echiquier[p8]
            print('votre pion peut aller :\n',coord8)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord8 :
                verification(coordfinal)
                npioncoord.update({'nreine':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        
                
            
        else:
            print('relancer le jeux car vous vous etes tromper dans lécriture')
            
            
            
            
            
    if nompionn=='nroi':
        deplacement=input("inscrivez la direction ou vous voulez déplacer ce pion, (devant, derriere, droite, gauche, devant gauche, devant droit, derriere gauche, derriere droit)")
        if deplacement == 'devant':        
            p1=(echiquier.index(npioncoord.get('nroi')))+8
            coord1=echiquier[p1]
            print('votre pion peut aller :\n',coord1)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord1 :
                verification(coordfinal)
                npioncoord.update({'nroi':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere':
            p2=(echiquier.index(npioncoord.get('nroi')))-8
            coord2=echiquier[p2]
            print('votre pion peut aller :\n',coord2)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord2:
                verification(coordfinal)
                npioncoord.update({'nbroi':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'droite':
            p3=(echiquier.index(npioncoord.get('nroi')))-1
            coord3=echiquier[p3]
            print('votre pion peut aller :\n',coord3)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord3 :
                verification(coordfinal)
                npioncoord.update({'nroi':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'gauche':
            p4=(echiquier.index(npioncoord.get('nroi')))+1
            coord4=echiquier[p4]
            print('votre pion peut aller :\n',coord4)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord4 :
                verification(coordfinal)
                npioncoord.update({'nroi':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'devant droit':        
            p5=(echiquier.index(npioncoord.get('nroi')))+7
            coord5=echiquier[p5]
            print('votre pion peut aller :\n',coord5)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord5 :
                verification(coordfinal)
                npioncoord.update({'nroi':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'devant gauche':
            p6=(echiquier.index(npioncoord.get('nroi')))+9
            coord6=echiquier[p6]
            print('votre pion peut aller :\n',coord6)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord6:
                verification(coordfinal)
                npioncoord.update({'nroi':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere droit':
            p7=(echiquier.index(npioncoord.get('nroi')))-9
            coord7=echiquier[p7]
            print('votre pion peut aller :\n',coord7)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord7 :
                verification(coordfinal)
                npioncoord.update({'nroi':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        if deplacement == 'derriere gauche':
            p8=(echiquier.index(npioncoord.get('nroi')))-7
            coord8=echiquier[p8]
            print('votre pion peut aller :\n',coord8)
            coordfinal=input('quelle coordonnée vous choisissez ?:' )
            if coordfinal == coord8 :
                verification(coordfinal)
                npioncoord.update({'nroi':coordfinal})
            else :
                print('erreur mauvaise coordonée relancer le jeux')
        
                
            
        else:
            print('relancer le jeux car vous vous etes tromper dans lécriture')
        


