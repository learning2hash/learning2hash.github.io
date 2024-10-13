---
layout: publication
title: Distributed Stratified Locality Sensitive Hashing For Critical Event Prediction In The Cloud
authors: De Palma Alessandro, Hemberg Erik, O'reilly Una-may
conference: "Arxiv"
year: 2017
bibkey: depalma2017distributed
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1712.00206"}
tags: ['ARXIV']
---
<p>The availability of massive healthcare data repositories calls for
efficient tools for data-driven medicine. We introduce a distributed
system for Stratified Locality Sensitive Hashing to perform fast
similarity-based prediction on large medical waveform datasets. Our
implementation, for an ICU use case, prioritizes latency over throughput
and is targeted at a cloud environment. We demonstrate our system on
Acute Hypotensive Episode prediction from Arterial Blood Pressure
waveforms. On a dataset of <span class="math inline">\(1.37\)</span>
million points, we show scaling up to <span
class="math inline">\(40\)</span> processors and a <span
class="math inline">\(21\times\)</span> speedup in number of comparisons
to parallel exhaustive search at the price of a <span
class="math inline">\(10\%\)</span> Matthews correlation coefficient
(MCC) loss. Furthermore, if additional MCC loss can be tolerated, our
system achieves speedups up to two orders of magnitude.</p>
