---
layout: publication
title: "Locality-Sensitive Hashing for Earthquake Detection: A Case Study of Scaling Data-Driven Science"
authors: Kexin Rong, Clara E. Yoon, Karianne J. Bergen, Hashem Elezabi,Peter Bailis, Philip Levis, Gregory C. Beroza
conference: VLDB
year: 2018
bibkey: rong2018locality
additional_links:
   - {name: "PDF", url: "http://www.vldb.org/pvldb/vol11/p1674-rong.pdf"}
   - {name: "Tutorial", url: "https://dawn.cs.stanford.edu/2018/09/05/quake/"}
tags: ["LSH", "VLDB", "Case Study"]
---
In this work, we report on a novel application of Locality Sensitive
Hashing (LSH) to seismic data at scale. Based on the high waveform similarity between reoccurring earthquakes, our application
identifies potential earthquakes by searching for similar time series
segments via LSH. However, a straightforward implementation of
this LSH-enabled application has difficulty scaling beyond 3 months
of continuous time series data measured at a single seismic station.
As a case study of a data-driven science workflow, we illustrate how
domain knowledge can be incorporated into the workload to improve
both the efficiency and result quality. We describe several end-toend optimizations of the analysis pipeline from pre-processing to
post-processing, which allow the application to scale to time series data measured at multiple seismic stations. Our optimizations
enable an over 100× speedup in the end-to-end analysis pipeline.
This improved scalability enabled seismologists to perform seismic
analysis on more than ten years of continuous time series data from
over ten seismic stations, and has directly enabled the discovery of
597 new earthquakes near the Diablo Canyon nuclear power plant
in California and 6123 new earthquakes in New Zealand.
