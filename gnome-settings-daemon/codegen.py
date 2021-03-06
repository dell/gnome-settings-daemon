#!/usr/bin/env python3

'''
FIXME

This script is used only to call gdbus-codegen and simulate the
generation of the source code and header as different targets.

Both are generated implicitly, so meson is not able to know how
many files are generated, so it does generate only one opaque
target that represents the two files.

Please see:
   https://bugzilla.gnome.org/show_bug.cgi?id=791015
   https://github.com/mesonbuild/meson/pull/2930
'''

import subprocess
import sys

name = 'org.gnome.' + sys.argv[1]

subprocess.call([
  'gdbus-codegen',
  '--interface-prefix=' + name + '.',
  '--generate-c-code=' + sys.argv[2],
  '--c-namespace=Gsd',
  '--annotate', name, 'org.gtk.GDBus.C.Name', sys.argv[1],
  '--output-directory=' + sys.argv[3],
  sys.argv[4]
])
