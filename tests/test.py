import normalize_md
import rename_files

if __name__ == '__main__':
    # replace the directory you want to rename
    target_directory = r"D:\Desktop\awesome-notes"
    normalize_md.process_dir(target_directory)

    # replace the directory you want to rename
    directory_path = r"D:\Desktop\C++"
    rename_files.rename(directory_path, "Mathematics Competition", "jpg")