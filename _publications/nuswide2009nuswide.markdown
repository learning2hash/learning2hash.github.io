---
layout: publication
title: "NUS-WIDE: a real-world web image database from National University of Singapore"
authors: T. Chua, J. Tang, R. Hong, H. Li, Z. Luo, Y. Zheng
conference: CIVR
year: 2009
bibkey: nuswide2009nuswide
additional_links:
   - {name: "URL", url: "ftp://vista.eng.tau.ac.il/dropbox/Litman/NUS-WIDE%20Homepage/NUS-WIDE%20Homepage.html"}
   - {name: "Features", url: "https://www.dropbox.com/s/4ds9f56xqs29a2z/nus_data.mat?dl=0"}
   - {name: "Tags", url: "https://www.dropbox.com/s/bwryqsqyev8waen/nus_gt.mat?dl=0"}
   - {name: "Tags (PCA projected)", url: "https://www.dropbox.com/s/18a9i6fadis6bj5/nus_tags_pca.mat?dl=0"}
---
This paper introduces a web image dataset created by NUS's Lab for Media Search. The dataset includes: (1) 269,648 images and the associated tags from Flickr, with a total of 5,018 unique tags; (2) six types of low-level features extracted from these images, including 64-D color histogram, 144-D color correlogram, 73-D edge direction histogram, 128-D wavelet texture, 225-D block-wise color moments extracted over 5x5 fixed grid partitions, and 500-D bag of words based on SIFT descriptions; and (3) ground-truth for 81 concepts that can be used for evaluation. Based on this dataset, we highlight characteristics of Web image collections and identify four research issues on web image annotation and retrieval. We also provide the baseline results for web image annotation by learning from the tags using the traditional k-NN algorithm. The benchmark results indicate that it is possible to learn effective models from sufficiently large image dataset to facilitate general image retrieval.
