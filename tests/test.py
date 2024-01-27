import pythonSmallToolsByHanXu.normalize_md as norm_md
import pythonSmallToolsByHanXu.rename_files

if __name__ == '__main__':
    # replace the directory you want to rename
    target_directory = r"/home/han/Desktop/MD_notes（复件）/online"
    norm_md.normalizer(target_directory)()
