---
layout: default
title: Tutorial
comments: true
---
In this tutorial we explore a learning to hash model and compare its performance to Locality Sensitive Hashing (LSH). 

Specifically we will implement [Graph Regularised Hashing (GRH)](https://sjmoran.github.io/pdfs/grh_ecir15.pdf), a simple but effecitive model for learning to hash.

<pre>
@incollection{ 
year={2015}, 
isbn={978-3-319-16353-6}, 
booktitle={Advances in Information Retrieval}, 
volume={9022}, 
series={Lecture Notes in Computer Science}, 
editor={Hanbury, Allan and Kazai, Gabriella and Rauber, Andreas and Fuhr, Norbert}, 
doi={10.1007/978-3-319-16354-3_15}, 
title={Graph Regularised Hashing}, 
url={http://dx.doi.org/10.1007/978-3-319-16354-3_15}, 
publisher={Springer International Publishing}, author={Moran, Sean and Lavrenko, Victor}, pages={135-146}, 
language={English} }
</pre>

The original Matlab code supplied by the authors is [here](https://github.com/sjmoran/GRH). This tutorial will train the model on the CIFAR-10 dataset and benchmark retrieval effectiveness against LSH.

