---
    layout: publication
    title: "Scalable Protein Sequence Similarity Search using Locality-Sensitive Hashing and MapReduce"
    authors: Sunarso Freddie, Venugopal Srikumar, Lauro Federico
    conference: Arxiv
    year: 2013
    bibkey: sunarso2013scalable
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/1310.0883"}
    tags: ['ARXIV', 'LSH']
    ---
    Metagenomics is the study of environments through genetic sampling of their microbiota. Metagenomic studies produce large datasets that are estimated to grow at a faster rate than the available computational capacity. A key step in the study of metagenome data is sequence similarity searching which is computationally intensive over large datasets. Tools such as BLAST require large dedicated computing infrastructure to perform such analysis and may not be available to every researcher. In this paper, we propose a novel approach called ScalLoPS that performs searching on protein sequence datasets using LSH (Locality-Sensitive Hashing) that is implemented using the MapReduce distributed framework. ScalLoPS is designed to scale across computing resources sourced from cloud computing providers. We present the design and implementation of ScalLoPS followed by evaluation with datasets derived from both traditional as well as metagenomic studies. Our experiments show that with this method approximates the quality of BLAST results while improving the scalability of protein sequence search.