---
layout: publication
title: "Optimal Hashing in External Memory"
authors: Conway Alex, Farach-Colton Martin, Shilane Philip
conference: Arxiv
year: 2018
bibkey: conway2018optimal
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1805.09423"}
tags: ['ARXIV']
---
Hash tables are a ubiquitous class of dictionary data structures. However,
standard hash table implementations do not translate well into the external
memory model, because they do not incorporate locality for insertions. Iacono
and Patracsu established an update/query tradeoff curve for external hash
tables: a hash table that performs insertions in \$O(\lambda/B)\$ amortized IOs
requires \$\Omega(\log_\lambda N)\$ expected IOs for queries, where \$N\$ is the
number of items that can be stored in the data structure, \$B\$ is the size of a
memory transfer, \$M\$ is the size of memory, and \$\lambda\$ is a tuning
parameter. They provide a hashing data structure that meets this curve for
\$\lambda\$ that is \$\Omega(\log\log M + \log_M N)\$. Their data structure,
which we call an \defn{IP hash table}, is complicated and, to the best of our
knowledge, has not been implemented. In this paper, we present a new and much
simpler optimal external memory hash table, the \defn{Bundle of Arrays Hash
Table} (BOA). BOAs are based on size-tiered LSMs, a well-studied data structure,
and are almost as easy to implement. The BOA is optimal for a narrower range of
\$\lambda\$. However, the simplicity of BOAs allows them to be readily modified
to achieve the following results: \begin{itemize} \item A new external memory
data structure, the \defn{Bundle of Trees Hash Table} (BOT), that matches the
performance of the IP hash table, while retaining some of the simplicity of the
BOAs. \item The \defn{cache-oblivious Bundle of Trees Hash Table} (COBOT), the
first cache-oblivious hash table. This data structure matches the optimality of
BOTs and IP hash tables over the same range of \$\lambda\$. \end{itemize}
