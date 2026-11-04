# Assignment 01 — GitHub Pages deployment, testing and review record

Chan Ka Wai (mc649337) · Class D · CISC7204 · 4 November 2026

This record documents the deployment-and-testing check carried out on the Assignment 01
showcase before the BONUS work was registered in the Personal Registration Forum. It is the
evidence for the *"GitHub Pages deployment and testing"* and *"Feedback and Responsible
Sharing"* items of the Data Science Portfolio rubric and self-check list.

## Review committee

Two members of Class D – Team 04 were selected at random from the course pairing information
to support the deployment and testing of this assignment:

| Reviewer | Student ID |
|---|---|
| GUO YUANQI | MC649062 |
| ZHOU ZIROU | MC648937 |

The two members assigned to Assignment 02 are **different** (WANG XIAOYANG and LUO JUNPENG);
no student reviews both assignments. CHAN KA WAI (MC649337) is the author of the work and is
not a reviewer. LIU HAIXIANG (MC649298) reviewed the separate Practice 09 portfolio.

**Scope of the check:** open the live GitHub Pages site, follow every link that leads to the
Assignment 01 artefacts, confirm the repository URLs resolve, and report anything a reader
cannot reach or understand.

## What was tested

| Check | Result |
|---|---|
| Live showcase URL returns HTTP 200 | Pass |
| Assignment 01 repository folder URL returns HTTP 200 | Pass |
| 60 screenshot images on the live site load (HTTP 200) | Pass — 60/60 |
| Links on the live site resolve | **2 fail** (both relative directory paths) |
| Assignment 01 and Practice 09 links in *"How it is built"* | **Fail — HTTP 404** |
| Module 01–06 archives reachable from the live site | **Fail — no links** |
| No passwords, API keys or restricted datasets exposed | Pass |

## Findings

1. **Broken links (deployment defect).** The *"How it is built"* section linked to
   `cisc7204-Assgn01-2026-mc649337/` and `practice-09-ds-portfolio/`. GitHub Pages does not
   serve directory listings, so both relative paths returned HTTP 404. A reader following the
   only Assignment 01 link on the live site reached an error page.
2. **No Assignment 01 presence on the live site.** The showcase presented five Assignment 02
   module cards and a screenshot gallery, but nothing for Assignment 01. The six module
   archives and the pair preliminary project could only be found by browsing the repository
   manually.
3. **Archives are not inspectable in a browser.** Each module is a `.zip`, so a reviewer must
   download and extract it before seeing a notebook or a screenshot. There was no list of the
   six archives on the deployed page.
4. **No visible verification record.** The live site showed the work but did not state who had
   tested the deployment or what had been corrected, so the testing-and-revision evidence was
   not identifiable from the submitted URL.

## Improvement committed in response

The corrective commits are `92a86b2c2451be1f743f94c8c6dd4b7279368eaa` and `19d331740805effc818f40c930fb072334a8e10e` (*Fix the broken Assignment 01 link and document deployment testing on the live showcase*); the hash is recorded here so the feedback-to-commit chain stays resolvable even if the message is reworded.

| Finding | Change | Commit message |
|---|---|---|
| 1 | Replaced both 404 directory links with public GitHub tree URLs | `Fix the broken Assignment 01 link and document deployment testing on the live showcase` + `Fix the remaining Practice 09 directory link so every showcase link resolves` |
| 2 & 3 | Added an *Assignment 01* section to the live showcase with six direct module-archive links and the pair preliminary project | same commit |
| 4 | Added a *Deployment, testing and review* section naming both review committees, the test counts and the correction | same commit |
| — | Added this review record inside the Assignment 01 folder | `Add the Assignment 01 deployment and testing review record` |

The commits are genuine changes to the deployed `index.html`: the live site now shows both
assignments, all 60 images and all links resolve, and the two previously broken paths are gone.

## Declaration of AI usage

The deployment check (HTTP status of every image and link) and the write-up of this record were
prepared with AI assistance (DeepSeek-V4.1-Flash). The repository contents, the notebooks
and the screenshots are my own coursework. The two named committee members were assigned to this assignment and reviewed the
deployment; their findings are recorded above and every corrective commit is listed in the
table that follows the findings.

---

**Public URLs for this assignment**

- Live showcase: <https://kelvin-chan-ka-wai.github.io/CISC7204-mc649337-2026GitHub/#assignment-01>
- Repository folder: <https://github.com/Kelvin-Chan-Ka-Wai/CISC7204-mc649337-2026GitHub/tree/main/cisc7204-Assgn01-2026-mc649337>
