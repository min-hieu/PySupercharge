# PySupercharge ⚡🧬
The supercharging library for bioinformatics.

Official Implementation of [Supercharge and Secretion](#) paper(Ahn et al.).
Official Web Implementation: [WebSupercharging](https://mb.re.kr/apps/supercharge)


## What is PySupercharge? - short introduction -
Decreasing electric charge by modifying amino acid sequence can improve the secretion ability of protein through bacterial ABC transporter system. PySupercharge replaces positive amino acids (Lys, Arg) that satisfy two conditions (AvNAPSA and consurf score) with negative amino acids (Glu, Asp) when the amino acid sequence has a high electric charge locally.
#### AvNAPSA score
The lower AvNAPSA score means fewer neighboring atoms and therefore less interaction. It ensures that the amino acid replacement will not make a significant change in the shape of the protein.An AvNAPSA cutoff of <150 has been widely used.
#### Consurf score
Consurf score identifies conserved regions of the polypeptide by tracing evolutionary history. Therefore it can determine whether the amino acid replacement causes functional problems of protein. A consurf score should be less or equal to 5 to be replaced.
***

## Requirements
Python Environment: 3.x. 
Python Package Dependency: install the `requirements.txt` file with
```
python -m pip install -r requirements.txt
```

## How to run
### Supercharge analysis
make sure that the requirements are met, and the PyAvNAPSA folder is inside the `python\Lib\site-packages`
Run the follow command in the directory to open GUI interface for the script
```
python superUI.py 
```
### PyMol plugins
1. install within pymol directory: `schrodinger\PyMol2\Lib\site-packages`
2. load the `Show_AvNAPSA_Script` on PyMol's plugin manager.
3. Choose pdb/pse model to be loaded.
4. Adjust threshold cut-off value (default: 80)
5. AvNAPSA selection is shown in red.

***
## Examples
### Supercharging
Inside the `example` folder, there is a pdb file and a consurf grade file for the 2013PEDV.
follow the steps to get the following result:
1. Import Consurf, sequence should be automatically added after choosing the file.
2. Import PDB, AvNAPSA value will be calculated in the terminal and might takes a while.
3. Adjust the threshold (in this case: 3)
4. Press `Supercharge` and `Export`.
5. The file should be in the same folder as the terminal current directory.
6. The exported result named `result.html` should looks like this.
<img src="https://github.com/YerinKim125/PySupercharge/blob/main/img/result.png" width="250">

## GUI helpful schematic

<img src="https://github.com/YerinKim125/PySupercharge/blob/main/img/label-window.png">

***
## Contributions
[Hieu](https://github.com/min-hieu) - superUI, AvNAPSA_class, PyMol plugin.

[Hyunjong Byun](https://github.com/bighungryjames) - AvNAPSA_class, AvNAPSA_dict.

[Yerin Kim](https://github.com/YerinKim125)