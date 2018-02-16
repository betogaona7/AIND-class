"""Reading in text files."""
import glob

def read_file(filename):
    """Read a plain text file and return the contents as a string."""
    with open(filename, "r") as file:
        content = file.read()
    return content


def read_files(path):
    """Read all files that match given path and return a dict with their contents."""
    files = {}
    # Get a list of all files that match path
    for file in glob.glob(path):
        content = read_file(file)
        files[file[5:]] = content
    return files


def test_run():
    # Test read_file()
    print(read_file("data/hieroglyph.txt"))
    
    # Test read_files()
    texts = read_files("data/*.txt")
    for name in texts:
        print("\n***", name, "***")
        print(texts[name])


if __name__ == '__main__':
    test_run()