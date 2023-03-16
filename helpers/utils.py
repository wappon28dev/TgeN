import os


class Utils:
    @staticmethod
    def get_src_path() -> str:
        return os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def get_localized_folder_name(folder_name: str) -> str:
        desktop_ini_path = os.path.join(folder_name, "desktop.ini")

        if os.path.exists(desktop_ini_path):
            with open(desktop_ini_path, encoding="shift-jis") as f:
                for line in f:
                    if line.startswith("LocalizedResourceName="):
                        return line.split("=")[1].strip()

        return folder_name

    @staticmethod
    def get_localized_folder_names() -> list[str]:
        folder_names: list[str] = []

        for folder in os.scandir("."):
            if folder.is_dir() and folder.name != "__pycache__":
                folder_names.append(
                    Utils.get_localized_folder_name(folder.name),
                )

        return folder_names

    @staticmethod
    def get_manifests_list() -> list[str]:
        return [
            manifest.name
            for manifest in os.scandir(
                os.path.join(Utils.get_src_path(), "..", "assets", "manifests"),
            )
            if manifest.is_dir()
        ]
