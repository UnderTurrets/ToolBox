import normalize_md
import rename_files

if __name__ == '__main__':
    # replace the directory you want to rename
    target_directory = r"D:\Desktop\awesome_notes\note_offline"
    normalize_md.process_dir(target_directory)
