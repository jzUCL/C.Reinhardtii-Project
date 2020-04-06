import csv


class Promoter(object):
    # Class Attribute
    type = 'Promoter'

    # properties, sequences, extracted from csv file
    # Initializer/Instance Attributes:
    def __init__(self, name, sequence, strength):
        self.name = name
        self.sequence = sequence
        self.strength = strength


class FivePrimeUtr(object):
    # Class Attribute
    type = '5UTR'

    # properties, sequences, extracted from csv file
    # Initializer/Instance Attributes:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

    # Instance Methods:


class Genes(object):
    # Class Attribute
    type = 'Gene'

    # genes, sequences, extracted from csv file
    # Initializer/Instance Attributes:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence


class Connect(object):
    # Class Attribute
    type = 'Gene'

    # genes, sequences, extracted from csv file
    # Initializer/Instance Attributes:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

    # Instance Methods:

class ThreePrimeUtr(object):
    # Class Attribute
    type = '3UTR'

    # properties, sequences, extracted from csv file
    # Initializer/Instance Attributes:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence


def CompiledSequences(Promoter, FivePrimeUtr, Genes):
    Cassette_name = Promoter.name + FivePrimeUtr.name + Genes.name
    Cassette = Promoter.sequence + FivePrimeUtr.sequence + Genes.sequence
    return Cassette_name, Cassette


File_Promoters = []
with open('Promoters.csv', 'r') as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        File_Promoters.append(Promoter(row[0], row[1], row[2]))

File_FiveUtrs = []
with open('5UTR.csv', 'r') as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        File_FiveUtrs.append(FivePrimeUtr(row[0], row[1]))

File_Genes = []
with open('Genes.csv', 'r') as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        File_Genes.append(Genes(row[0], row[1]))

File_ThreeUtrs= []
with open('3UTR.csv', 'r') as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        File_ThreeUtrs.append(ThreePrimeUtr(row[0], row[1]))

File_ConnectingSeq = []
with open('connectingseq.csv', 'r') as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        File_ConnectingSeq.append(Connect(row[0], row[1]))



# kivy setup - layout, stacking,
# 3 boxes on left-  dropown to set value of promoter - initial picture showing the promoter/utr/genes - set value
# when ready - sequences show in box - construct total cassete sequence
# load cassettes constructed into lower box.

superpromoter = Promoter("Promoter1", "CTATATCGCG", 5)
superUTR = FivePrimeUtr("UTR1", "GAGATAGAGA")
superGENE = Genes("Gene1", "ATATATATATATA")

CassetteName1, Cassette1 = CompiledSequences(superpromoter, superUTR, superGENE)
# print("Cassette: ", CassetteName1, Cassette1)

# print(File_FiveUtrs[-1].name, File_FiveUtrs[-1].sequence, File_Genes[-1].name, File_Promoters[-1].name)

randomcassette_name, random_cassette = CompiledSequences(File_Promoters[-1], File_FiveUtrs[-1], File_Genes[-1])
# print("Cassette: ", randomcassette_name, random_cassette)
