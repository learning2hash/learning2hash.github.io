---
layout: publication
title: Automatic Search Of Multiword Place Names On Historical Maps
authors: Rhett Olson, Jina Kim, Yao-Yi Chiang
conference: Proceedings of the 3rd ACM SIGSPATIAL International Workshop on Searching
  and Mining Large Collections of Geospatial Data
year: 2024
bibkey: olson2024automatic
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.15586'}]
tags: ["SIGIR", "Text Retrieval"]
short_authors: Rhett Olson, Jina Kim, Yao-Yi Chiang
---
Historical maps are invaluable sources of information about the past, and
scanned historical maps are increasingly accessible in online libraries. To
retrieve maps from these large libraries that contain specific places of
interest, previous work has applied computer vision techniques to recognize
words on historical maps, enabling searches for maps that contain specific
place names. However, searching for multiword place names is challenging due to
complex layouts of text labels on historical maps. This paper proposes an
efficient query method for searching a given multiword place name on historical
maps. Using existing methods to recognize words on historical maps, we link
single-word text labels into potential multiword phrases by constructing
minimum spanning trees. These trees aim to link pairs of text labels that are
spatially close and have similar height, angle, and capitalization. We then
query these trees for the given multiword place name. We evaluate the proposed
method in two experiments: 1) to evaluate the accuracy of the minimum spanning
tree approach at linking multiword place names and 2) to evaluate the number
and time range of maps retrieved by the query approach. The resulting maps
reveal how places using multiword names have changed on a large number of maps
from across history.