#So this is the AvNAPSA, originally from the Liu group, written in Perl.
#This version is a translation into python.
#Author: Hyunjong Byun
#This document has translations by Hyunjong Byun only.
#This document implements AvNAPSA calculations based on the dictionary-approach.
#Not very object-oriented.

from math import sqrt
residues = []
DISTANCE_CUTOFF = 10

#def tabulate_residues (atoms): #atoms is a list with PDB atoms.
    #for atom in atoms:
        #resNum = atom['resNum']
        #if not resNum_exists(resNum):
            ##I think Hieu's right. So residues is a global list of list of dictionaries {'resNum':str(int), 'resName':str}
            #global residues 
            #resName = atom['resName']
            #residues.append({'resNum':resNum, 'resName':atom['resName']})

##
## tabulate_residues
##
## goes through list of atoms and makes a list of amino acid residues
## and stores it in global variable @residues
##

#sub tabulate_residues
#{
#for ($a = 0; $a < @atoms; $a++)
#{
#$resNum = $atoms[$a]{resNum};
#if ( ! resNum_exists($resNum) )
#{
#push @residues,
#{
#resNum => $resNum,
#resName => $atoms[$a]{resName}
#};
#}
#}
#}



def resNum_exists(residues, resNum):
    residues
    for residue in residues:
        if residue[0]['resNum'] == resNum:
            return True
    return False

##
## resNum_exists
##
## returns 1 if resNum is contained in @residues
##

#sub resNum_exists($)
#{
#my ($resNum) = @_;
#for ($r = 0; $r < @residues; $r++)
#{
#return 1 if ($residues[$r]{resNum} == $resNum);
#}
#return 0;
#}



def resNum_to_resIndex(residues, resNum):
    residues
    for i, residue in enumerate(residues):
        if residue[0]['resNum'] == resNum:
            return i
    return -1

##
## resNum_to_resindex
##
## converts PDB numbering to index in @residues
##
#sub resNum_to_resindex($)
#{
#my ($resNum) = @_;
#for ($r = 0; $r < @residues; $r++)
#{
#return $r if ($residues[$r]{resNum} == $resNum);
#}
#return "none";
#}


#PDB ATOM lines structure:
#Actually, PDB is very old type and therefore has strict number of characters designated to each column
#char 0-5            12-15      17-19
#Signifier  atomNum  atomName   resName ChainName  resNum    x       y       z       1.00  0.70      atomType
#ATOM       1        N          THR     A          12        -4.777  -6.979  -3.511  1.00  0.70      N
#ATOM       2        CA         THR     A          12        -5.738  -6.248  -2.633  1.00  0.70      C

def readPDB(filename='./input.pdb'):
#resName = ''
#resNum = -1
#atomName = ''
#atomNum = -1
#chain = ''
#field = '' 
##in the original code, "type". but type is a built-in function in python, so I had to avoid.
    atoms = []
    try:
        f = open(filename, 'r')
    except RuntimeError:
        print('Could not open {}\n'.format(filename))
        return atoms
    
    while True:
        line = f.readline()
        if not line:
            break
        
        field = line[0:6].strip().upper()
        if not field in ('ATOM', 'HETATM'): # RTyp field is columns 1-6
            continue
        
        resName = line[17:20].strip().upper() # Res field is columns 18-20
        if resName == 'HOH':
            continue
        
        atomName = line[12:16].strip().upper() # Atm field is columns 13-16
        if atomName[-1] == 'H' and atomName[:-1].isdecimal():
            continue
        
        atomNum = int(line[6:11].strip()) # Num field is columns 7-11
        chain = line[21:22].strip() # Chain field is column 22
        resNum = int(line[22:26].strip()) # ResNo field is columns 23-26
        x = float(line[30:38].strip()) # X field is columns 31-38
        y = float(line[38:46].strip()) # Y field is columns 39-46
        z = float(line[46:54].strip()) # Z field is columns 37-54
        
        atom = {}
        atom['field'] = field
        atom['atomNum'] = atomNum
        atom['atomName'] = atomName
        atom['resName'] = resName
        atom['chain'] = chain
        atom['resNum'] = resNum
        atom['x'] = x
        atom['y'] = y
        atom['z'] = z
        atom['neighborCount'] = 0
        
        atoms.append(atom)
    f.close()
    return atoms

