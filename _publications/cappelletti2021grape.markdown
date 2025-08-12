---
layout: publication
title: GRAPE For Fast And Scalable Graph Processing And Random Walk-based Embedding
authors: Luca Cappelletti, Tommaso Fontana, Elena Casiraghi, Vida Ravanmehr, Tiffany
  J. Callahan, Carlos Cano, Marcin P. Joachimiak, Christopher J. Mungall, Peter N.
  Robinson, Justin Reese, Giorgio Valentini
conference: Nature Computational Science
year: 2023
bibkey: cappelletti2021grape
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.06196'}]
tags: []
short_authors: Cappelletti et al.
---
Graph Representation Learning (GRL) methods opened new avenues for addressing
complex, real-world problems represented by graphs. However, many graphs used
in these applications comprise millions of nodes and billions of edges and are
beyond the capabilities of current methods and software implementations. We
present GRAPE, a software resource for graph processing and embedding that can
scale with big graphs by using specialized and smart data structures,
algorithms, and a fast parallel implementation of random walk-based methods.
Compared with state-of-the-art software resources, GRAPE shows an improvement
of orders of magnitude in empirical space and time complexity, as well as a
competitive edge and node label prediction performance. GRAPE comprises about
1.7 million well-documented lines of Python and Rust code and provides 69 node
embedding methods, 25 inference models, a collection of efficient graph
processing utilities and over 80,000 graphs from the literature and other
sources. Standardized interfaces allow seamless integration of third-party
libraries, while ready-to-use and modular pipelines permit an easy-to-use
evaluation of GRL methods, therefore also positioning GRAPE as a software
resource to perform a fair comparison between methods and libraries for graph
processing and embedding.