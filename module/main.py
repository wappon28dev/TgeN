import os
import subprocess
from typing import Any

import questionary
from helpers.creation import Creation
from helpers.manifest import Langs, Manifest
from helpers.utils import Utils
from termcolor import colored

version: str = "0.0.1"

logo: str = rf"""
  _____          _   _
 |_   _|_ _  ___| \ | |
   | |/ _` |/ _ \  \| |
   | | (_| |  __/ |\  |
   |_|\__, |\___|_| \_|
      |___/      v{version}
"""

description: str = f"""\
Creation of templates for various projects
cwd: {colored(os.getcwd(), "yellow")}
--------------------------------\
"""


def getDirList() -> list[str]:
    dirList = next(os.walk("."))[1]
    if len(dirList) == 0:
        return []
    return dirList


def printDirList() -> None:
    dirList = Utils.get_localized_folder_names()
    if len(dirList) == 0:
        print("Directory is empty / ディレクトリ内は空です")
        return

    print(colored("## | フォルダー名", "dark_grey"))
    print(colored("--------------------------------", "dark_grey"))
    for i, dir in enumerate(dirList):
        lastIndex = i + 1
        lastIndex = str(i + 1).zfill(2)
        print(colored(f"{lastIndex} | {dir}", "dark_grey"))


def handleCancel(value: Any, message: list[str], assertion: bool) -> None:
    if value is None or not assertion:
        print(colored(f"{message[0]} is empty / {message[1]}が空です", "red"))
        print(colored("Canceled / キャンセルされました", "red"))
        exit(-1)


def main() -> None:
    print(colored(logo, "green"))
    print(description)
    printDirList()
    print(colored("--------------------------------\n", "dark_grey"))

    nextIndex: int = len(getDirList()) + 1
    pjName: str = questionary.text(  # type: ignore
        "Project Name / プロジェクトの名前 >",
        default=str(nextIndex).zfill(2) + "_",
    ).ask()

    handleCancel(
        value=pjName,
        message=["Project name", "プロジェクト名"],
        assertion=pjName != "",
    )

    if pjName in getDirList():
        print(colored("Project name already exists / プロジェクト名が既に存在します", "red"))
        print(colored("Canceled / キャンセルされました", "red"))
        return

    manifests = Utils.get_manifests_list()

    manifest: str = questionary.select(  # type: ignore
        "Manifest / マニフェスト >",
        choices=manifests,
    ).ask()

    handleCancel(
        value=manifest,
        message=["Manifest", "マニフェスト"],
        assertion=manifest != "",
    )

    lang: str = questionary.select(  # type: ignore
        "Language of directory name / フォルダー名の言語 >",
        choices=[lang.value for lang in Langs],
    ).ask()

    handleCancel(
        value=lang,
        message=["Language of directory name", "フォルダー名の言語"],
        assertion=lang != "",
    )

    callAsDir: bool = questionary.confirm(  # type: ignore
        "Call as directory / フォルダーの代わりにディレクトリと呼ぶ",
        default=False,
    ).ask()

    handleCancel(
        value=callAsDir,
        message=["Whether call as directory", "フォルダーの代わりにディレクトリと呼ぶか"],
        assertion=True,
    )

    print(colored("\ngenerating... / 生成中...\n", "yellow"))
    os.makedirs(pjName, exist_ok=True)
    target_path = os.path.join(os.getcwd(), pjName)

    Creation(
        target_path=target_path,
        manifest=Manifest(
            name=manifest,
            lang=Langs(lang),
            callAsDir=callAsDir,
        ),
    ).create()

    print(colored("\ndone / 完了", "green"))
    subprocess.Popen(["explorer", target_path], shell=True)
