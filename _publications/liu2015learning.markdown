---
layout: publication
title: Learning Better Encoding For Approximate Nearest Neighbor Search With Dictionary Annealing
authors: Liu Shicong, Lu Hongtao
conference: "Arxiv"
year: 2015
bibkey: liu2015learning
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1507.01442"}
tags: ['ARXIV', 'Independent', 'Quantisation']
---
<p>We introduce a novel dictionary optimization method for
high-dimensional vector quantization employed in approximate nearest
neighbor (ANN) search. Vector quantization methods first seek a series
of dictionaries, then approximate each vector by a sum of elements
selected from these dictionaries. An optimal series of dictionaries
should be mutually independent, and each dictionary should generate a
balanced encoding for the target dataset. Existing methods did not
explicitly consider this. To achieve these goals along with minimizing
the quantization error (residue), we propose a novel dictionary
optimization method called that alternatively “heats up” a single
dictionary by generating an intermediate dataset with residual vectors,
“cools down” the dictionary by fitting the intermediate dataset, then
extracts the new residual vectors for the next iteration. Better codes
can be learned by DA for the ANN search tasks. DA is easily implemented
on GPU to utilize the latest computing technology, and can easily
extended to an online dictionary learning scheme. We show by experiments
that our optimized dictionaries substantially reduce the overall
quantization error. Jointly used with residual vector quantization, our
optimized dictionaries lead to a better approximate nearest neighbor
search performance compared to the state-of-the-art methods.</p>
