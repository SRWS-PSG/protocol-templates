# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository nature

This is a **documentation / planning workspace**, not a software codebase. There is no build system, no tests, no source code — only Markdown planning documents written primarily in Japanese.

The repository is also not a git repository (verified via the environment metadata). Do not assume `git log` / `git blame` will work; if version history is needed, ask the user before running `git init`.

## What this project is about

The work is centered on [plan.md](plan.md): a plan to update an existing **systematic review (SR) protocol template** that is currently published on **protocols.io**, and to make the updated template easier to cite and to discover via **Google Scholar**.

The strategy splits responsibilities across platforms — keep the *living* template on protocols.io (so the team can keep using and versioning it), but publish a separate short article/preprint on **Zenodo** so that Google Scholar can index it as a citable document with proper metadata (title, authors, publication date, DOI).

Key context to keep in mind when editing the plan:

- The goal is **not** peer-reviewed publication. It is internal team usability + Google-Scholar-friendly citability + future version management.
- protocols.io = the place the team actually edits and uses the template (DOI-versioned).
- Zenodo Article/Preprint = the surface that Google Scholar will pick up as a citation source.
- Optional supplementary placements: Zenodo or OSF Project for Word/Markdown/example/changelog files; a community preprint server if a domain-appropriate one exists.
- The plan references three external sources the user has already vetted — protocols.io, Google Scholar inclusion guidelines, and Zenodo's Google Scholar FAQ — so prefer those over guessing when policy questions come up.

## Working in this repo

- The primary (and currently only) artifact is [plan.md](plan.md). Edit it in place rather than spawning new planning files.
- The plan is written in Japanese with English field labels in the "record fields" code blocks. Match that style: Japanese prose, English/Markdown structure for templates and checklists.
- The plan is currently truncated mid-section ("Step 1 / 2.1 現在版の確認" ends with an empty "記録項目" block). Continuing the plan is a likely near-term task — pick up from where the existing structure leaves off rather than restructuring earlier sections.
- No commands to build, lint, or test. If the user later adds tooling (e.g. a Markdown linter, a PDF build for the Zenodo deposit), record those commands here.
