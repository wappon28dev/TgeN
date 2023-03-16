import os

from tqdm import tqdm

from helpers.ini_config import IniConfig
from helpers.manifest import Manifest


class Creation:
    def __init__(self, target_path: str, manifest: Manifest):
        self.base_path = target_path
        self.manifest = manifest

    def create(self):
        for template in tqdm(self.manifest.get_templates_list()):
            os.makedirs(os.path.join(self.base_path, template.key), exist_ok=True)
            config = IniConfig(
                manifest=self.manifest,
                template=template,
                target_path=self.base_path,
            )
            config.write()
            config.apply(key=template.key)