##
## readPDB(filename)
##
## reads the atoms from a PDB and returns them as an array of hashes
##
#sub read_PDB($)
#{
#my ($filename) = @_;
#open (PDB, $filename) or die("Could not open $filename\n");
#$#atoms = -1; # clear atoms storage
#
## read the file
#
#foreach (<PDB>) {
#my $type = trim(substr($_, 0,6)); # RTyp field is columns 1-6
#next unless ($type eq "ATOM" || $type eq "HETATM");
#
#my $resName = trim(substr($_, 17, 3)); # Res field is columns 18-20
#my $atomName = trim(substr($_, 12, 4)); # Atm field is columns 13-16
#
#next if uc $resName eq "HOH"; # omit waters
#next if uc $atomName =~ /^[0-9]*H/; # omit protons
#
## add a hash to the array, containing data from this record of the PDB
#
#push @atoms, {
#type => $type,
#resName => $resName,
#atomName => $atomName,
#atomNum => trim(substr($_, 6,5)), # Num field is columns 7-11
#chain => trim(substr($_, 21,1)), # Chain field is column 22
#resNum => trim(substr($_, 22,4)), # ResNo field is columns 23-26
#x => trim(substr($_, 30,8)), # X field is columns 31-38
#y => trim(substr($_, 38,8)), # Y field is columns 39-46
#z => trim(substr($_, 46,8)) # Z field is columns 37-54
#};
#}
#close(PDB);
#}



#This method is newly created, since residues[] and atoms[] are two different things in this script, unlike the original one.
def residues_from_atoms(atoms):
    residues = []
    residue = []
    this_resNum = atoms[0]['resNum']
    for atom in atoms:
        if atom['resNum'] == this_resNum:
            residue.append(atom)
            continue
        else:
            residues.append(residue)
            this_resNum = atom['resNum']
            residue = [atom]
    residues.append(residue)
    return residues



#since the original version of is_numbers in Perl was mediocre, I created one myself.
#It is now much more strict.
#"Robust... Precise... AR-15."

def is_number(s):
    s = s.strip()
    if s[0] == '-':
        s = s[1:] #allows negative
    has_decimal = False  #allows single decimal point
    for char in s:
        if not char.isdecimal():
            if char.isspace():
                continue
            elif char == '.':
                if has_decimal:
                    return False
                else:
                    has_decimal = True
                    continue
            else:
                return False
    return True

##
## is_number
##
## returns 1 if passed argument is a number (allows whitespace, negative, and decimal point)
## returns 0 if passed argument is blank or not a number
##
#sub is_number($)
#{
#$_ = shift;
#s/^\s+//;
#s/\s+$//;
#return 1 if /^-?[0-9]+$/ || /^-?[0-9]*\.[0-9]+$/ || /^-?[0-9]+\.[0-9]*$/;
#return 0;
#}



def inter_residue_distance(residues, res1, res2):
    resNum1 = residues[res1][0]['resNum']
    resNum2 = residues[res2][0]['resNum']
    min_distance = 1000000
    for atom1 in residues[res1]:
        for atom2 in residues[res2]:
            this_distance = compute_distance(atom1, atom2)
            if this_distance < min_distance:
                min_distance = this_distance
    return min_distance

##
## inter_residue_distance
##
## returns the minimum distance between any atoms of the specified residues
## (residues are specified according to index in @residues)
##
#sub inter_residue_distance($, $)
#{
#my ($r1, $r2) = @_;
### convert to PDB numbering
#my $resNum1 = $residues[$r1]{resNum};
#my $resNum2 = $residues[$r2]{resNum};
#my $min_dist = 1000000;
#for ($a1 = 0; $a1 < @atoms; ++$a1)
#{
#next unless ( $atoms[$a1]{resNum} == $resNum1 );
#for ($a2 = 0; $a2 < @atoms; ++$a2)
#{
#next unless ( $atoms[$a2]{resNum} == $resNum2 );
#my $dist = compute_distance($a1,$a2);
#$min_dist = $dist if ($dist < $min_dist);
#}
#}
#return $min_dist;
#}



