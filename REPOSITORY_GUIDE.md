# Working with GitHub in the pozzo-research-group organization

*For students, postdocs and visitors who create or maintain repositories in
[github.com/pozzo-research-group](https://github.com/pozzo-research-group). Read it when you join,
and again when you start a repository, submit a paper, publish, and leave the group.*

Papers print our repository links, and other groups use our tools, often years after the author
has left. The rules below keep those links working, keep credit with the right people, and make
each repository usable by whoever comes next. They follow established practice for research
software (see [Sources](#sources)).

**When in doubt, ask Lilo before you act.**

---

## 1. Who does what

| Action | Who |
|---|---|
| Create, rename, transfer, archive or delete a repository | **Lilo** (ask her; she does it or tells you to) |
| Make a private repository public | **Lilo**, after the checks in §2 |
| Connect a repository to Zenodo | **Lilo** |
| Pin repositories and edit the organization front page | **Lilo** |
| Everything inside your repository: code, README, LICENSE, `CITATION.cff`, description, topics, releases | **You**, the maintainer |

Every active repository has one named **maintainer**, listed in its README. That's usually the
person who started it. The maintainer changes when that person leaves (§10).

## 2. Starting a repository

1. **Search pozzo-research-group first.** If an existing repository covers your work, add to it (a
   branch, a folder or a pull request) instead of starting a parallel one.
2. **Ask Lilo** to create the repository in pozzo-research-group, or for permission to create it
   yourself. Group work never lives in a personal account. A personal fork for day-to-day work is
   fine.
3. **Start private.** A repository stays private until it has a README and a LICENSE, and nothing
   unpublished is in it. Lilo makes it public, usually at paper submission or publication.
4. **Create it when there is content.** Don't create empty placeholder repositories.
5. **Set your Git identity** on every computer you commit from, so commits are credited to you:
   ```
   git config --global user.name "Your Name"
   git config --global user.email "ID+username@users.noreply.github.com"
   ```
   Your noreply address is under GitHub → Settings → Emails
   ([GitHub Docs: Setting your commit email address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)).
6. Use **`main`** as the default branch.

### Naming

- New repositories use **lowercase kebab-case**: `saxs-data-processing`, not
  `SAXS_Data_Processing` or `saxsDataProcessing`. The Python package inside keeps a snake_case
  import name ([PEP 8](https://peps.python.org/pep-0008/#package-and-module-names)).
- The name says what the repository contains: `jubilee-pipette-tool`, `rhua-saxs-modeling`. Avoid
  personal names, conference names and dates unless the repository really is a one-off. One-offs
  are archived when they're done (§10).
- **Don't make copies such as "OLD-" or "-v2".** Old versions live in the Git history, tags and
  releases. A copy splits issues, stars and citations across two repositories.
- **Don't rename existing repositories.** GitHub redirects a renamed repository only until another
  repository takes the old name
  ([GitHub Docs: Renaming a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository)).
  A repository cited in a paper is never renamed, moved or deleted, and the folder paths inside it
  stay where they are.

## 3. Description and topics

Every repository needs both. The organization front page and GitHub search depend on them.

- **Description:** one plain sentence saying what the repository contains. Keep it current. Once a
  paper is published, give its published title and journal.
- **Topics:** the maintainer sets them. Use exactly one **category topic**, plus a few specific ones
  ([GitHub Docs: Classifying your repository with topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)):

| Category | Category topic | Example extra topics |
|---|---|---|
| Analysis, modeling & data management | `analysis` (add `data-management` if relevant) | `saxs`, `sans`, `nexus`, `bayesian-optimization` |
| Lab automation & open hardware | `automation` (add `open-hardware` if relevant) | `jubilee`, `opentrons`, `3d-printing` |
| Papers & research projects | `paper` (published) or `project` (ongoing) | `nanoparticles`, `polymers`, `hydrogels` |
| Teaching, demos & community | `teaching` | `jubilee`, `bayesian-optimization` |

Add `jubilee` to anything built on Science Jubilee, and `opentrons` to anything for the OT-2. When a
repository is new, changes category or is archived, tell Lilo so the front page is updated.

## 4. README

GitHub shows the README first, so write it for someone who has never met you. Cover, in this order
([Wilson et al. 2017](https://doi.org/10.1371/journal.pcbi.1005510);
[The Turing Way](https://book.the-turing-way.org/project-design/project-repo/project-repo-readme)):

1. **What this is**, in one paragraph.
2. **Paper and DOI**, if any: the published title, linked to the paper's DOI, and the DOI badge for
   the code (§7).
3. **Install**: the exact commands, starting from a fresh environment.
4. **Minimal example**: one command or a short notebook that runs in a few minutes.
5. **Data**: where it lives (a DOI, §8) and how to get it.
6. **Maintainer**, and how to report problems (GitHub Issues).
7. **How to cite**: "see `CITATION.cff`" is enough.

Keep it true:
- Remove badges for services that no longer run.
- Delete placeholder text left by project generators.
- When a paper is published, replace "submitted" or working titles with the published citation.
- If the repository is a fork, say so at the top (§6).

## 5. License

Without a LICENSE file, a repository is "all rights reserved" and nobody can legally reuse it
([GitHub Docs: Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)).
Put the license text in a file named `LICENSE` at the top of the repository.

- **New repositories use a standard open-source license:**
  [MIT](https://choosealicense.com/licenses/mit/) or
  [BSD-3-Clause](https://choosealicense.com/licenses/bsd-3-clause/). These are the licenses of the
  scientific Python tools we build on (NumPy, SciPy, scikit-learn), and they let anyone reuse the
  work with credit ([Morin et al. 2012](https://doi.org/10.1371/journal.pcbi.1002598)).
- **Repositories that already have CC BY-NC-SA 4.0 keep it.** Don't change an existing license
  without asking Lilo.
- If the repository has a `pyproject.toml`, the license declared there must match the LICENSE file.
- **Forks keep the upstream license.** Never relicense someone else's code.
- For work under a sponsored-research or IP agreement, ask Lilo before choosing a license.

## 6. Forks and outside code

- Fork into pozzo-research-group only when the group **contributes to or depends on** that project.
  Say at the top of the README that it's a fork, link the original, and list the group's changes.
- Don't fork reading lists, "awesome" lists or other projects just to keep a copy. Star them instead.
- A repository made from someone else's template ("Use this template") isn't counted as a fork by
  GitHub, so credit the original in the README yourself.

## 7. Citation, releases and DOIs

Software is a research output and should be cited like one
([Smith et al. 2016](https://doi.org/10.7717/peerj-cs.86);
[Barker et al. 2022](https://doi.org/10.1038/s41597-022-01710-x)).

### `CITATION.cff`

Every repository tied to a paper, and every package, has a `CITATION.cff` at the top. GitHub then
shows a **"Cite this repository"** button
([GitHub Docs: About CITATION files](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)),
and Zenodo copies the authors into the DOI record. Get it right before the first release:

```yaml
cff-version: 1.2.0
message: "If you use this software, please cite it as below."
title: "repository-name"
authors:
  - family-names: "Surname"             # surname only
    given-names: "First M."             # first and middle names or initials
    orcid: "https://orcid.org/0000-0000-0000-0000"
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
    name: "Publisher name"              # an object, not a plain string
  authors: [ ... ]
```

- **Authors are the people who wrote the software.** They may differ from the paper's author list.
  Agree on the list with Lilo.
- **Split names correctly.** Particles and middle names go in `given-names`. `family-names` holds
  only the surname.
- **Add ORCIDs** for everyone who has one.
- **Validate before you commit:**
  ```
  pip install cffconvert
  cffconvert --validate
  ```
  If the file is invalid, Zenodo may ignore it.
- Format reference: [citation-file-format.github.io](https://citation-file-format.github.io/).

### Releases and Zenodo DOIs

pozzo-research-group is connected to [Zenodo](https://zenodo.org). Once Lilo enables a repository,
each GitHub release is archived and gets a DOI
([GitHub Docs: Referencing and citing content](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content)).

1. **Search [zenodo.org](https://zenodo.org) for the repository name** before asking Lilo to enable
   it. If a record exists, keep using it. A second record splits citations and can't be merged.
2. **Release when you submit the paper:** GitHub → Releases → *Draft a new release*. Tag it `v1.0.0`
   ([semantic versioning](https://semver.org/)) and write a sentence on what the release is. Increase
   the version for every later release.
3. **Check the Zenodo record:** title, authors and spelling. If something is wrong, fix
   `CITATION.cff` and release again.
4. **In the paper**, cite the **version DOI** of the exact release used, with the GitHub URL as a
   second link. A DOI keeps working even if the repository moves.
5. **In the README**, add the badge for the **concept DOI**, which always resolves to the newest
   version:
   ```
   [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.NNNNNNN.svg)](https://doi.org/10.5281/zenodo.NNNNNNN)
   ```
6. If a repository has a `.zenodo.json`, Zenodo uses it instead of `CITATION.cff`. Keep only one of
   the two.

## 8. Data, large files and secrets

Git keeps every version of every file forever. Large files slow down every clone, and removing them
means rewriting history, which changes commit hashes that papers may cite.

- **GitHub limits:** it warns at 50 MiB per file and blocks files over 100 MiB. Repositories should
  ideally stay under 1 GB
  ([GitHub Docs: About large files](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)).
- **Raw and large data go to a data repository**, usually Zenodo, with its own DOI. Put that DOI in
  the README and download the data with a small script
  ([Wilson et al. 2017](https://doi.org/10.1371/journal.pcbi.1005510);
  [Wilkinson et al. 2016](https://doi.org/10.1038/sdata.2016.18)). For SAXS and UV-Vis data, the
  group's NeXus and NOMAD tools are the longer-term home.
- **Keep only small example or test data in Git**, a few MB in total, in `data/` or `tests/data/`.
- **Never commit** passwords, API tokens, instrument credentials or `.env` files. If one is
  committed by mistake, revoke it right away and tell Lilo: deleting the file doesn't remove it from
  the history.
- **Add a `.gitignore` from the start.** Exclude `.DS_Store`, `__pycache__/`,
  `.ipynb_checkpoints/`, raw-data file types and local configuration
  ([GitHub's Python template](https://github.com/github/gitignore/blob/main/Python.gitignore)).
- **Unpublished data stays in private repositories** until Lilo says it can be shared.

## 9. Code habits

Based on [Taschuk & Wilson 2017](https://doi.org/10.1371/journal.pcbi.1005412),
[Sandve et al. 2013](https://doi.org/10.1371/journal.pcbi.1003285),
[Rule et al. 2019](https://doi.org/10.1371/journal.pcbi.1007007) and
[Perez-Riverol et al. 2016](https://doi.org/10.1371/journal.pcbi.1004947):

- **Record the environment:** an `environment.yml` or `requirements.txt`, with versions pinned for
  paper code. Packages use `pyproject.toml`
  ([Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)).
- **No hard-coded personal paths** (`C:\Users\yourname\...`, `/Users/yourname/...`). Use relative
  paths or a configuration file.
- **Notebooks:** clear outputs before committing (for example with
  [`nbstripout`](https://github.com/kynan/nbstripout)), and move reusable functions into `.py`
  modules.
- **Use pull requests** for changes to anything others use, even in your own repository. Write
  commit messages that say *why*.
- **Bot pull requests** (Dependabot and similar): merge or close them promptly.
- **Packages others install** have at least one test, run by GitHub Actions on every push.

## 10. Publication, archiving and leaving

**Archive, don't delete.** Archiving makes a repository read-only and keeps every URL working
([GitHub Docs: Archiving repositories](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories)).
Lilo archives:
- paper repositories once the paper is published, the DOI is minted and nobody expects to change
  the code;
- any repository with no commits on its default branch for **24 months**, unless its maintainer
  says it's still in use.

**Before a repository is archived** (an archived repository can't be changed):
1. Merge or close every open pull request, including bot pull requests.
2. Make the final release and add the DOI badge.
3. Update the README and description to the published paper.
4. If another repository replaces it, put a line at the top of the README pointing to the
   replacement.

**Before you leave the group:**
- [ ] READMEs are current: the install steps work and the published paper is cited.
- [ ] Data is deposited, with its DOI linked from the README.
- [ ] Final release tagged and the Zenodo record checked.
- [ ] A new maintainer is named in the README, or the repository is flagged to Lilo for archiving.
- [ ] Group repositories in your personal account are transferred to pozzo-research-group
      ([GitHub Docs: Transferring a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)).
- [ ] Open pull requests and branches are merged or closed.

---

## Checklists

**New repository:** searched pozzo-research-group → Lilo approved → private, `main` branch →
kebab-case name → description and one category topic → README, MIT or BSD-3-Clause LICENSE,
`.gitignore` → Git identity set.

**Paper submission:** `CITATION.cff` validated, authors agreed with Lilo → Zenodo searched, then
enabled by Lilo → release `v1.0.0` → Zenodo record checked → version DOI in the paper's
code-availability statement → badge in the README → Lilo makes the repository public.

**Paper published:** README, description and `CITATION.cff` updated to the published title, journal
and DOI → topic `paper` → tell Lilo (front page, and archiving once the work is finished).

**Leaving:** the checklist in §10.

## Sources

- Barker M, et al. (2022). Introducing the FAIR Principles for research software. *Sci Data* 9: 622. https://doi.org/10.1038/s41597-022-01710-x
- Morin A, Urban J, Sliz P (2012). A quick guide to software licensing for the scientist-programmer. *PLOS Comput Biol* 8: e1002598. https://doi.org/10.1371/journal.pcbi.1002598
- Perez-Riverol Y, et al. (2016). Ten simple rules for taking advantage of Git and GitHub. *PLOS Comput Biol* 12: e1004947. https://doi.org/10.1371/journal.pcbi.1004947
- Rule A, et al. (2019). Ten simple rules for writing and sharing computational analyses in Jupyter Notebooks. *PLOS Comput Biol* 15: e1007007. https://doi.org/10.1371/journal.pcbi.1007007
- Sandve GK, et al. (2013). Ten simple rules for reproducible computational research. *PLOS Comput Biol* 9: e1003285. https://doi.org/10.1371/journal.pcbi.1003285
- Smith AM, Katz DS, Niemeyer KE, FORCE11 (2016). Software citation principles. *PeerJ Comput Sci* 2: e86. https://doi.org/10.7717/peerj-cs.86
- Taschuk M, Wilson G (2017). Ten simple rules for making research software more robust. *PLOS Comput Biol* 13: e1005412. https://doi.org/10.1371/journal.pcbi.1005412
- The Turing Way Community. *The Turing Way*. https://doi.org/10.5281/zenodo.3233853
- Wilkinson MD, et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Sci Data* 3: 160018. https://doi.org/10.1038/sdata.2016.18
- Wilson G, et al. (2017). Good enough practices in scientific computing. *PLOS Comput Biol* 13: e1005510. https://doi.org/10.1371/journal.pcbi.1005510
- GitHub Docs pages are linked inline.
