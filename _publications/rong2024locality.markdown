---
layout: publication
title: Locality-sensitive Hashing For Earthquake Detection A Case Study Of Scaling Data-driven Science
authors: Rong Kexin, Yoon, Bergen, Elezabi, Bailis Peter, Levis, Beroza
conference: "Arxiv"
year: 2024
bibkey: rong2024locality
additional_links:
  - {name: "Paper", url: "http://www.vldb.org/pvldb/vol11/p1674-rong.pdf"}
tags: ['ARXIV', 'Case Study', 'Independent', 'LSH']
---
In this work we report on a novel application of Locality Sensitive Hashing (LSH) to seismic data at scale. Based on the high waveform similarity between reoccurring earthquakes our application identifies potential earthquakes by searching for similar time series segments via LSH. However a straightforward implementation of this LSH-enabled application has difficulty scaling beyond 3 months of continuous time series data measured at a single seismic station. As a case study of a data-driven science workflow we illustrate how domain knowledge can be incorporated into the workload to improve both the efficiency and result quality. We describe several end-toend optimizations of the analysis pipeline from pre-processing to post-processing which allow the application to scale to time series data measured at multiple seismic stations. Our optimizations enable an over 100× speedup in the end-to-end analysis pipeline. This improved scalability enabled seismologists to perform seismic analysis on more than ten years of continuous time series data from over ten seismic stations and has directly enabled the discovery of 597 new earthquakes near the Diablo Canyon nuclear power plant in California and 6123 new earthquakes in New Zealand.
