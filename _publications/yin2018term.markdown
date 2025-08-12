---
layout: publication
title: Term Definitions Help Hypernymy Detection
authors: Wenpeng Yin, Dan Roth
conference: Proceedings of the Seventh Joint Conference on Lexical and Computational
  Semantics
year: 2018
bibkey: yin2018term
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.04532'}]
tags: []
short_authors: Wenpeng Yin, Dan Roth
---
Existing methods of hypernymy detection mainly rely on statistics over a big
corpus, either mining some co-occurring patterns like "animals such as cats" or
embedding words of interest into context-aware vectors. These approaches are
therefore limited by the availability of a large enough corpus that can cover
all terms of interest and provide sufficient contextual information to
represent their meaning. In this work, we propose a new paradigm, HyperDef, for
hypernymy detection -- expressing word meaning by encoding word definitions,
along with context driven representation. This has two main benefits: (i)
Definitional sentences express (sense-specific) corpus-independent meanings of
words, hence definition-driven approaches enable strong generalization -- once
trained, the model is expected to work well in open-domain testbeds; (ii)
Global context from a large corpus and definitions provide complementary
information for words. Consequently, our model, HyperDef, once trained on
task-agnostic data, gets state-of-the-art results in multiple benchmarks