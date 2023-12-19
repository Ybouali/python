import sys

try:
    from importlib import metadata
except ImportError:
    import importlib_metadata as metadata

try:
    import numpy as np
except ImportError:
    print("ERROR: to run this script u should be installed numpy")

try:
    print("Info: The first argument should be the package name")
    print("Info: The secound argument should be (metadata) Or (listFiles)")
    print("Info: metadata if u wanna show the metadata for the package")
    print("Info: listFiles if u wanna show the list of files")

    # check if the package name is not provided
    if (len(sys.argv) == 2):
        raise ValueError("Please provide a package name and a \
                            option read the info above")
    packageName = sys.argv[1]

    print("Check if the package is installed ...\n")

    # check if the package is installed
    try:
        __import__(packageName)
        print("Nice! package %s is installed\n" % packageName)
    except ImportError:
        raise ImportError("No such package name: %s" % packageName)

    # show the list files
    if (len(sys.argv) == 3 and sys.argv[2] == "listFiles"):

        # get the list of file paths for the specified distribution.

        paths = metadata.files(packageName)

        for i in range(len(paths)):
            print(paths[i])

    # show the metadata
    if (len(sys.argv) == 3 and sys.argv[2] == "metadata"):

        # get the metadata from the name package
        sp_data = metadata.metadata(packageName)

        # show the metadata
        for data in sp_data:
            print(data + ": " + sp_data[data])

except Exception as e:
    print("ERROR: %s" % e)
