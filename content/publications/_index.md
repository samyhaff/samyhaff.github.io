+++
title = "Publications"
description = "Publications and preprints by Samy Haffoudhi."
template = "prose.html"
insert_anchor_links = "none"

[extra]
lang = 'en'
math = false
mermaid = false
copy = true
comment = false
+++

My publications, most recent first. See also my [Google Scholar profile](https://scholar.google.com/citations?user=YI7i_z8AAAAJ&hl=fr) and my [projects](/projects).

## 2026

**LELA: an LLM-based Entity Linking Approach with Zero-Shot Domain Adaptation** \
**Samy Haffoudhi**, Fabian M. Suchanek, Nils Holzenberger \
*International Semantic Web Conference (ISWC), Bari, Italy, 2026* \
[paper](https://arxiv.org/abs/2601.05192) · [code](https://github.com/dig-team/LELA)

<details>
<summary><span>Abstract</span></summary>

Entity linking (mapping ambiguous mentions in text to entities in a knowledge base) is a foundational step in tasks such as knowledge graph construction, question-answering, and information extraction. Our method, LELA, is a modular coarse-to-fine approach that leverages the capabilities of large language models (LLMs), and works with different target domains, knowledge bases and LLMs, without any fine-tuning phase. Our experiments across various entity linking settings show that LELA is highly competitive with fine-tuned approaches, and substantially outperforms the non-fine-tuned ones.

</details>

<details>
<summary><span>BibTeX</span></summary>

```bibtex
@inproceedings{haffoudhi2026lela,
  title     = {{LELA}: an {LLM}-based Entity Linking Approach with Zero-Shot Domain Adaptation},
  author    = {Haffoudhi, Samy and Suchanek, Fabian M. and Holzenberger, Nils},
  booktitle = {The Semantic Web -- ISWC 2026: 25th International Semantic Web Conference,
               Bari, Italy, October 25--29, 2026, Proceedings},
  series    = {Lecture Notes in Computer Science},
  publisher = {Springer},
  address   = {Cham},
  year      = {2026},
  url       = {https://arxiv.org/abs/2601.05192}
}
```

</details>

**LELA: An End-to-end LLM-based Entity Linking Framework with Zero-shot Domain Adaptation** \
**Samy Haffoudhi**, Nikola Dobričić, Fabian M. Suchanek, Nils Holzenberger \
*35th International Joint Conference on Artificial Intelligence (IJCAI-ECAI 2026), Demonstrations Track, Bremen, Germany* \
[paper](https://arxiv.org/abs/2605.26956) · [demo](/LELA_Demo.pdf) · [code](https://github.com/dig-team/LELA)

<details>
<summary><span>Abstract</span></summary>

Entity linking is a key component of many downstream NLP systems, yet existing approaches are often tied to the specific target knowledge bases and domains, limiting their real world application. In this paper, we extend LELA, a modular and domain-agnostic LLM-based entity disambiguation method, into a practical Python library that integrates zero-shot Named Entity Recognition (NER) — thereby providing a complete end-to-end pipeline for entity-linking in real-world usage. We provide experimental results validating LELA's performance and robustness across diverse entity linking settings. In our demo, users can play with the system on their own input texts.

</details>

<details>
<summary><span>BibTeX</span></summary>

```bibtex
@inproceedings{haffoudhi2026lelademo,
  title     = {{LELA}: An End-to-end {LLM}-based Entity Linking Framework with Zero-shot Domain Adaptation},
  author    = {Haffoudhi, Samy and Dobri{\v{c}}i{\'{c}}, Nikola and Suchanek, Fabian M. and Holzenberger, Nils},
  booktitle = {Proceedings of the Thirty-Fifth International Joint Conference on
               Artificial Intelligence, {IJCAI-ECAI} 2026},
  publisher = {International Joint Conferences on Artificial Intelligence Organization},
  note      = {Demonstrations Track},
  year      = {2026},
  month     = {8},
  url       = {https://arxiv.org/abs/2605.26956}
}
```

</details>

## Preprints

**Retrieval-Constrained Decoding Reveals Underestimated Parametric Knowledge in Language Models** \
Rajaa El Hamdani, **Samy Haffoudhi**, Nils Holzenberger, Fabian M. Suchanek, Thomas Bonald, Fragkiskos D. Malliaros \
*arXiv:2509.23417, 2025* \
[preprint](https://arxiv.org/abs/2509.23417) · [code](https://github.com/Rajjaa/disambiguated-LLM)

<details>
<summary><span>Abstract</span></summary>

Language models (LMs) encode substantial factual knowledge, but often produce answers judged as incorrect. We hypothesize that many of these answers are actually correct, but are expressed in alternative surface forms that are dismissed due to an overly strict evaluation, leading to an underestimation of models' parametric knowledge. We propose Retrieval-Constrained Decoding (RCD), a decoding strategy that restricts model outputs to unique surface forms. We introduce YAGO-QA, a dataset of 19,137 general knowledge questions. Evaluating open-source LMs from 135M to 70B parameters, we show that standard decoding undervalues their knowledge. For instance, Llama-3.1-70B scores only 32.3% F1 with vanilla decoding but 46.0% with RCD. Similarly, Llama-3.1-8B reaches 33.0% with RCD, outperforming the larger model under vanilla decoding. We publicly share the code and dataset at [github.com/Rajjaa/disambiguated-LLM](https://github.com/Rajjaa/disambiguated-LLM).

</details>

<details>
<summary><span>BibTeX</span></summary>

```bibtex
@misc{elhamdani2025rcd,
  title         = {Retrieval-Constrained Decoding Reveals Underestimated Parametric Knowledge in Language Models},
  author        = {El Hamdani, Rajaa and Haffoudhi, Samy and Holzenberger, Nils and Suchanek, Fabian M. and Bonald, Thomas and Malliaros, Fragkiskos D.},
  year          = {2025},
  eprint        = {2509.23417},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2509.23417}
}
```

</details>
