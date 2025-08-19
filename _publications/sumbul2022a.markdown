---
layout: publication
title: A Novel Framework To Jointly Compress And Index Remote Sensing Images For Efficient
  Content-based Retrieval
authors: "Gencer Sumbul, Jun Xiang, Nimisha Thekke Madam, Beg\xFCm Demir"
conference: IGARSS 2022 - 2022 IEEE International Geoscience and Remote Sensing Symposium
year: 2022
bibkey: sumbul2022a
citations: 1
additional_links: [{name: Code, url: 'https://git.tu-berlin.de/rsim/RS-JCIF.'}, {
    name: Paper, url: 'https://arxiv.org/abs/2201.06459'}]
tags: [RSS, Hashing Methods, Image Retrieval, Tools & Libraries, Scalability]
short_authors: Sumbul et al.
---
Remote sensing (RS) images are usually stored in compressed format to reduce
the storage size of the archives. Thus, existing content-based image retrieval
(CBIR) systems in RS require decoding images before applying CBIR (which is
computationally demanding in the case of large-scale CBIR problems). To address
this problem, in this paper, we present a joint framework that simultaneously
learns RS image compression and indexing. Thus, it eliminates the need for
decoding RS images before applying CBIR. The proposed framework is made up of
two modules. The first module compresses RS images based on an auto-encoder
architecture. The second module produces hash codes with a high discrimination
capability by employing soft pairwise, bit-balancing and classification loss
functions. We also introduce a two stage learning strategy with gradient
manipulation techniques to obtain image representations that are compatible
with both RS image indexing and compression. Experimental results show the
efficacy of the proposed framework when compared to widely used approaches in
RS. The code of the proposed framework is available at
https://git.tu-berlin.de/rsim/RS-JCIF.