Snaps are packages: https://snapcraft.io

Snaps for duplicity should be built from releases of duplicity,
after dist/makedist has been run on the files.

To build a snap, in the root of the project, type:
SNAPCRAFT_BUILD_INFO=y snapcraft
