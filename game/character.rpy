init:
    $ clair_name = renpy.random.choice(["Evangeline", "Isadora", "Lenore", "Ophelia", "Allegra", "Thalia", "Cassandra", "Viola", "Rosalind", "Rowena"])
    $ scholar_name = renpy.random.choice(["Percival", "Reginald", "Cyril", "Augustus", "Cornelius", "Winston", "Alastair", "Benedict", "Atticus", "Leopold"])
    $ caretaker_name = renpy.random.choice(["Mathilde", "Prudence", "Eleanor", "Beatrice", "Agnes", "Edith", "Constance", "Winifred", "Agatha", "Mabel"])
    $ priest_name = "Father " + renpy.random.choice(["Thorne", "Blackwell", "Etheridge", "Pendleton", "Holbrook", "Whitman", "Fitzwilliam", "Fields", "Stone", "Crilly"])
    $ invest_name = renpy.random.choice(["Cordelia", "Rosamund", "Alberta", "Arabella", "Imogen", "Gwendolyn", "Felicity", "Josephine", "Eliza", "Harriet"])
    $ journalist_name = renpy.random.choice(["Oliver", "Jasper", "Percy", "Rupert", "Sebastian", "Arthur", "Felix", "Theodore", "Edmund", "Gilbert"])

#Clairvoyant define
define cl = Character(clair_name)
image cl = "CPortraits/clairvoyant.png"
default cl_trust = 5 # Out of a possible 50
default cl_str = 5
default cl_dex = 7
default cl_cha = 4
default cl_per = 6
default cl_luck = 6
default cl_HP = 70

#Scholar Define
define s = Character(scholar_name)
image s = "CPortraits/scholar.png"
default s_trust = 10 # Out of a possible 50
default s_str = 8
default s_dex = 6
default s_cha = 6
default s_per = 4
default s_luck = 4
default s_HP = 85

#Priest define
define p = Character(priest_name)
image p = "CPortraits/priest.png"
default p_trust = 15 # Out of a possible 50
default p_str = 3
default p_dex = 6
default p_cha = 6
default p_per = 5
default p_luck = 8
default p_HP = 65

#Investigator define
define i = Character(invest_name)
image i = "CPortraits/investigator.png"
default i_trust = 0 # Out of a possible 50
default i_str = 7
default i_dex = 5
default i_cha = 5
default i_per = 8
default i_luck = 3
default i_HP = 85

#Caretaker define
define ca = Character(caretaker_name)
image ca = "CPortraits/caretaker.png"
default ca_trust = -5 # Out of a possible 50
default ca_str = 3
default ca_dex = 5
default ca_cha = 6
default ca_per = 9
default ca_luck = 5
default ca_HP = 55

#Journalist define
define j = Character(journalist_name)
image j = "CPortraits/journalist.png"
default j_trust = 5 # Out of a possible 50
default j_str = 6
default j_dex = 5
default j_cha = 7
default j_per = 7
default j_luck = 3
default j_HP = 80