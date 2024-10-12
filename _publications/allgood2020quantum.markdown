---
layout: publication
title: A Quantum Algorithm To Locate Unknown Hashgrams
authors: Allgood Nicholas R., Nicholas Charles K.
conference: "Arxiv"
year: 2020
bibkey: allgood2020quantum
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2005.02911"}
tags: ['ARXIV']
---
Quantum computing has evolved quickly in recent years and is showing significant benefits in a variety of fields, especially in the realm of cybersecurity. The combination of software used to locate the most frequent hashes and \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\}-grams that identify malicious software could greatly benefit from a quantum algorithm. By loading the table of hashes and \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\}-grams into a quantum computer we can speed up the process of mapping \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\}-grams to their hashes. The first phase will be to use KiloGram to find the top-\{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\} hashes and \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\}-grams for a large malware corpus. From here, the resulting hash table is then loaded into a quantum simulator. A quantum search algorithm is then used search among every permutation of the entangled key and value pairs to find the desired hash value. This prevents one from having to re-compute hashes for a set of \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\}-grams, which can take on average \{&#37; raw &#37;\}\\(O(MN)\\)\{&#37; endraw &#37;\} time, whereas the quantum algorithm could take \{&#37; raw &#37;\}\\(O(\sqrt\{N\})\\)\{&#37; endraw &#37;\} in the number of table lookups to find the desired hash values.
