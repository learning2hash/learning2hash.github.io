---
    layout: publication
    title: "Lucene for Approximate Nearest-Neighbors Search on Arbitrary Dense Vectors"
    authors: Teofili Tommaso, Lin Jimmy
    conference: Arxiv
    year: 2019
    bibkey: teofili2019lucene
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1910.10208"}
    tags: ['Arxiv', 'Deep Learning', 'LSH', 'Case Study']
    ---
    {% raw %}
    We demonstrate three approaches for adapting the open-source Lucene search library to perform approximate nearest-neighbor search on arbitrary dense vectors, using similarity search on word embeddings as a case study. At its core, Lucene is built around inverted indexes of a document collection's (sparse) term-document matrix, which is incompatible with the lower-dimensional dense vectors that are common in deep learning applications. We evaluate three techniques to overcome these challenges that can all be natively integrated into Lucene: the creation of documents populated with fake words, LSH applied to lexical realizations of dense vectors, and k-d trees coupled with dimensionality reduction. Experiments show that the "fake words" approach represents the best balance between effectiveness and efficiency. These techniques are integrated into the Anserini open-source toolkit and made available to the community.
    {% endraw %}