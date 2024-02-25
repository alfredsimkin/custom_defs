from ete2 import Tree
#t=Tree('100way_mod.nh', format=1)

def get_dist(t, species_list):
	'''
	this module takes a phylogenetic tree (t) with branch lengths and internal
	nodes, along with a list of species of interest (species_list), and reports
	the total branch length to the common ancestor of the species of interest
	'''
	from decimal import Decimal
	t=Tree(t, format=1)
	ancestor=t.get_common_ancestor(species_list)
	branch_set=set([])
	total_dist=Decimal('0')
	for species in species_list:
		branch=t.search_nodes(name=species)[0]
		while branch!=ancestor:
			branch_set.add(branch)
			branch=branch.up
	for branch in branch_set:
		total_dist+=Decimal(branch.dist)
	return total_dist

def prune_species(t, good_species, outname):
	'''
	prunes an input phylogenetic tree (t) to only contain good_species, and
	sends the result out to a newick file named 'outname'
	'''
	t=Tree(t, format=1)
	t.prune(good_species, preserve_branch_length=True)
	t.write(format=1, outfile=outname)
