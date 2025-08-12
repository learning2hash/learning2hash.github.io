---
layout: publication
title: Clustering Based Opcode Graph Generation For Malware Variant Detection
authors: Kar Wai Fok, Vrizlynn L. L. Thing
conference: 2021 18th International Conference on Privacy, Security and Trust (PST)
year: 2021
bibkey: fok2021clustering
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.10048'}]
tags: []
short_authors: Kar Wai Fok, Vrizlynn L. L. Thing
---
Malwares are the key means leveraged by threat actors in the cyber space for
their attacks. There is a large array of commercial solutions in the market and
significant scientific research to tackle the challenge of the detection and
defense against malwares. At the same time, attackers also advance their
capabilities in creating polymorphic and metamorphic malwares to make it
increasingly challenging for existing solutions. To tackle this issue, we
propose a methodology to perform malware detection and family attribution. The
proposed methodology first performs the extraction of opcodes from malwares in
each family and constructs their respective opcode graphs. We explore the use
of clustering algorithms on the opcode graphs to detect clusters of malwares
within the same malware family. Such clusters can be seen as belonging to
different sub-family groups. Opcode graph signatures are built from each
detected cluster. Hence, for each malware family, a group of signatures is
generated to represent the family. These signatures are used to classify an
unknown sample as benign or belonging to one the malware families. We evaluate
our methodology by performing experiments on a dataset consisting of both
benign files and malware samples belonging to a number of different malware
families and comparing the results to existing approach.