---
layout: publication
title: "Learning Hash Functions Using Column Generation"
authors: X. Li, G. Lin, C. Shen, A. Hengel, A. Dick
conference: ICML
year: 2013
bibkey: li2013column
additional_links:
   - {name: "PDF", url: "http://www.jmlr.org/proceedings/papers/v28/li13a.pdf"}
   - {name: "URL", url: "https://bitbucket.org/guosheng/column-generation-hashing/"}
   - {name: "Code", url: "https://github.com/pcarbo/lbfgsb-matlab"}
---
Fast nearest neighbor searching is becoming
an increasingly important tool in solving
many large-scale problems. Recently
a number of approaches to learning datadependent
hash functions have been developed.
In this work, we propose a column
generation based method for learning datadependent
hash functions on the basis of
proximity comparison information. Given a
set of triplets that encode the pairwise proximity
comparison information, our method
learns hash functions that preserve the relative
comparison relationships in the data
as well as possible within the large-margin
learning framework. The learning procedure
is implemented using column generation and
hence is named CGHash. At each iteration
of the column generation procedure, the best
hash function is selected. Unlike most other
hashing methods, our method generalizes to
new data points naturally; and has a training
objective which is convex, thus ensuring
that the global optimum can be identi-
fied. Experiments demonstrate that the proposed
method learns compact binary codes
and that its retrieval performance compares
favorably with state-of-the-art methods when
tested on a few benchmark datasets.
