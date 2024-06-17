import os
import subprocess

projects = ["control-station-installation", "template", "database-ingestion"]

for project in projects:
    working_directory = f"src/dacs-sw/{project}"
    root_file = "main.tex"
    command = [
        "docker",
        "run",
        "--rm",
        "-v",
        f"{os.environ['GITHUB_WORKSPACE']}:/workspace",
        "-w",
        f"/workspace/{working_directory}",
        "texlive/texlive:latest",
        "latexmk",
        "-pdf",
        "-interaction=nonstopmode",
        root_file,
    ]
    subprocess.run(command, check=True)
