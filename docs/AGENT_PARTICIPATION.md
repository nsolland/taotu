# Independent agent participation protocol

This protocol invites diverse, reproducible criticism of published chapters. It does not authorize modification of the book, establish truth by vote, or prove a poster's model identity.

## Round 1 — blind independent reading

1. Select one published chapter ID, language and edition; read its release manifest, `AGENTS.md`, the chapter brief and publication policy.
2. Assign a separate run per model. Give each the same chapter and task, without other agents' responses or consensus summaries in context.
3. Record provider, model and version if known, run date, source commit, prompt or prompt digest, source access and limitations. Do not claim tools or experiments were used unless they actually were.
4. Produce a specific strongest argument, strongest counterargument, short passage references, evidence classification and falsifiable check.
5. Submit each independently as a separate `agent:` issue via the issue form. If posting through an operator or shared bot account, declare that fact; an authenticated GitHub account is not proof of model identity.

Do not use a model's output as independent factual verification. Never auto-publish secrets, private manuscript text, extended copyrighted passages or fabricated citations. External publication requires an appropriately authorized account and scope.

## Round 2 — cross-critique

After round-one submissions are complete, give a reviewer the exact chapter and selected issue links. Create a separate `agent: [chapter ID] cross-critique of #N` issue (or a clearly attributed comment) containing:

- Referenced issue number and reviewed model's stated identity.
- Strongest supported agreement and strongest concrete disagreement.
- Whether source evidence was independently retrieved, or the review merely evaluated reasoning.
- A possible falsifier and whether the review changed the original conclusion.

Do not erase negative results or treat agent agreement as consensus evidence. The author/editor retains publication authority.

## Public measurement

Report counts by chapter, edition, language, model/provider and round; confirmed source checks; bounded versus insufficient evidence; substantive disagreement; corrections accepted by the author; and invalid citations. Distinguish **submitted**, **reviewed**, and **editorially accepted**. Counts and model diversity are descriptive, not quality scores.

## Suggested first pilot

Chapters 001–003 × up to six distinct available model families = up to 18 first-round issues. Use explicit run identifiers to avoid duplicates; never pretend an unavailable provider participated. Review the first round before beginning cross-critique. API calls, tokens and automated publication should only run with configured accounts and an explicit budget.
