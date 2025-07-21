---
layout: publication
title: Spherical Hashing
authors: Heo et al.
conference: 2012 IEEE Conference on Computer Vision and Pattern Recognition
year: 2012
bibkey: heo2025spherical
citations: 380
additional_links: [{name: Paper, url: 'http://www.ee.columbia.edu/ln/dvmm/pubs/files/Spherical_Hashing.pdf'}]
tags: ["Hashing-Methods", "CVPR"]
---
Many binary code encoding schemes based on hashing
have been actively studied recently, since they can provide
efficient similarity search, especially nearest neighbor
search, and compact data representations suitable for handling
large scale image databases in many computer vision
problems. Existing hashing techniques encode highdimensional
data points by using hyperplane-based hashing
functions. In this paper we propose a novel hyperspherebased
hashing function, spherical hashing, to map more
spatially coherent data points into a binary code compared
to hyperplane-based hashing functions. Furthermore, we
propose a new binary code distance function, spherical
Hamming distance, that is tailored to our hyperspherebased
binary coding scheme, and design an efficient iterative
optimization process to achieve balanced partitioning
of data points for each hash function and independence between
hashing functions. Our extensive experiments show
that our spherical hashing technique significantly outperforms
six state-of-the-art hashing techniques based on hyperplanes
across various image benchmarks of sizes ranging
from one to 75 million of GIST descriptors. The performance
gains are consistent and large, up to 100% improvements.
The excellent results confirm the unique merits of
the proposed idea in using hyperspheres to encode proximity
regions in high-dimensional spaces. Finally, our method
is intuitive and easy to implement.