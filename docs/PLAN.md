# TAOTU — delivery plan

**Primary objective:** Build a complete, evidence-controlled public edition of *The Art of the Underdrivelse*, including an interactive multilingual chapter release process, three separate contribution surfaces, and traceability to the working manuscript.

## Governing rules

1. **No partial milestone replaces the objective.** Every milestone must identify what remains.
2. `nsolland/Index` remains the canonical working source until an explicitly documented migration. `taotu` is the publication repository.
3. Claims remain linked to their source and evidence status; a model-generated interpretation is not evidence.
4. No public transfer of confidential, NDA-restricted, private or uncleared third-party content.
5. Chapters release only after source audit, review, author sign-off, checksums and rendering checks.
6. A chapter's model-facing format, human-facing format and language variants may differ, but must map to the same stable edition ID.

## Execution sequence and acceptance gates

### 0 — Repository foundation (first deliverable)

- [x] Define README, editorial plan, contribution routes and rights boundaries.
- [ ] Add executable publication schemas and JSON validation.
- [ ] Set up CI for manifest/schema, Markdown links, metadata, file digests and content isolation.
- [ ] Document author, reviewer and release authority separately.

**Gate:** Documentation links resolve, validation runs on an example fixture, and CI fails on deliberately invalid metadata.

### 1 — Complete source audit (the controlling dependency)

Working baseline: 1,810 Library PDF/DOCX/MD/TXT items; 1,506 filename-normalized names. **These are metadata counts, not 1,506 verified distinct works.** The previous filename candidate list is a prioritization aid, not a substitute for examining the full corpus.

- [ ] Freeze a source inventory with IDs, version, access and provenance.
- [ ] Extract and hash content where access permits; identify exact and near duplicates.
- [ ] Classify **all** documents: research, book variant, original idea, correspondence, administrative, private, irrelevant, etc.
- [ ] Review every unique source family against current manuscript and claims.
- [ ] Apply evidence and rights grades, including `INSUFFICIENT_EVIDENCE`.
- [ ] Produce a full disposition ledger: integrated / already covered / rejected / restricted / unresolved.
- [ ] Close all unresolved coverage rows or explicitly record their blockers.

**Gate:** every counted file has a disposition; all eligible unique source families have an evidence/overlap decision. No open file silently becomes 'reviewed' through title matching.

### 2 — Editorial consolidation

- [ ] Compare newly supported claims against every chapter in the canonical manuscript.
- [ ] Integrate genuinely new narrative, eliminating repetition.
- [ ] Produce one consolidated edited manuscript and reproducible PDF/DOCX proofs.
- [ ] Run semantic, structural, visual and technical quality checks; verify page-by-page rendering.
- [ ] Record independent review limitations honestly.

**Gate:** chapter coverage matrix reconciled to source ledger; PDF/DOCX checks pass and changes are accepted by the author.

### 3 — Chapter release system

- [ ] Define stable chapter and release IDs, checksums, provenance, links to parent editions.
- [ ] Publish the first **cleared** chapter in a selected language with a release manifest.
- [ ] Provide source edition, translation provenance and how to submit corrections.
- [ ] Prevent changes to past release manifests; new editions supersede rather than silently overwrite.

**Gate:** independent reader can reconstruct the exact released text and its provenance.

### 4 — Interactive book and counterbook

- [ ] Separate `counterbook/`, `human/`, `author/` streams.
- [ ] Add distinct issue/PR templates, explicit authorship metadata and moderation rules.
- [ ] Design and test a machine-only counterbook submission gate; do not claim enforcement before verified.
- [ ] Introduce agent-to-agent critique with human author/editor approval for changes to the book.
- [ ] Make multilingual releases compare and cross-reference exact claims and sections.

**Gate:** an agent critique cannot alter the canonical chapter; a human response cannot falsely masquerade as verified agent output.

### 5 — Public research experiment and operations

- [ ] Publish versioned research questions, evaluation protocol and observational limitations.
- [ ] Track chapter change histories, disagreement, translation drift and model-specific failure.
- [ ] Publish reproducible aggregate measures without exposing private source content.
- [ ] Add installation/setup and maintainer support instructions; test a clean clone.
- [ ] Issue a verified public release with build artifact provenance.

**Final gate:** public chapters, interactive response areas, research ledger, provenance, reproducible builds and maintenance documentation operate end to end. Source-audit completion is non-negotiable.

## First concrete next engineering step

Implement `schemas/chapter.schema.json`, `schemas/release.schema.json`, `scripts/validate_publication.py`, minimal passing/failing fixtures and GitHub Actions. This creates a mechanically testable contract *before* any chapter is exposed. Then run the corpus audit from the working source, not by copying its private file list into this public repository.

## Status labels

`NOT_STARTED`, `IN_PROGRESS`, `BLOCKED_WITH_EVIDENCE`, `VERIFIED`. A generated file or passing local test alone does not prove public deployment.
