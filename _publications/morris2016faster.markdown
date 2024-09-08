---
    layout: publication
    title: "Faster Kernels for Graphs with Continuous Attributes via Hashing"
    authors: Morris Christopher, Kriege Nils M., Kersting Kristian, Mutzel Petra
    conference: Arxiv
    year: 2016
    bibkey: morris2016faster
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1610.00064"}
    tags: ['Graph', 'Arxiv']
    ---
    While state-of-the-art kernels for graphs with discrete labels scale well to graphs with thousands of nodes, the few existing kernels for graphs with continuous attributes, unfortunately, do not scale well. To overcome this limitation, we present hash graph kernels, a general framework to derive kernels for graphs with continuous attributes from discrete ones. The idea is to iteratively turn continuous attributes into discrete labels using randomized hash functions. We illustrate hash graph kernels for the Weisfeiler-Lehman subtree kernel and for the shortest-path kernel. The resulting novel graph kernels are shown to be, both, able to handle graphs with continuous attributes and scalable to large graphs and data sets. This is supported by our theoretical analysis and demonstrated by an extensive experimental evaluation.