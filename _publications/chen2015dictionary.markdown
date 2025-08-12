---
layout: publication
title: A Dictionary Approach To EBSD Indexing
authors: Yu-Hui Chen, Se Un Park, Dennis Wei, Gregory Newstadt, Michael Jackson, Jeff
  P. Simmons, Marc de Graef, Alfred O. Hero
conference: Arxiv
year: 2015
bibkey: chen2015dictionary
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1502.07436'}]
tags: []
short_authors: Chen et al.
---
We propose a framework for indexing of grain and sub-grain structures in
electron backscatter diffraction (EBSD) images of polycrystalline materials.
The framework is based on a previously introduced physics-based forward model
by Callahan and De Graef (2013) relating measured patterns to grain
orientations (Euler angle). The forward model is tuned to the microscope and
the sample symmetry group. We discretize the domain of the forward model onto a
dense grid of Euler angles and for each measured pattern we identify the most
similar patterns in the dictionary. These patterns are used to identify
boundaries, detect anomalies, and index crystal orientations. The statistical
distribution of these closest matches is used in an unsupervised binary
decision tree (DT) classifier to identify grain boundaries and anomalous
regions. The DT classifies a pattern as an anomaly if it has an abnormally low
similarity to any pattern in the dictionary. It classifies a pixel as being
near a grain boundary if the highly ranked patterns in the dictionary differ
significantly over the pixels 3x3 neighborhood. Indexing is accomplished by
computing the mean orientation of the closest dictionary matches to each
pattern. The mean orientation is estimated using a maximum likelihood approach
that models the orientation distribution as a mixture of Von Mises-Fisher
distributions over the quaternionic 3-sphere. The proposed dictionary matching
approach permits segmentation, anomaly detection, and indexing to be performed
in a unified manner with the additional benefit of uncertainty quantification.
We demonstrate the proposed dictionary-based approach on a Ni-base IN100 alloy.