#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from destination_stdout import DestinationStdout

if __name__ == "__main__":
    DestinationStdout().run(sys.argv[1:])
