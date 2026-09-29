---
name: bilibili-creator-studio
description: "Research, plan, draft, preview, and review Bilibili video content for aspiring or active creators. Use when a user needs topic discovery or validation, channel positioning, a knowledge talking-head, Vlog, or comedic monologue structure, an adjustable-tone word-for-word script, an audio-visual preview, a publishing package, or a post-publication retrospective. Do not use for merely downloading, editing, or uploading an already-finished video."
---

# B站创作者工作台

Turn a vague idea, source, lived experience, or existing draft into an honest, shootable Bilibili video plan. Optimize for audience value, creator fit, clarity, and learning speed—not a promised “viral formula.”

## Operating principles

- Preserve the creator's actual experience, constraints, and point of view. Never manufacture credentials, test results, audience data, personal anecdotes, or “candid” moments.
- Treat platform behavior as changeable. For current trends, competitor results, policy, or feature claims, research them now and record dates and sources. If research is unavailable, label the judgment as a hypothesis.
- Keep three layers separate: verified fact, creator-supplied claim, and creative choice. Flag high-stakes claims for primary-source verification.
- Titles and covers may create curiosity, but the opening must promptly honor the same promise. Do not recommend misleading packaging, fake scarcity, engagement bait, or guaranteed performance.
- Prefer the smallest useful deliverable. Do not force a full production dossier when the user only wants topic options or a structure review.
- A format is an expressive choice, not a Bilibili category. The same topic may work as knowledge talking-head, Vlog, or comedic monologue.

## Choose an operating mode

Infer the mode from the request. Ask only for missing information that would materially change the result.

- **Explore:** channel direction, audience, content pillars, or a topic pool.
- **Develop:** one idea from research through a complete preview script.
- **Audit:** diagnose an existing title, outline, or script without rewriting unless asked.
- **Retrospect:** use actual performance data and creator observations to decide the next experiment.

For a new creator, establish a lightweight creator compass before generating many ideas: knowledge/experience, access to people or places, comfort on camera, available time and budget, privacy boundaries, desired audience relationship, and sustainable publishing cadence. Do not make completion of a long questionnaire a prerequisite.

## Core workflow

### 1. Frame the content job

Capture or infer:

- target viewer and the moment in which they would choose this video;
- one viewer-facing promise;
- desired outcome: understand, feel, decide, try, or discuss;
- evidence or experience already available;
- target duration range, production constraints, and whether the user wants a quick draft or a researched package.

Restate the working brief in no more than six lines. Mark assumptions that materially affect the concept.

### 2. Research and validate the topic

Read [research-and-topic-validation.md](references/research-and-topic-validation.md) when the user asks for topic discovery, current opportunity assessment, competitor research, or factual content.

Build a small evidence table before scoring. Evaluate audience need, creator edge, freshness, proofability, producibility, and series potential. Use `unknown` instead of invented numbers. Distinguish:

- **signal:** observed search, platform, community, or channel evidence;
- **interpretation:** what the signal might mean;
- **experiment:** the cheapest publishable way to test it.

Offer a decision, not merely a score: pursue, narrow, re-angle, park, or reject.

### 3. Design the promise and packaging together

Produce one primary promise and up to three title-cover pairs. Each pair must specify:

- what the viewer expects to receive;
- the curiosity gap, if any;
- a cover concept with minimal readable text;
- the exact opening beat that pays off the promise;
- any risk of exaggeration or ambiguity.

Do not claim that a title formula is an algorithmic preference. Packaging is a hypothesis to test against real impressions, clicks, and retention.

### 4. Select the expression format

If the user has not chosen a format, compare the three in a compact table and recommend one. Before writing a complete script, let the user choose when practical; if they asked for an autonomous draft, state the chosen format and rationale and continue.

| Format | Best source material | Primary engine | Main production risk |
|---|---|---|---|
| Knowledge talking-head | research, expertise, demonstrations | question → explanation → proof → use | accurate but lecture-like |
| Vlog | access, lived process, place, challenge | goal → attempts → change → reflection | footage without a story |
| Comedic monologue / 脱口秀 | a strong personal point of view and contradictions | premise → escalation → punch/tag/callback | jokes without a coherent argument |