def compute_distance(atom1, atom2):
    x1, y1, z1 = atom1['x'], atom1['y'], atom1['z']
    x2, y2, z2 = atom2['x'], atom2['y'], atom2['z']
    distance = sqrt( (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2 )
    return distance

##
## compute_distance
##
## computes the distances between a given pair of atoms
##
#sub compute_distance
#{
#my ($atom1, $atom2) = @_;
#my ($x1,$y1,$z1) = ($atoms[$atom1]->{x}, $atoms[$atom1]->{y}, $atoms[$atom1]->{z});
#my ($x2,$y2,$z2) = ($atoms[$atom2]->{x}, $atoms[$atom2]->{y}, $atoms[$atom2]->{z});
#my $distance = sqrt(($x1-$x2)**2 + ($y1-$y2)**2 + ($z1-$z2)**2);
#return $distance;
#}


#The original function in Perl was stupid and was accessing each calculations twice.
#In here, each calculation is only accessed once.
def compute_neighbor_counts(atoms, cutoff = DISTANCE_CUTOFF): #waring: O(n^2) function!
    length = len(atoms)
    counter = 0
    for i in range(length):
        for j in range(i+1, length):
            if compute_distance(atoms[i], atoms[j]) <= cutoff:
                atoms[i]['neighborCount'] += 1
                atoms[j]['neighborCount'] += 1

##
## compute_neighbor_counts
##
## computes the number of neighbors that each atom has.
## paramter is the cutoff, in Angstroms, for atomic neighborhood
##
#sub compute_neighbor_counts
#{
#$DISTANCE_CUTOFF = 10; # criterion for neighborhood, in Angstroms
#my $n_atoms = @atoms;
#my $prog = 0;
#$| = 1;
#print "Progress: ";
#for ($atom1=0; $atom1 < $n_atoms; $atom1++)
#{
#my $new_prog = int(100 * $atom1 / $n_atoms);
#if ($new_prog-$prog) {
#print $new_prog . "% ";
#$prog = $new_prog;
#}
#my $count = 0;
#for ($atom2=0; $atom2 < $n_atoms; $atom2++)
#{
#$count++ if (compute_distance($atom1,$atom2) <= $DISTANCE_CUTOFF
#&& $atom1 != $atom2);
#}
#$atoms[$atom1]{neighborCount} = $count;
#}
#print "Done.\n";
#}


#returns a list of int which same length if residues[].
def compute_residue_AvNAPSA(residues): 
    AvNAPSAs = []
    for residue in residues:
        sum_neighborCount = 0
        num_sidechain = 0
        for atom in residue:
            if (not atom['atomName'] in ('C', 'O', 'N', 'CA'))\
               or (atom['atomName'] == 'CA' and atom['resName'] == 'GLY'):
                num_sidechain += 1
                sum_neighborCount += atom['neighborCount']
        try:
            AvNAPSA = float(sum_neighborCount) / num_sidechain
        except ZeroDivisionError:
            AvNAPSA = 10000.0
        AvNAPSAs.append(AvNAPSA)
    return AvNAPSAs

## compute_residue_avNapsa
##
## for each residue, compute
## Average Neighbor Atoms Per Sidechain Atom (AvNAPSA)
## (sidechain atoms are all those except N, C, O, CA)
## for glycines, just use CA
##
#sub compute_residue_avNapsa
#{
#for (my $r = 0; $r < @residues; $r++)
#{
#my $numSideChainAtoms = 0;
#my $totalNeighbors = 0;
#my $resName = $residues[$r]{resName};
#my $resNum = $residues[$r]{resNum};
#for (my $a = 0; $a < @atoms; $a++)
#{
#if ($atoms[$a]{resNum} == $resNum)
#{
#my $atomName = $atoms[$a]{atomName};
#if (
#( $atomName ne "C"
#&& $atomName ne "O"
#&& $atomName ne "N"
#&& $atomName ne "CA"
#)
#|| ( $atomName eq "CA" && $resName eq "GLY")
#)
#{
#$numSideChainAtoms++;
#$totalNeighbors += $atoms[$a]{neighborCount};
#}
#}
#}
#my $avNapsa = 0;
#$avNapsa = $totalNeighbors / $numSideChainAtoms unless !$numSideChainAtoms;
#$residues[$r]{avNapsa} = $avNapsa;
#}
#}



def _main():
    atoms = readPDB(filename='./input.pdb')
    residues = residues_from_atoms(atoms)
    compute_neighbor_counts(atoms)
    AvNAPSAs = compute_residue_AvNAPSA(residues)
    print(AvNAPSAs)
    return AvNAPSAs


if __name__ == '__main__':
    _main()