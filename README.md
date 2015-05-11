# README #

## DCAF - Discrimination, Comparison, Alignment tool for small molecules ##

DCAF is a method for describing molecules' pharmacophoric properties and a fast and efective tool for comparing and combining ligands.

DCAF is written as a Python module and can be easily combined with OpenBabel, RDKit and other chemoinformatic tools.


## Examples ##

### Basic example: ###
```
#!python

#use RDKit
from rdkit.Chem import MolFromSmiles
from dcaf.toolkits import rd
from dcaf.utils import similarity, combine_pharmacophores, draw

#create models
mol1 = MolFromSmiles("c1cc(cc(c1)N)c1cc(cc(c1O)c1[nH]c2ccc(cc2n1)C(=N)N)Cl")
phar1 = rd.phar_from_mol(mol1)
mol2 = MolFromSmiles("c1cc(cc(c1)N(=O)=O)c1cc(cc(c1O)c1cc2cc(ccc2[nH]1)C(=N)N)CC(=O)O")
phar2 = rd.phar_from_mol(mol2)

#compare and combine models
print similarity(phar1, phar2)
phar = combine_pharmacophores(phar1, phar2)

#draw pharmacophore
draw(phar)
```

### Demos ###
There are also three demo scripts, showing prossible applications of DCAF:

* compare_demo.py - compare two sets of ligands to refrence set
* filter_demo.py - screen database for molecules similar to given pharmacophore model
* model_demo.py - create pharmacophore models from set of molecules

## Requirements ##
* numpy (for basic functionalities)

* Pybel (OpenBabel) and/or RDKit (for creating models from molecules)
* matplotlib (for pharmacophore drawing)
* scipy (for spring layout)


## Contact ##

Please contact us with comments, suggestions, questions or bug reports:

* Marta Stepniewska ( martasd[at]ibb.waw.pl )