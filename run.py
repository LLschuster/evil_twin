import sys, os
gamepath = os.path.abspath(os.path.dirname(sys.argv[0]))
sys.path.append(gamepath)
sys.path.append(os.path.join(gamepath, "code"))

import main

main.main(gamepath)