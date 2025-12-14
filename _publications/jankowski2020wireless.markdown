---
layout: publication
title: Wireless Image Retrieval At The Edge
authors: Mikolaj Jankowski, Deniz Gunduz, Krystian Mikolajczyk
conference: IEEE Journal on Selected Areas in Communications
year: 2020
bibkey: jankowski2020wireless
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.10915'}]
tags: [Image Retrieval, Datasets]
short_authors: Mikolaj Jankowski, Deniz Gunduz, Krystian Mikolajczyk
---
We study the image retrieval problem at the wireless edge, where an edge
device captures an image, which is then used to retrieve similar images from an
edge server. These can be images of the same person or a vehicle taken from
other cameras at different times and locations. Our goal is to maximize the
accuracy of the retrieval task under power and bandwidth constraints over the
wireless link. Due to the stringent delay constraint of the underlying
application, sending the whole image at a sufficient quality is not possible.
We propose two alternative schemes based on digital and analog communications,
respectively. In the digital approach, we first propose a deep neural network
(DNN) aided retrieval-oriented image compression scheme, whose output bit
sequence is transmitted over the channel using conventional channel codes. In
the analog joint source and channel coding (JSCC) approach, the feature vectors
are directly mapped into channel symbols. We evaluate both schemes on image
based re-identification (re-ID) tasks under different channel conditions,
including both static and fading channels. We show that the JSCC scheme
significantly increases the end-to-end accuracy, speeds up the encoding
process, and provides graceful degradation with channel conditions. The
proposed architecture is evaluated through extensive simulations on different
datasets and channel conditions, as well as through ablation studies.