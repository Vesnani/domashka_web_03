import os
import shutil
from threading import Thread


class FolderProcessor(Thread):
    def __init__(self, folder_path):
        super().__init__()
        self.folder_path = folder_path

    def sort_files_in_folder(self, folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                _, file_ext = os.path.splitext(file)
                dest_folder = os.path.join(folder_path, file_ext[1:])
                os.makedirs(dest_folder, exist_ok=True)

                if os.path.exists(file_path):
                    dest_path = os.path.join(dest_folder, file)
                    shutil.move(file_path, dest_path)

    def run(self):
        self.sort_files_in_folder(self.folder_path)


if __name__ == "__main__":
    folder_path = input('Введіть шлях до папки: ')
    if not os.path.exists(folder_path):
        print('Папки не існує!')
    else:
        folder_processor = FolderProcessor(folder_path)
        folder_processor.start()
        folder_processor.join()
        print('Сортування завершено!')
