---
layout: publication
title: Similarity Search And Locality Sensitive Hashing Using Tcams
authors: Shinde Rajendra, Goel Ashish, Gupta Pankaj, Dutta Debojyoti
conference: "Arxiv"
year: 2010
bibkey: shinde2010similarity
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1006.3514"}
tags: ['ARXIV', 'Independent', 'LSH']
---
Similarity search methods are widely used as kernels in various machine learning applications. Nearest neighbor search (NNS) algorithms are often used to retrieve similar entries, given a query. While there exist efficient techniques for exact query lookup using hashing, similarity search using exact nearest neighbors is known to be a hard problem and in high dimensions, best known solutions offer little improvement over a linear scan. Fast solutions to the approximate NNS problem include Locality Sensitive Hashing (LSH) based techniques, which need storage polynomial in \\(n\\) with exponent greater than \\(1\\), and query time sublinear, but still polynomial in \\(n\\), where \\(n\\) is the size of the database. In this work we present a new technique of solving the approximate NNS problem in Euclidean space using a Ternary Content Addressable Memory (TCAM), which needs near linear space and has O(1) query time. In fact, this method also works around the best known lower bounds in the cell probe model for the query time using a data structure near linear in the size of the data base. TCAMs are high performance associative memories widely used in networking applications such as access control lists. A TCAM can query for a bit vector within a database of ternary vectors, where every bit position represents \\(0\\), \\(1\\) or \\(*\\). The \\(*\\) is a wild card representing either a \\(0\\) or a \\(1\\). We leverage TCAMs to design a variant of LSH, called Ternary Locality Sensitive Hashing (TLSH) wherein we hash database entries represented by vectors in the Euclidean space into \\(\\{0,1,*\\}\\). By using the added functionality of a TLSH scheme with respect to the \\(*\\) character, we solve an instance of the approximate nearest neighbor problem with 1 TCAM access and storage nearly linear in the size of the database. We believe that this work can open new avenues in very high speed data mining.
