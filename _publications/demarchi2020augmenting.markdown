---
layout: publication
title: Augmenting Molecular Images With Vector Representations As A Featurization
  Technique For Drug Classification
authors: Daniel de Marchi, Amarjit Budhiraja
conference: ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2020
bibkey: demarchi2020augmenting
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.03646'}]
tags: ["ICASSP"]
short_authors: Daniel de Marchi, Amarjit Budhiraja
---
One of the key steps in building deep learning systems for drug
classification and generation is the choice of featurization for the molecules.
Previous featurization methods have included molecular images, binary strings,
graphs, and SMILES strings. This paper proposes the creation of molecular
images captioned with binary vectors that encode information not contained in
or easily understood from a molecular image alone. Specifically, we use Morgan
fingerprints, which encode higher level structural information, and MACCS keys,
which encode yes or no questions about a molecules properties and structure. We
tested our method on the HIV dataset published by the Pande lab, which consists
of 41,127 molecules labeled by if they inhibit the HIV virus. Our final model
achieved a state of the art AUC ROC on the HIV dataset, outperforming all other
methods. Moreover, the model converged significantly faster than most other
methods, requiring dramatically less computational power than unaugmented
images.