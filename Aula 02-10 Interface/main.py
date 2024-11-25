from eleicao import Urna
from common import *

candidatos = list([Candidato('sla', 43, 234, 4), Candidato('sla2', 413, 2234, 44)])
eleitor1 = Eleitor('asas', 43 ,12 ,6, 1, 3)
eleitor2 = Eleitor('aaaasas', 413 ,112 ,62, 14, 37)

eleitores = list([eleitor1, eleitor2])

urna = Urna(Eleitor('bro resenha', 432, 12, 534, 234, 1), 543, 23, candidatos, eleitores)

urna.to_csv()