import os

# helpful computer system programs using os

# directory tree
#/Users/nickellingson/Documents/2025/algo_a_day/python/scripts
os.chdir("/Users/nickellingson/Documents")

# list all of the files
def list_files():
    for _, _, filenames in os.walk("."):
        print(filenames)


# build tree
path = "."
def build_tree(path, indent=""):
    try:
        files_and_dirs = sorted(os.listdir(path))
    except:
        print("unauthorized")
        return
    for index, name in enumerate(files_and_dirs):
        full_path = os.path.join(path, name)
        connector = "|--" if index == len(files_and_dirs) -1 else "|--"
        print(f"{indent}{connector} {name}")

        if os.path.isdir(full_path):
            sub_indent = "    " if index == len(files_and_dirs) -1 else "| "
            build_tree(full_path, indent + sub_indent)


# disk usage
def get_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size





if __name__=="__main__":
    # get tree
    # root_dir = "."
    # build_tree(root_dir)

    size = get_size(".")
    print(f"Total size: {size} bytes (~{size/1024/1024:.2f} MB)")