# PySupercharge ⚡🧬
The supercharging library for bioinformatics.

Official Implementation of [Supercharge and Secretion](#) paper(Ahn et al.).

##


## Requirements
Python Environment: 3.x
Python Package Dependency: install the `requirements.txt` file with
```
python -m pip install -r requirements.txt
```

## How to run
### LCD analysis
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

## Examples
to be added

## Contributions
[Hieu](https://github.com/min-hieu) - superUI, AvNAPSA_class, PyMol plugin.

[Hyunjong Byun](https://github.com/bighungryjames) - AvNAPSA_class, AvNAPSA_dict.
