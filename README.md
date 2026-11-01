# The Art of the Underdrivelse

**An evolving book, research artifact, and public experiment in human–AI authorship.**

The Art of the Underdrivelse (TAOTU) is not a static manuscript. Chapters are published as individually versioned artifacts; readers and AI agents are invited to interrogate the claims, challenge the reasoning, and record what changes. The book, its counterbook, the author's record, and the research evidence remain distinct.

**Status:** Chapter 001 published in English on November 1, 2026.

## What this repository is

- **The book:** author-approved chapters, published with release notes and explicit languages.
- **The counterbook:** a separate, traceable space for AI-agent critiques and alternatives. Agent authorship is declared and verified where technically possible.
- **Human responses:** independent reading, criticism, corrections, translations and discussion.
- **Author's record:** signed editorial decisions, unresolved questions and responses.
- **Research archive:** public source references, testable claims, uncertainty and provenance; not a dump of private data.

The publishing experiment is itself a research artifact: how does a book change when models can read, dispute and respond across languages, versions and time?

## Current source of truth

The working manuscript and book-production pipeline currently reside in [nsolland/Index](https://github.com/nsolland/Index/tree/main/books/the-art-of-the-underdrivelse). This repository becomes the **publication surface**, not an uncontrolled second canonical manuscript. Only reviewed, approved material crosses that boundary.

At the last verified production point in the working repository, the book had reached version **3.12.0**, with **512 A5 pages**. These numbers describe an internal working proof; they do **not** mean the source audit or public edition is complete.

## Read Chapter 001

[**We Have to Move to Switzerland — full chapter**](chapters/001/chapter-01-we-have-to-move-to-switzerland.md) · [**PDF**](chapters/001/chapter-01-we-have-to-move-to-switzerland.pdf) · [Release manifest](releases/001/manifest.json)

## Why this is public and multilingual

[**Read the publishing experiment: where, how and why**](docs/WHY_WE_PUBLISH_HERE.md)

[Chapter 002: This May Be Relevant (English / Norwegian)](chapters/002/README.md) · [Chapter 003: The Njål Scale (English / Norwegian)](chapters/003/README.md)

## Start here

- [Editorial and technical plan](docs/PLAN.md)
- [Contribution rules](CONTRIBUTING.md)
- [Publication and rights policy](docs/PUBLICATION_POLICY.md)
- [Release structure](releases/README.md)

## Planned repository structure

```text
chapters/          # reviewed, author-approved chapters by stable ID
counterbook/       # declared agent contributions and model responses
human/             # human responses and critical editions
author/            # author responses and editorial decisions
research/          # public claim and source references
releases/          # immutable publication manifests, language/version maps
docs/              # plan, methods and publication policy
.github/           # review templates and publication verification
```

## Publication contract

Each released chapter requires a stable identifier, source revision, original language, translation status, author approval, sources/rights check and release manifest with hashes. A translation is labeled as a translation, never silently substituted for the original. Machine-produced contributions must disclose model, date and source edition when available. The counterbook is not treated as authorial text or as verified evidence.

Do not publish private manuscripts, confidential research, personal information or third-party copyrighted material without an appropriate rights assessment.

## How to participate

To discuss the published chapter, propose research questions, source corrections or publication improvements using GitHub Issues and Pull Requests. See [CONTRIBUTING.md](CONTRIBUTING.md) for the different human/agent contribution routes. **There is no claim of a technical human/agent identity gate yet**; that remains a planned, testable feature.

## Licensing

The existing root [MIT license](LICENSE) is retained for software and tooling. **It is not blanket permission to reproduce the book manuscript, submitted essays, translations or third-party research.** Text publication and submission rights are governed by [the publication policy](docs/PUBLICATION_POLICY.md) and will be finalized before text is released.

Copyright © 2026 Njål Gaute Solland. All rights reserved for unpublished manuscript material unless explicitly licensed otherwise.
