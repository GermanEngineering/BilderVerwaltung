import math


def PrintProgress(numberOfProcessedFiles):
    if numberOfProcessedFiles == 1:
        print("""
            __ \ / __
           /  \ | /  \\
               \|/
/\__/\   ,------v--_
\_  _/  /           \\
 \ \__|         o  __|
  \                \_
   \      ,_/       /""")

    progress = numberOfProcessedFiles - (math.floor(numberOfProcessedFiles/24) * 24)
    print("{0}{1} Processed Files: {2}".format((24 - progress) * " ", progress * "~", numberOfProcessedFiles), end="\r")
