import os

from .manifest import Langs, Manifest, Template
from .utils import Utils


class IniConfig:
    def __init__(
        self,
        manifest: Manifest,
        template: Template,
        target_path: str,
    ) -> None:
        self.manifest = manifest
        self.target_path = target_path
        self.template = template

        self.key = self.template.key
        self.desktop_ini_path = os.path.join(
            self.target_path,
            self.key,
            "desktop.ini",
        )

        if os.name != "nt":
            raise RuntimeError("This script is only for Windows / このスクリプトはWindowsのみ対応しています")

    def _get_new_config(self) -> str:
        icon_path = os.path.join(
            Utils.get_src_path(),
            "..",
            "assets",
            "manifests",
            self.manifest.name,
            "ico",
            f"{self.key}.ico",
        )

        meta = "[.ShellClassInfo]\n"
        meta += f"IconResource={icon_path}, 0\n"
        meta += f"InfoTip={self.template.meta['description']}\n"

        if self.manifest.lang != Langs.EN:
            l10n_dir_name = f"{self.template.meta['name']}"
            meta += f"LocalizedResourceName={self.key[:2]}_{l10n_dir_name}\n"
        return meta

    def write(self) -> None:
        file = open(self.desktop_ini_path, "x", encoding="shift-jis")
        file.write(self._get_new_config())
        os.system(f"attrib +s +h \"{self.desktop_ini_path}\"")
        file.close()

    def apply(self, key: str) -> None:
        os.chdir(os.path.join(self.target_path))
        os.system(f"attrib +s \"{key}\"")
