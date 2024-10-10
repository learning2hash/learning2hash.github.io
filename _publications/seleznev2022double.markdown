---
layout: publication
title: Double-hashing Algorithm For Frequency Estimation In Data Streams
authors: Seleznev Nikita, Kumar Senthil, Bruss C. Bayan
conference: "Arxiv"
year: 2022
bibkey: seleznev2022double
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2204.00650"}
tags: ['ARXIV']
---
Frequency estimation of elements is an important task for summarizing data streams and machine learning applications. The problem is often addressed by using streaming algorithms with sublinear space data structures. These algorithms allow processing of large data while using limited data storage. Commonly used streaming algorithms such as count-min sketch have many advantages but do not take into account properties of a data stream for performance optimization. In the present paper we introduce a novel double-hashing algorithm that provides flexibility to optimize streaming algorithms depending on the properties of a given stream. In the double-hashing approach first a standard streaming algorithm is employed to obtain an estimate of the element frequencies. This estimate is derived using a fraction of the stream and allows identification of the heavy hitters. Next it uses a modified hash table where the heavy hitters are mapped into individual buckets and other stream elements are mapped into the remaining buckets. Finally the element frequencies are estimated based on the constructed hash table over the entire data stream with any streaming algorithm. We demonstrate on both synthetic data and an internet query log dataset that our approach is capable of improving frequency estimation due to removing heavy hitters from the hashing process and thus reducing collisions in the hash table. Our approach avoids employing additional machine learning models to identify heavy hitters and thus reduces algorithm complexity and streamlines implementation. Moreover because it is not dependent on specific features of the stream elements for identifying heavy hitters it is applicable to a large variety of streams. In addition we propose a procedure on how to dynamically adjust the proposed double-hashing algorithm when frequencies of the elements in a stream are changing over time.
