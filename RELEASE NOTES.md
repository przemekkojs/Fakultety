# RELEASE NOTES
Detailed descriptions of each release. Also contains future releases!

## [1.0] - 22.09.2024
**Release date:** 22.09.2024

### Summary
This release provides the first stable version of the project.

### Features
- Working desktop app
- Filtering by necessary values
- Details window
- Polish language version, with an option to translate it, by just adding one python class to the *dictionary.py* file

### Environment
- Developed and tested on: Windows 10
- Python: 3.11.4 64-bit

## [1.0.1] - 23.09.2024
**Release date:** 23.09.2024

### Summary
This version mainly solved issue with paths.

### New features
- Paths issues are solved
- .exe file is now avaiable for download

## [1.0.2] - 30.09.2024
**Release date:** 30.09.2024

### Summary
This version focused on upgrading filtering logic. Also, the file was changed to the one for the current semester.

### New features
- Update of filtering by course name and teacher name - using contains, not equality.
- Changed file to valid one (2024/2025)

## [1.1.0] - 01.10.2024
**Release date:** 01.10.2024

### Summary
This version is a major upgrade - I'm planning on developing also a web and mobile app. Also, styling was added. It'll be changed to match [The Karol Lipiński Academy of Music Wroclaw](https://amuz.wroc.pl/) website.

### New features
- Added directories for future app versions - mobile and web
- Basic styling (dark mode)
- Added menu with an option to load a database
- Added *RELEASE NOTES.md* and *CHANGELOG.md* files, for better clarity.

## [1.1.1] - 01.10.2024

### Summary
This version makes ui coherent with the [website](https://amuz.wroc.pl/).

### New features
- UI coherent with the Academy website
- Web folders structure

## [1.2] - 03.10.2024

### Summary
This version created fully working website, which behaves just like the desktop version.

### New features
- Minor corrections in the desktop app
- Fully working web app
- Deployment scripts
- Setting up GitHub pages
- Matching results count

**[1.2.1] - 04.10.2024**

### Summary
This version fixes several minor bugs, like addidional pass info not displaying correctly in the web version. Also, styling for mobile devices was added.

### New features
- Fixed bugs
- Filtering is now not-case-sensitive - characters do not neet to be capitalized correctly for filtering to work

## [1.3.0] - 04.11.2024 - preview

### Summary
This will be a major leap - Academy agreed to collaborate and prepare files with a new format. With this being said, new .csv file format is coming and making loading multiple files will now be possible.

Additional new ideas include:
- Sorting by fields (probably 1.4)
- Filtering fields to display in table (probably 1.5)

So, I want to say *thank You* to Wroclaw Karol Lipiński' Academy of Music for everything and - from now on - new part of work begun.

I'm also thinking about switching to TypeScript, for better scaling, code understanding and support for possible collaborators.