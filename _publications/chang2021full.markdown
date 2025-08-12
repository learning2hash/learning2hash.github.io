---
layout: publication
title: Full-privacy Secured Search Engine Empowered By Efficient Genome-mapping Algorithms
authors: Yuan-yu Chang, Sheng-tang Wong, Emmanuel O Salawu, Yu-xuan Wang, Jui-hung
  Hung, Lee-wei Yang
conference: IEEE Journal of Biomedical and Health Informatics
year: 2023
bibkey: chang2021full
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.00696'}]
tags: ["Efficiency", "Privacy & Security"]
short_authors: Chang et al.
---
Since the 90s, keyword-based search engines have been helping people locate
relevant web content via a simple query, so have the recent full-text-based
search engines mainly used for plagiarism detection following an article
upload. However, these "free" or paid services operate by storing users' search
queries and preferences for personal profiling and targeted ads delivery, while
user-uploaded articles can further profit the service providers as part of
their expanding databases. In short, search engine privacy has not been an
option for web exploration in the past decades. Here we demonstrate that a
database or internet search, provided with the entire article as a query, can
be correctly carried out without revealing users' sensitive queries by an
irreversible encoding scheme and an efficient FM-index search routine that is
generally used in the NGS of genomes. In our solution, Sapiens Aperio Veritas
Engine (S.A.V.E.), every word in the query is encoded into one of 12 "amino
acids" (a.a.) comprising a pseudo-biological sequence (PBS) at users' local
machines. The PBS-mediated plagiarism detection is done by users' submission of
locally encoded PBS through our cloud service to locate identical duplicates in
the collected web contents which had been encoded in the same way as the query.
It is found that PBSs with a length longer than 12 a.a., can return correct
results with a false positive rate <0.8%. S.A.V.E. runs at a similar speed as
Bowtie and is 4 orders faster than BLAST. S.A.V.E., functioning in both regular
and in-private search modes, provides a new option for efficient internet
search and plagiarism detection in a compressed search space without a chance
of storing and revealing users' confidential contents. We expect that future
privacy-aware search engines can reference the ideas proposed herein. S.A.V.E.
is made available at https://dyn.life.nthu.edu.tw/SAVE/