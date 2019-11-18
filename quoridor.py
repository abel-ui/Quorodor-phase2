class Quoridor:

    def __init__(self, joueurs, murs=None):
        """
        Initialiser une partie de Quoridor avec les joueurs et les murs spécifiés, 
        en s'assurant de faire une copie profonde de tout ce qui a besoin d'être copié.

        :param joueurs: un itérable de deux joueurs dont le premier est toujours celui qui 
        débute la partie. Un joueur est soit une chaîne de caractères soit un dictionnaire. 
        Dans le cas d'une chaîne, il s'agit du nom du joueur. Selon le rang du joueur dans 
        l'itérable, sa position est soit (5,1) soit (5,9), et chaque joueur peut initialement
        placer 10 murs. Dans le cas où l'argument est un dictionnaire, celui-ci doit contenir 
        une clé 'nom' identifiant le joueur, une clé 'murs' spécifiant le nombre de murs qu'il 
        peut encore placer, et une clé 'pos' qui spécifie sa position (x, y) actuelle.
        
        :param murs: un dictionnaire contenant une clé 'horizontaux' associée à la liste des
        positions (x, y) des murs horizontaux, et une clé 'verticaux' associée à la liste des
        positions (x, y) des murs verticaux. Par défaut, il n'y a aucun mur placé sur le jeu.

        :raises QuoridorError: si joueurs n'est pas itérable.
        :raises QuoridorError: si l'itérable de joueurs en contient plus de deux.
        :raises QuoridorError: si le nombre de murs qu'un joueur peut placer est >10, ou négatif.
        :raises QuoridorError: si la position d'un joueur est invalide.
        :raises QuoridorError: si murs n'est pas un dictionnaire lorsque présent.
        :raises QuoridorError: si le total des murs placés et plaçables n'est pas égal à 20.
        :raises QuoridorError: si la position d'un mur est invalide.
        """
        self.joueur1 = joueurs[0]
        self.joueur2 = joueurs[1]
        self.murs = murs
        self.état_partie = {'joueurs': [{'nom': self.joueur1, 'murs': 10, 'pos': [5, 1]},
                           {'nom': self.joueur2, 'murs': 10, 'pos': [5, 9]}], 'murs': {'horizontaux': [],
                            'verticaux': []}}
        if hasattr(joueurs, '__iter__') is False:
            raise QuorridorError
        if len(joueurs) > 2:
            raise QuorridorError
        for j in self.état_partie['joueurs']:
            if j['murs'] > 10 or j['murs'] < 0:
                raise QuorridorError
            if j['pos'][0] > 9 or j['pos'][0] < 1:
                raise QuoridorError
            if j['pos'][1] > 9 or j['pos'][1] < 1:
                raise QuorridorError
        if self.état_partie.get('murs'):
            if type(self.état_partie['murs']) != dict:
                raise QuorridorError
        a = self.état_partie['joueurs'][0]['murs'] + self.état_partie['joueurs'][1]['murs']
        b = len(self.état_partie['murs']['horizontaux']) + len(self.état_partie['murs']['verticaux'])
        if (a + b) != 20:
            raise QuorridorError
        for m in self.état_partie['murs']['horizontaux']:
            if m[0] < 1 or m[0] > 8:
                raise QuorridorError
            if m[1] < 2 or m[1] > 9:
                raise QuorridorError
        for m in self.état_partie['murs']['verticaux']:
            if m[0] < 2 or m[0] > 9:
                raise QuorridorError
            if m[1] < 1 or m[1] > 8:
                raise QuorridorError
        

        
        
    def __str__(self):
        """
        Produire la représentation en art ascii correspondant à l'état actuel de la partie. 
        Cette représentation est la même que celle du TP précédent.

        :returns: la chaîne de caractères de la représentation.
        """
        deb = 'Légende: 1='+str(self.état_partie['joueurs'][0]['nom'])+' 2=automate'+'\n'+'   '+35*'-'+'\n'
    sui = ''
    for i in range(8):
        sui += str(9-i)+' | '+8*'.   '+'. |'+'\n'+'  |                                   |'+'\n'
    fin = '1 |' + ' .  '*8 + ' . |'+'\n'+'--|' + '-'*35 + '\n'
    fin2 = '  | 1   2   3   4   5   6   7   8   9'
    tot = list(sui+fin+fin2)
    for j in range(len(self.état_partie)):
        tot[40*(18-2*self.état_partie['joueurs'][j]['pos'][1])+4*dico['joueurs'][j]['pos'][0]] = str(j+1)
    for i in self.état_partie['murs']['horizontaux']:
        for ading in range(7):
            tot[40*(19-2*i[1])+4*i[0]-1+ading] = '-'
    for place in self.état_partie['murs']['verticaux']:
        for adding in range(3):
            tot[40*(18-adding-2*place[1])+4*place[0]-2] = '|'
    return deb + ''.join(tot)

    def déplacer_jeton(self, joueur, position):
        """
        Pour le joueur spécifié, déplacer son jeton à la position spécifiée.

        :param joueur: un entier spécifiant le numéro du joueur (1 ou 2).
        :param position: le tuple (x, y) de la position du jeton (1<=x<=9 et 1<=y<=9).
        :raises QuoridorError: le numéro du joueur est autre que 1 ou 2.
        :raises QuoridorError: la position est invalide (en dehors du damier).
        :raises QuoridorError: la position est invalide pour l'état actuel du jeu.
        """

    def état_partie(self):
        """
        Produire l'état actuel de la partie.

        :returns: une copie de l'état actuel du jeu sous la forme d'un dictionnaire:
        {
            'joueurs': [
                {'nom': nom1, 'murs': n1, 'pos': (x1, y1)},
                {'nom': nom2, 'murs': n2, 'pos': (x2, y2)},
            ]
            'Murs': {
                'horizontaux': [...],
                'verticaux': [...],
            }
        }
        
        où la clé 'nom' d'un joueur est associée à son nom, la clé 'murs' est associée 
        au nombre de murs qu'il peut encore placer sur ce damier, et la clé 'pos' est 
        associée à sa position sur le damier. Une position est représentée par un tuple 
        de deux coordonnées x et y, où 1<=x<=9 et 1<=y<=9.

        Les murs actuellement placés sur le damier sont énumérés dans deux listes de
        positions (x, y). Les murs ont toujours une longueur de 2 cases et leur position
        est relative à leur coin inférieur gauche. Par convention, un mur horizontal se
        situe entre les lignes y-1 et y, et bloque les colonnes x et x+1. De même, un
        mur vertical se situe entre les colonnes x-1 et x, et bloque les lignes x et x+1.
        """

    def jouer_coup(self, joueur):
        """
        Pour le joueur spécifié, jouer automatiquement son meilleur coup pour l'état actuel 
        de la partie. Ce coup est soit le déplacement de son jeton, soit le placement d'un 
        mur horizontal ou vertical.

        :param joueur: un entier spécifiant le numéro du joueur (1 ou 2).
        :raises QuoridorError: le numéro du joueur est autre que 1 ou 2.
        :raises QuoridorError: la partie est déjà terminée.
        """

    def partie_terminée(self):
        """
        Déterminer si la partie est terminée.

        :returns: le nom du gagnant si la partie est terminée; False autrement.
        """

    def placer_mur(self, joueur: int, position: tuple, orientation: str):
        """
        Pour le joueur spécifié, placer un mur à la position spécifiée.

        :param joueur: le numéro du joueur (1 ou 2).
        :param position: le tuple (x, y) de la position du mur.
        :param orientation: l'orientation du mur ('horizontal' ou 'vertical').
        :raises QuoridorError: le numéro du joueur est autre que 1 ou 2.
        :raises QuoridorError: un mur occupe déjà cette position.
        :raises QuoridorError: la position est invalide pour cette orientation.
        :raises QuoridorError: le joueur a déjà placé tous ses murs.
        """
class QuorridorError(Exception):

