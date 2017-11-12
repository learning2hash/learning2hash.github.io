---
layout: publication
title: "Discrete Graph Hashing"
authors: W. Liu, C. Mu, S. Kumar, S. Chang
conference: NIPS
year: 2014
bibkey: liu2014discrete
additional_links:
   - {name: "PDF", url: "http://www.ee.columbia.edu/~wliu/NIPS14_dgh.pdf"}
   - {name: "Talk", url: "http://www.ee.columbia.edu/~wliu/NIPS14_dgh_slides.pdf"}
---
Hashing has emerged as a popular technique for fast nearest neighbor search in gigantic
databases. In particular, learning based hashing has received considerable
attention due to its appealing storage and search efficiency. However, the performance
of most unsupervised learning based hashing methods deteriorates rapidly
as the hash code length increases. We argue that the degraded performance is due
to inferior optimization procedures used to achieve discrete binary codes. This
paper presents a graph-based unsupervised hashing model to preserve the neighborhood
structure of massive data in a discrete code space. We cast the graph
hashing problem into a discrete optimization framework which directly learns the
binary codes. A tractable alternating maximization algorithm is then proposed to
explicitly deal with the discrete constraints, yielding high-quality codes to well
capture the local neighborhoods. Extensive experiments performed on four large
datasets with up to one million samples show that our discrete optimization based
graph hashing method obtains superior search accuracy over state-of-the-art unsupervised
hashing methods, especially for longer codes.
