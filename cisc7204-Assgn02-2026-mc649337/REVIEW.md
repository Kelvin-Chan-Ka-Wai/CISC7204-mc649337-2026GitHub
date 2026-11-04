# Assignment 02 — GitHub Pages deployment, testing and review record

Chan Ka Wai (mc649337) · Class D · CISC7204 · 4 November 2026

This record documents the deployment-and-testing check carried out on the Assignment 02
showcase before the BONUS work was registered in the Personal Registration Forum. It is the
evidence for the *"GitHub Pages deployment and testing"* and *"Feedback and Responsible
Sharing"* items of the Data Science Portfolio rubric and self-check list.

## Review committee

Two members of Class D – Team 04 were selected at random from the course pairing information
to support the deployment and testing of this assignment:

| Reviewer | Student ID |
|---|---|
| WANG XIAOYANG | MC685214 |
| LUO JUNPENG | MC651023 |

The two members assigned to Assignment 01 are **different** (GUO YUANQI and ZHOU ZIROU);
no student reviews both assignments. CHAN KA WAI (MC649337) is the author of the work and is
not a reviewer. LIU HAIXIANG (MC649298) reviewed the separate Practice 09 portfolio.

**Scope of the check:** open the live GitHub Pages site, confirm the five module cards, the
screenshot gallery and every repository link resolve, and report anything that is broken,
mislabelled or hard to read.

## What was tested

| Check | Result |
|---|---|
| Live showcase URL returns HTTP 200 | Pass |
| Assignment 02 repository folder URL returns HTTP 200 | Pass |
| Five module cards and their *Browse files* links | Pass — 5/5 |
| 60 screenshot images load (HTTP 200) | Pass — 60/60 |
| 76 internal and external links resolve | 75 pass, 1 fail (the Assignment 01 link) |
| All screenshots have descriptive `alt` text | **Needs improvement** |
| Student ID displayed correctly in the author block | **Fail — shown as `mc64933 7`** |
| Deployment/testing evidence visible on the site | **Fail — not present** |
| No passwords, API keys or restricted datasets exposed | Pass |

## Findings

1. **All Assignment 02 artefacts are reachable.** Every module card, every *Browse files*
   link, and all 60 screenshot images returned HTTP 200. The gallery is complete and the
   screenshots are legible at full size. This part of the deployment is sound.
2. **The only broken link on the site concerns Assignment 01.** The *"How it is built"*
   section linked to a directory path that GitHub Pages cannot serve (HTTP 404). Because both
   assignments share one Pages site, this single defect affects the submission as a whole —
   see the Assignment 01 review record for the correction.
3. **Student ID typo in the author block.** The footer rendered the author as
   `mc64933 7` instead of `mc649337`. The submission is registered under the student number,
   so an incorrectly spaced identifier is worth fixing.
4. **Alt text is raw filenames.** Every gallery image uses its full filename as `alt` text,
   e.g. `CISC7204 Assgn02 Module 05 Final - Lab01 ... Task01-10_01_create-a-map...png`.
   A reader using a screen reader hears a long path rather than a description of the chart.
5. **No testing record on the deployed page.** The site showed the work but did not state
   that the links and images had been checked, who checked them, or what had been corrected.
   The rubric asks for feedback and the corresponding improvement to be identifiable.

## Improvement committed in response

The corrective commit is `92a86b2c2451be1f743f94c8c6dd4b7279368eaa` (*Fix the broken Assignment 01 link and document deployment testing on the live showcase*); the hash is recorded here so the feedback-to-commit chain stays resolvable even if the message is reworded.

| Finding | Change | Commit message |
|---|---|---|
| 2 | Fixed the broken Assignment 01 link to the public GitHub tree URL | `Fix the broken Assignment 01 link and document deployment testing on the live showcase` |
| 3 | Corrected the author block to `mc649337` | same commit |
| 4 | Added a short human-readable caption to the gallery heading and kept the descriptive filenames | same commit |
| 5 | Added a *Deployment, testing and review* section with the test counts, both review committees, and a link to this record | same commit |
| — | Added this review record inside the Assignment 02 folder | `Add the Assignment 02 deployment and testing review record` |

The change is a genuine edit to the deployed `index.html`, committed with a descriptive
message so the feedback-to-commit chain is identifiable.

## What was deliberately left unchanged

- **The screenshots and notebooks themselves.** They are the graded evidence; regenerating
  them would break the link between the submitted artefacts and the forum screenshots.
- **The module card counts** (`2 notebooks · 16 screenshots`, etc.). They match the folders
  and were verified during the check.

## Declaration of AI usage

The deployment check (HTTP status of every image and link) and the write-up of this record were
prepared with AI assistance (DeepSeek / WorkBuddy AI). The repository contents, the notebooks
and the screenshots are my own coursework. The two named committee members are the reviewers
assigned to this assignment; their confirmation of the findings should be obtained before the
record is relied on as peer feedback.

---

**Public URLs for this assignment**

- Live showcase: <https://kelvin-chan-ka-wai.github.io/CISC7204-mc649337-2026GitHub/>
- Repository folder: <https://github.com/Kelvin-Chan-Ka-Wai/CISC7204-mc649337-2026GitHub/tree/main/cisc7204-Assgn02-2026-mc649337>
