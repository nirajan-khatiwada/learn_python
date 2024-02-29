
#using main package
# The code is importing the `main` module from the `MainPackage` package and then calling the
# `hello()` function from that module.
from MainPAckage import main
main.hello()

#using sub package
# The code is importing the `main` module from the `SubPackage` subpackage within the `MainPackage`
# package. It then calls the `hello()` function from that module.
from MainPAckage.SubPackage import main
main.hello()
#output
#importing main package
#used function main of mainpackage
#importing subpackage
#used function main of subpackage