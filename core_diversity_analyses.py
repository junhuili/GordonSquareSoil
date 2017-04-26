Last login: Sat Apr  8 16:38:55 on ttys000
eduroam-int-dhcp-97-185-138:~ michael$ source activate qiime1
(qiime1) eduroam-int-dhcp-97-185-138:~ michael$ cd desktop
(qiime1) eduroam-int-dhcp-97-185-138:bioc3301_data-master michael$ core_diversity_analyses.py -i/Users/michael/Desktop/Qiime/bioc3301_data-master/merged_otu_table.biom -m/Users/michael/Desktop/Qiime/bioc3301_data-master/2016/map/map.tsv_corrected.txt -t/Users/michael/Desktop/Qiime/bioc3301_data-master/2016/otus/97_otus.tree -e 371590 -o matrix.html
/Users/michael/miniconda2/envs/qiime1/lib/python2.7/site-packages/skbio/stats/ordination/_principal_coordinate_analysis.py:107: RuntimeWarning: The result contains negative eigenvalues. Please compare their magnitude with the magnitude of some of the largest positive eigenvalues. If the negative ones are smaller, it's probably safe to ignore them, but if they are large in magnitude, the results won't be useful. See the Notes section for more details. The smallest eigenvalue is -0.00137255347774 and the largest is 0.229249292233.
  RuntimeWarning
/Users/michael/miniconda2/envs/qiime1/lib/python2.7/site-packages/matplotlib/collections.py:590: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
  if self._edgecolors == str('face'):
/Users/michael/miniconda2/envs/qiime1/lib/python2.7/site-packages/matplotlib/collections.py:590: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
  if self._edgecolors == str('face'):
(qiime1) eduroam-int-dhcp-97-185-138:bioc3301_data-master michael$ 