Then read exactly the relevant guide:

- [knowledge-talking-head.md](references/knowledge-talking-head.md)
- [vlog.md](references/vlog.md)
- [comedic-monologue.md](references/comedic-monologue.md)

Hybrid formats are allowed, but name the dominant engine and use the other format only where it has a clear job.

### 5. Calibrate tone without erasing the creator

Read [tone-and-voice.md](references/tone-and-voice.md) when the user requests a tone, provides samples, or wants variants. Represent tone with adjustable dimensions rather than a single adjective. Preserve factual meaning across variants. Do not imitate a living creator; translate the request into abstract traits.

When tone is unclear, propose one default profile plus at most two meaningfully different alternatives. Show a 80–150 Chinese-character sample before rewriting a long script when a tone mismatch would be expensive.

### 6. Build the structure before prose

Create a beat sheet whose units each have a job, evidence or experience, visual treatment, and transition. Use timestamps only as estimates. Avoid universal beat intervals or fixed interaction quotas.

Check the structure for:

- promise paid early;
- necessary context before complexity;
- genuine progression rather than repeated wording;
- a change in knowledge, situation, or emotional value at each major beat;
- a conclusion earned by the preceding material;
- interaction prompts only where viewers can contribute a real judgment or experience.

### 7. Draft the word-for-word script and audio-visual preview

Read [deliverables.md](references/deliverables.md) for the output contracts. Draft for the ear: speakable sentences, intentional pauses, concrete nouns, and visible actions. Separate audio from visual intent. Attach evidence IDs to factual claims when research was used.

For Vlogs, distinguish planned narration, capture targets, and moments that must remain unscripted. For comedy, label setups, punches, tags, act-outs, and callbacks during review, but remove craft labels from the clean performance script unless requested.

Estimate runtime with a creator-specific measured rate when available. Otherwise report a range and state the assumption. The bundled `scripts/script_metrics.py` can count Chinese characters, Latin words, cues, and unresolved placeholders; it does not predict actual delivery better than a table read.

### 8. Run the preview gate

Before treating the script as final, produce a text preview containing:

1. a one-paragraph viewer experience summary;
2. a timeline or audio-visual table;
3. the first 30–45 seconds in full;
4. estimated runtime and assumption;
5. promise/payoff check;
6. evidence and compliance risks;
7. likely confusion, drag, or expensive shots;
8. a prioritized cut/change list.

For a full workflow, ask for approval of the script before expanding into a detailed shot list, storyboard, or generation prompts. Cheap text decisions should precede expensive production decisions.

### 9. Prepare the publishing package

After script approval, supply only the requested items: final title-cover pairs, description, chapters, source note, tags/topics, pinned comment, natural interaction prompt, and a small experiment plan. Ensure title, cover, opening, and content describe the same value.

For regulated, sponsored, medical, financial, legal, safety, or youth-related content, research the current applicable rules and flag required disclosures or professional review. Never infer permission to publish or make external changes.

### 10. Close the learning loop

For post-publication review, read [quality-and-retrospective.md](references/quality-and-retrospective.md). Use actual observations: impressions, click-through behavior where available, early retention, average viewing, peaks/dips, comments, follows, saves/coins/likes, and creator production cost. Avoid cross-video comparisons that ignore topic, traffic source, audience, or length.

End with one to three testable changes for the next video. Do not rewrite the whole creative identity from one result.

## Output discipline

- Cite research close to the claim and include access dates for volatile sources.
- When no live research was performed, say so; never present estimated demand or competition as observed platform data.
- Label optional ideas as optional. Separate essential fixes from enhancements.
- When working in a project directory, keep inspectable artifacts using the filenames in [deliverables.md](references/deliverables.md). Otherwise return the same sections in chat without creating files.
- Default to Chinese for user-facing deliverables unless the user requests another language.

## Definition of done

The result is complete when the user has a defensible topic decision, a format and tone choice, a coherent beat structure, a speakable and shootable script, a preview with timing and risks, and an explicit next step. If the user asked for publishing or retrospective support, also include a truthful packaging experiment or evidence-based learning plan. No claim of virality or guaranteed growth is allowed.
