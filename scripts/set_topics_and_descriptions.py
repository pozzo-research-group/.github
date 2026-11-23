"""Step 1.3 and 1.4: add category topics and fill in missing one-line descriptions
for repositories in github.com/pozzo-research-group.

Requires the GitHub CLI (https://cli.github.com), logged in as an org owner:
    gh auth login

Dry run (prints the commands, changes nothing):
    python set_topics_and_descriptions.py
Apply:
    python set_topics_and_descriptions.py --apply

Topics are ADDED (`gh repo edit --add-topic`), so existing topics such as
"papers" are kept. Edit DESCRIPTIONS below before running with --apply.
Ghost repos flagged for deletion are skipped.
"""
import subprocess
import sys

ORG = "pozzo-research-group"

# repo: [category topic(s) + extra topics]   (plan Appendix A)
TOPICS = {
    # Analysis, modeling & data management
    "MC-DFM": ["analysis", "saxs", "sans", "monte-carlo", "protein-assembly"],
    "autophasemap": ["analysis", "paper", "phase-mapping", "uv-vis"],
    "activephasemap": ["analysis", "phase-mapping", "active-learning"],
    "saxs_data_processing": ["analysis", "saxs"],
    "pispis": ["analysis", "data-management", "saxs", "nexus"],
    "theia": ["analysis", "data-management", "saxs", "nexus", "nomad"],
    "micelles": ["analysis", "sans", "form-factors"],
    "bayesian-optimization-tools": ["analysis", "bayesian-optimization"],
    "designspacediscovery": ["analysis", "cheminformatics"],
    "hardy": ["analysis", "machine-learning"],
    "AnalySAS": ["analysis", "saxs", "sans"],
    # Lab automation & open hardware
    "phasIR": ["automation", "open-hardware", "thermal-analysis", "infrared"],
    "Automation-Hardware": ["automation", "open-hardware", "labware", "3d-printing"],
    "OT2-DOE": ["automation", "opentrons", "high-throughput"],
    "digital_pipette_server": ["automation", "open-hardware", "jubilee", "self-driving-lab"],
    "bo-serving": ["automation", "bayesian-optimization", "self-driving-lab"],
    "OT2-ADT": ["automation", "opentrons", "membranes"],
    "AFL-sample-loader": ["automation", "saxs", "self-driving-lab"],
    "science_jubilee": ["automation", "open-hardware", "jubilee", "self-driving-lab"],
    "sonication_station": ["automation", "open-hardware", "jubilee", "sonochemistry"],
    "otto": ["automation", "opentrons", "nanoparticles"],
    "OT2_silica_synthesis": ["automation", "opentrons", "nanoparticles"],
    "OT2Protocols": ["automation", "opentrons"],
    "OLD-OT2Protocols": ["automation", "opentrons"],
    "Ball-Mill-Mechanoredox": ["automation", "open-hardware", "jubilee"],
    # Papers & research projects
    "papers": ["paper"],
    "HEAD": ["paper", "bayesian-optimization", "nanoparticles"],
    "silica_lipid_DNA": ["paper", "hoomd", "self-assembly"],
    "automated-mesoporous-silica": ["paper", "saxs", "self-driving-lab", "jubilee"],
    "c-wolf-blends-morphology": ["paper", "sans", "waxs", "polymers"],
    "des-basis-set": ["paper", "deep-eutectic-solvents", "high-throughput"],
    "RhuA_SAXS_Modeling": ["paper", "saxs", "protein-assembly"],
    "silica-np-synthesis": ["project", "self-driving-lab", "nanoparticles", "jubilee"],
    "gel-reaction-diffusion": ["project", "jubilee", "hydrogels"],
    "Polymer_drop_casting": ["project", "jubilee", "polymers"],
    # Teaching, demos & community
    "jubilee_pipette_BOdemo": ["teaching", "jubilee", "bayesian-optimization"],
    "colormixdemo": ["teaching", "jubilee"],
    "OT2-Course-MSE": ["teaching", "opentrons"],
    "MRSFall23": ["teaching", "functional-data-analysis"],
    "ML4MS2024_tutorials": ["teaching", "jubilee", "bayesian-optimization"],
    # Private repos (not shown to visitors). Checked against their READMEs on 23 Nov 2026.
    # nomad-oasis and Moeez_Brenden_MRS24 are left out: they are to be archived (plan 2.3).
    "IOCs": ["automation", "open-hardware"],
    "OT2_DCSP": ["automation", "opentrons", "membranes"],
    "nomad-oasis-ferry": ["analysis", "data-management", "nomad"],
}

# Missing one-line descriptions: DRAFTS, edit before --apply.
# Leave a value as "" to skip that repo.
DESCRIPTIONS = {
    "AnalySAS": "Python package for processing, analysis and modeling of small-angle scattering data",
    "OT2-DOE": "Python modules and notebooks for design of experiments and high-throughput sample preparation and analysis with the Opentrons OT-2",
    "theia": "Tools and a NOMAD Oasis plugin for converting SAXS and UV-Vis data to NeXus (NXcanSAS) files",
    "silica-np-synthesis": "Automated silica nanoparticle synthesis: sampling and optimization rounds with SAXS analysis",
    "digital_pipette_server": "Raspberry Pi server that drives the Digital Pipette syringe tool for Science Jubilee",
    "Polymer_drop_casting": "Drop-casting polymer films in 48-well plates with Science Jubilee",
    "automated-mesoporous-silica": "Code for the paper 'Open-hardware automation platform for accelerated sol-gel nanomaterial synthesis'",
    # Private repo (description written by Lilo)
    "nomad-oasis-ferry": "NOMAD Oasis Ferry is a Python package and command-line tool for automatically monitoring, pairing, and uploading SAXS and UV-Vis files to a NOMAD Oasis instance.",
}


def run(cmd, apply):
    print(("RUN  " if apply else "DRY  ") + " ".join(cmd))
    if apply:
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0:
            print("     FAILED:", r.stderr.strip())
            return False
    return True


def main():
    apply = "--apply" in sys.argv
    failed = []
    for repo in sorted(set(TOPICS) | set(DESCRIPTIONS), key=str.lower):
        cmd = ["gh", "repo", "edit", f"{ORG}/{repo}"]
        if TOPICS.get(repo):
            cmd += ["--add-topic", ",".join(TOPICS[repo])]
        if DESCRIPTIONS.get(repo):
            cmd += ["--description", DESCRIPTIONS[repo]]
        if len(cmd) > 4 and not run(cmd, apply):
            failed.append(repo)
    print(f"\n{'Applied' if apply else 'Dry run'}; failures: {failed or 'none'}")


if __name__ == "__main__":
    main()
