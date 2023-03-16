import json
import os
from enum import Enum
from typing import List, NamedTuple, TypedDict

from .utils import Utils


class Langs(Enum):
    JA = "ja"
    EN = "en"


class Meta(TypedDict):
    name: str
    description: str


class Template(NamedTuple):
    key: str
    meta: Meta


class Manifest:
    def __init__(self, name: str, lang: Langs, callAsDir: bool) -> None:
        self.lang = lang
        self.callAsDir = callAsDir
        self.name = name

    def _get_dir_called_with(
        self,
        i18n_data: dict[str, dict[str, str]],
    ) -> str:
        if self.callAsDir:
            return i18n_data["dirCalledWith"]["directory"]
        else:
            return i18n_data["dirCalledWith"]["folder"]

    def _get_templates(self) -> dict[str, Meta]:
        manifest_path = os.path.join(
            Utils.get_src_path(),
            "..",
            "assets",
            "manifests",
            self.name,
            "manifest.json",
        )
        with open(manifest_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        i18n_data = data[self.lang.value]
        dir_called_with = self._get_dir_called_with(i18n_data)
        replaced_data = json.dumps(i18n_data).replace("{dir}", dir_called_with)

        return json.loads(replaced_data)["templates"]

    def get_templates_list(self) -> List[Template]:
        templates = self._get_templates()
        return [Template(*tpl) for tpl in templates.items()]

    def get_selected_template(self, template_name: str) -> Template:
        templates = self._get_templates()

        if template_name not in templates:
            raise ValueError(f"No template found with name '{template_name}'.")

        return Template(template_name, templates[template_name])
