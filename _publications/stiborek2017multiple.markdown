---
layout: publication
title: Multiple Instance Learning For Malware Classification
authors: "Jan Stiborek, Tom\xE1\u0161 Pevn\xFD, Martin Reh\xE1k"
conference: Expert Systems with Applications
year: 2017
bibkey: stiborek2017multiple
citations: 61
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.02268'}]
tags: ["Evaluation"]
short_authors: "Jan Stiborek, Tom\xE1\u0161 Pevn\xFD, Martin Reh\xE1k"
---
This work addresses classification of unknown binaries executed in sandbox by
modeling their interaction with system resources (files, mutexes, registry keys
and communication with servers over the network) and error messages provided by
the operating system, using vocabulary-based method from the multiple instance
learning paradigm. It introduces similarities suitable for individual resource
types that combined with an approximative clustering method efficiently group
the system resources and define features directly from data. This approach
effectively removes randomization often employed by malware authors and
projects samples into low-dimensional feature space suitable for common
classifiers. An extensive comparison to the state of the art on a large corpus
of binaries demonstrates that the proposed solution achieves superior results
using only a fraction of training samples. Moreover, it makes use of a source
of information different than most of the prior art, which increases the
diversity of tools detecting the malware, hence making detection evasion more
difficult.