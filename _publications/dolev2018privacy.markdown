---
layout: publication
title: Privacy-preserving Secret Shared Computations Using Mapreduce
authors: Shlomi Dolev, Peeyush Gupta, Yin Li, Sharad Mehrotra, Shantanu Sharma
conference: IEEE Transactions on Dependable and Secure Computing
year: 2019
bibkey: dolev2018privacy
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.10323'}]
tags: ["Efficiency"]
short_authors: Dolev et al.
---
Data outsourcing allows data owners to keep their data at *untrusted*
clouds that do not ensure the privacy of data and/or computations. One useful
framework for fault-tolerant data processing in a distributed fashion is
MapReduce, which was developed for *trusted* private clouds. This paper
presents algorithms for data outsourcing based on Shamir's secret-sharing
scheme and for executing privacy-preserving SQL queries such as count,
selection including range selection, projection, and join while using MapReduce
as an underlying programming model. Our proposed algorithms prevent an
adversary from knowing the database or the query while also preventing
output-size and access-pattern attacks. Interestingly, our algorithms do not
involve the database owner, which only creates and distributes secret-shares
once, in answering any query, and hence, the database owner also cannot learn
the query. Logically and experimentally, we evaluate the efficiency of the
algorithms on the following parameters: (\textit\{i\}) the number of
communication rounds (between a user and a server), (\textit\{ii\}) the total
amount of bit flow (between a user and a server), and (\textit\{iii\}) the
computational load at the user and the server.\B