# Working with GitHub in the Pozzo Research Group

*For every student, postdoc and visitor who creates or maintains a repository in
[github.com/pozzo-research-group](https://github.com/pozzo-research-group). Read it once when you
join, and again when you start a repo, submit a paper, publish, and leave the group.*

Papers print our repository links, and other groups use our tools. A repo you create may still be
cited ten years after you have left. These rules keep the links working, keep credit attached to the
right people, and make each repo usable by whoever comes next. They follow established practice for
research software (see [Sources](#sources)), plus lessons from cleaning up this org in November 2026.

**When in doubt, ask Lilo before you act.** Most of the problems we fixed came from a repo created,
renamed, copied or left behind without anyone noticing.

---

## 1. Who does what

| Action | Who |
|---|---|
| Create, rename, transfer, archive or delete a repo | **Lilo** (ask her; she does it or tells you to) |
| Make a private repo public | **Lilo**, after the checks in §2 |
| Connect a repo to Zenodo | **Lilo** |
| Pin repos and edit the org front page | **Lilo** |
| Everything inside your repo: code, README, LICENSE, `CITATION.cff`, topics, description, releases | **You**, the repo's maintainer |

Every active repo has one named **maintainer**, listed in its README. That is usually you for the
repos you start. It changes when you leave (§10).

## 2. Starting a repository

1. **Check that it doesn't already exist.** Search the org first. If an existing repo covers your
   work, add to it (a branch, a folder, or a pull request) rather than starting a parallel copy.
2. **Ask Lilo** to create it, or for permission to create it in the org. Group work never lives in a
   personal account. A personal fork for day-to-day work is fine.
3. **Start private.** New repos stay private until there is a README, a LICENSE and nothing
   unpublished in them. Lilo makes them public, usually when the paper is submitted or published.
4. **Don't create empty placeholders.** Create the repo when you have something to put in it. Empty
   repos with only a slide template or a `.gitignore` had to be deleted or archived.
5. **Set your Git identity** once on every computer you commit from, so commits are credited to you
   (not to "Ubuntu" or "lab-pc"):
   ```
   git config --global user.name "Your Name"
   git config --global user.email "ID+username@users.noreply.github.com"
   ```
   Your noreply address is under GitHub → Settings → Emails
   ([GitHub Docs: Setting your commit email address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)).
6. Use **`main`** as the default branch.

### Naming

- New repos use **lowercase kebab-case**: `saxs-data-processing`, not `SAXS_Data_Processing` or
  `saxsDataProcessing`. The Python package inside keeps a snake_case import name
  ([PEP 8](https://peps.python.org/pep-0008/#package-and-module-names)).
- The name says what it is: `jubilee-pipette-tool`, `rhua-saxs-modeling`. Avoid personal names,
  conference names and dates unless the repo really is a one-off (and then it gets archived, §9).
- **Never make an "OLD-" or "-v2" copy.** Old versions live in the history, in tags and in releases.
  A copy splits issues, stars and citations across two repos. (We had `OT2Protocols` and
  `OLD-OT2Protocols`.)
- **Don't rename existing repos.** GitHub redirects a renamed repo only until another repo takes the
  old name ([GitHub Docs: Renaming a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository)).
  A repo cited in a paper is never renamed, moved or deleted. Its folder paths also stay where they
  are.

## 3. Description and topics

Every repo needs both. The org front page and GitHub search depend on them.

- **Description:** one plain sentence saying what the repo contains. Keep it current. "Analysis
  scripts for a work in progress… data will be made available once published" was still on a repo
  years after the paper came out. Once a paper is out, give its published title.
- **Topics:** exactly one **category topic**, plus a few specific ones
  ([GitHub Docs: Classifying your repository with topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)):

| Category | Category topic | Example extra topics |
|---|---|---|
| Analysis, modeling & data management | `analysis` (add `data-management` if relevant) | `saxs`, `sans`, `nexus`, `bayesian-optimization` |
| Lab automation & open hardware | `automation` (add `open-hardware` if relevant) | `jubilee`, `opentrons`, `3d-printing` |
| Papers & research projects | `paper` (published) or `project` (ongoing) | `nanoparticles`, `polymers`, `hydrogels` |
| Teaching, demos & community | `teaching` | `jubilee`, `bayesian-optimization` |

Add `jubilee` to anything built on Science Jubilee, and `opentrons` to anything for the OT-2. When a
repo is new or changes category, tell Lilo so the front page is updated.

## 4. README

GitHub shows the README first, so write it for someone who has never met you. Cover, in this order
([Wilson et al. 2017](https://doi.org/10.1371/journal.pcbi.1005510);
[The Turing Way](https://book.the-turing-way.org/project-design/project-repo/project-repo-readme)):

1. **What this is**, in one paragraph.
2. **Paper and DOI**, if any: the published title, linked to the paper's DOI, plus the DOI badge
   for the code (§7).
3. **Install**: the exact commands, starting from a fresh environment.
4. **Minimal example**: one command or a short notebook that runs in a few minutes.
5. **Data**: where it lives (a DOI, §8) and how to get it.
6. **Maintainer**, and how to report problems (GitHub Issues).
7. **How to cite**: "see `CITATION.cff`" is enough.

Keep it true:
- Remove badges for services that no longer run (we removed dead Travis CI and Coveralls badges).
- Delete placeholder text left by project generators.
- When a paper is published, replace "submitted" or working titles with the published citation. One
  README still gave a title the paper never had.
- If the repo is a fork, say so in the first lines (§6).

## 5. License

A repo without a LICENSE file is "all rights reserved" by default: nobody can legally reuse it
([GitHub Docs: Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)).

- **The group default is [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).** Put
  the license text in a file named `LICENSE` at the top of the repo.
- **Packages others will install** may use a permissive software license (for example
  [MIT](https://choosealicense.com/licenses/mit/), as autophasemap does), **with Lilo's approval**.
  If the repo has a `pyproject.toml`, the license there must match the LICENSE file.
- **Forks keep the upstream license.** Never relicense someone else's code.
- Work under a sponsored-research or IP agreement: ask Lilo before choosing a license.

## 6. Forks and outside code

- Fork into the org only when the group **contributes to or depends on** that project (for example
  `AFL-sample-loader`, `science_jubilee`). Say at the top of the README that it's a fork, link the
  original, and list the group's changes.
- Don't fork reading lists, "awesome" lists or other projects just to keep a copy. Star them instead.
- A repo made from someone else's template (GitHub's "Use this template") is not counted as a fork,
  so credit the original in the README yourself.

## 7. Citation, releases and DOIs

Software is a research output, and it should be cited like one
([Smith et al. 2016](https://doi.org/10.7717/peerj-cs.86);
[Barker et al. 2022, FAIR4RS](https://doi.org/10.1038/s41597-022-01710-x)).

### `CITATION.cff`

Every repo tied to a paper, and every package, has a `CITATION.cff` at the top. GitHub then shows a
**"Cite this repository"** button ([GitHub Docs: About CITATION files](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)),
and Zenodo copies its authors into the DOI record. Get it right before the first release:

```yaml
cff-version: 1.2.0
message: "If you use this software, please cite it as below."
title: "repo-name"
authors:
  - family-names: "Chiang"          # surname only
    given-names: "Huat Thart"       # first and middle names, initials
    orcid: "https://orcid.org/0000-0002-0042-7958"
  - family-names: "Pozzo"
    given-names: "Lilo D."
    orcid: "https://orcid.org/0000-0001-7104-9061"
preferred-citation:
  type: article
  title: "Published paper title"
  doi: "10.xxxx/xxxxx"
  journal: "Journal name"
  year: 2025
  publisher:
    name: "Publisher name"          # an object, not a plain string
  authors: [ ... ]
```

- **Authors are the people who wrote the software.** They may differ from the paper's author list.
  Agree on the list with Lilo.
- **Split names correctly.** `family-names: "D. Pozzo"` would put the wrong surname on a permanent
  DOI record. (This happened in one of our files and was caught just before release.)
- **Add ORCIDs** for everyone who has one.
- **Validate before you commit:**
  ```
  pip install cffconvert
  cffconvert --validate
  ```
  If the file is invalid, Zenodo may ignore it.

### Releases and Zenodo DOIs

Lilo has connected the org to [Zenodo](https://zenodo.org). Once she enables a repo, each GitHub
release is archived and gets a DOI
([GitHub Docs: Referencing and citing content](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content)).

1. **Before asking Lilo to enable Zenodo, search [zenodo.org](https://zenodo.org) for the repo name.**
   Several of our repos already had DOIs from earlier years. A second record splits citations and
   can't be merged.
2. **Release when you submit the paper**: GitHub → Releases → *Draft a new release*, tag `v1.0.0`
   (semantic versioning). Write a sentence on what the release is. Bump the version for every later
   release.
3. **Check the Zenodo record**: title, authors and spelling. Fix the `CITATION.cff` and release
   again rather than living with a wrong record.
4. **In the paper**, cite the **version DOI** of the exact release used. Give the GitHub URL as a
   second link. A DOI keeps working even if the repo moves.
5. **In the README**, add the badge for the **concept DOI**, which always resolves to the newest
   version:
   ```
   [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.NNNNNNN.svg)](https://doi.org/10.5281/zenodo.NNNNNNN)
   ```
6. If a repo has a `.zenodo.json`, Zenodo uses it instead of `CITATION.cff`. Keep only one of the
   two.

## 8. Data, large files and secrets

Git keeps every version of every file forever. Large files committed once slow down every clone, and
removing them means rewriting history, which changes the commit hashes papers may cite.

- **GitHub limits:** it warns at 50 MiB per file and blocks files over 100 MiB. Repos should ideally
  stay under 1 GB ([GitHub Docs: About large files](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)).
  Several of our repos are far over that (one is 2.8 GB).
- **Raw and large data go to a data repository**, usually Zenodo, with its own DOI. Put that DOI in
  the README and download the data with a small script
  ([Wilson et al. 2017](https://doi.org/10.1371/journal.pcbi.1005510);
  [Wilkinson et al. 2016, FAIR](https://doi.org/10.1038/sdata.2016.18)). For SAXS and UV-Vis data,
  the group's NeXus/NOMAD tools (`theia`, `pispis`) are the longer-term home.
- **Keep only small example or test data in Git**, a few MB in total, in `data/` or `tests/data/`.
- **Never commit** passwords, API tokens, instrument credentials or `.env` files. If one slips in,
  tell Lilo and revoke it right away: deleting the file doesn't remove it from history.
- Use a `.gitignore` from the start. It should exclude `.DS_Store`, `__pycache__/`,
  `.ipynb_checkpoints/`, large raw-data extensions and local config
  ([GitHub's Python template](https://github.com/github/gitignore/blob/main/Python.gitignore)).
- **Unpublished data stays in private repos** until Lilo says it can be shared.

## 9. Code habits

Taken from [Taschuk & Wilson 2017](https://doi.org/10.1371/journal.pcbi.1005412),
[Sandve et al. 2013](https://doi.org/10.1371/journal.pcbi.1003285) and
[Rule et al. 2019](https://doi.org/10.1371/journal.pcbi.1007007):

- **Record the environment**: an `environment.yml` or `requirements.txt` with versions pinned for
  paper code. Packages use `pyproject.toml`
  ([Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)).
- **No hard-coded personal paths** (`C:\Users\yourname\...`, `/Users/yourname/...`). Use relative
  paths or a config file.
- **Notebooks**: clear outputs before committing (for example with
  [`nbstripout`](https://github.com/kynan/nbstripout)). Move reusable functions into `.py` modules.
- **Work through pull requests**, even on your own repo, for anything others use. Write commit
  messages that say *why*.
- **Dependabot and other bot PRs**: merge them or close them. Don't leave them piling up.
- Packages others install should have at least one test, run by GitHub Actions on every push.

## 10. Finishing: publication, archiving and leaving

**Archive, don't delete.** Archiving makes a repo read-only and keeps every URL working
([GitHub Docs: Archiving repositories](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories)).
Lilo archives:
- paper repos once the paper is published, the DOI is minted and nobody expects to change the code;
- any repo with no commits for 24 months, unless its maintainer says it's still in use.

**Before a repo is archived**, because an archived repo can't be changed:
1. Merge or close **every open pull request**, including Dependabot's.
2. Make the final release, and merge the DOI badge.
3. If another repo replaces it, put a line at the top of the README pointing to the replacement.

**Before you leave the group** (offboarding checklist):
- [ ] READMEs current: install steps work and the published paper is cited.
- [ ] Data deposited, with its DOI linked from the README.
- [ ] Final release tagged and the Zenodo DOI checked.
- [ ] A new maintainer named in the README, or the repo flagged to Lilo for archiving.
- [ ] Group repos in your personal account transferred to the org
      ([GitHub Docs: Transferring a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)).
- [ ] Open pull requests and branches merged or closed.

---

## Checklists

**New repo:** searched the org → Lilo approved → private, `main` branch → kebab-case name →
description and one category topic → README skeleton, LICENSE, `.gitignore` → Git identity set.

**Paper submission:** `CITATION.cff` validated, authors agreed with Lilo → Zenodo searched, then
enabled by Lilo → release `v1.0.0` → Zenodo record checked → version DOI in the paper's code
availability statement → badge in the README → Lilo makes the repo public.

**Paper published:** README, description and `CITATION.cff` updated to the published title, journal
and DOI → topic `paper` → tell Lilo (front page, and archiving when the work is done).

**Leaving:** the offboarding checklist in §10.

## Sources

- Barker M, et al. (2022). Introducing the FAIR Principles for research software. *Sci Data* 9: 622. https://doi.org/10.1038/s41597-022-01710-x
- Perez-Riverol Y, et al. (2016). Ten simple rules for taking advantage of Git and GitHub. *PLOS Comput Biol* 12: e1004947. https://doi.org/10.1371/journal.pcbi.1004947
- Rule A, et al. (2019). Ten simple rules for writing and sharing computational analyses in Jupyter Notebooks. *PLOS Comput Biol* 15: e1007007. https://doi.org/10.1371/journal.pcbi.1007007
- Sandve GK, et al. (2013). Ten simple rules for reproducible computational research. *PLOS Comput Biol* 9: e1003285. https://doi.org/10.1371/journal.pcbi.1003285
- Smith AM, Katz DS, Niemeyer KE, FORCE11 (2016). Software citation principles. *PeerJ Comput Sci* 2: e86. https://doi.org/10.7717/peerj-cs.86
- Taschuk M, Wilson G (2017). Ten simple rules for making research software more robust. *PLOS Comput Biol* 13: e1005412. https://doi.org/10.1371/journal.pcbi.1005412
- The Turing Way Community. *The Turing Way*. https://doi.org/10.5281/zenodo.3233853
- Wilkinson MD, et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Sci Data* 3: 160018. https://doi.org/10.1038/sdata.2016.18
- Wilson G, et al. (2017). Good enough practices in scientific computing. *PLOS Comput Biol* 13: e1005510. https://doi.org/10.1371/journal.pcbi.1005510
- Citation File Format: https://citation-file-format.github.io/
- GitHub Docs pages are linked inline above.
