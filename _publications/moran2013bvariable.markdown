---
layout: publication
title: "Variable Bit Quantisation for LSH"
authors: S. Moran, V. Lavrenko, and M. Osborne
conference: ACL
year: 2013
bibkey: moran2013bvariable
additional_links:
   - {name: "PDF", url: "http://homepages.inf.ed.ac.uk/miles/papers/acl13.pdf"}
   - {name: "Talk", url: "https://www.slideshare.net/sjmoran1/acl-variable-bit-quantisation-talk"}
---
We introduce a scheme for optimally allocating
a variable number of bits per
LSH hyperplane. Previous approaches assign
a constant number of bits per hyperplane.
This neglects the fact that a subset
of hyperplanes may be more informative
than others. Our method, dubbed Variable
Bit Quantisation (VBQ), provides a datadriven
non-uniform bit allocation across
hyperplanes. Despite only using a fraction
of the available hyperplanes, VBQ outperforms
uniform quantisation by up to 168%
for retrieval across standard text and image
datasets.
