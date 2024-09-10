## Avant-propos
This project is based on [jhdeov's interlingual-MFA project](https://github.com/jhdeov/interlingual-MFA), which is licensed under the GNU General Public License (GPL). While some of the code and files (created by YuDZEN) are original, the majority of the project retains jhdeov’s copyright. For any inquiries, particularly regarding commercial use or licensing, please contact jhdeov !

By using or modifying this project, you agree to comply with the terms of the GPL, which governs the original project.

## Introduction
This project aims to use an English MFA acoustic model to align the phonemes of the Korebaju language. Please follow the instructions below if you wish to use it.

## Before You Begin
Ensure that MFA (Montreal Forced Aligner) is installed and running on your system. You can find installation instructions here: [MFA Getting Started Guide](https://montreal-forced-aligner.readthedocs.io/en/latest/getting_started.html).

You will also need to have Python installed on your PC, along with several required libraries. It is recommended to review each Python script in this project to ensure all necessary libraries are installed (for example, in VSCode, missing libraries will be indicated within the script).

## Alignment Procedure
Place the corpus you want to transcribe into the `corpus/` folder. Each audio file (`.wav`) should have a corresponding TextGrid file (`.textgrid`) with the same name. For example:
```
file1.wav
file1.textgrid
file2.wav
file2.textgrid
...
```
For the TextGrid file, ensure that it contains a single tier named `word`, where the transcript of the Korebaju words should be placed within the intervals. You can refer to the example in the `example/` folder.


Once the files are in place, you can run the script from the main folder by executing:
```bash
./run.sh # for linux/mac system, if you use a Windows, you might need to change the script, but the logic remains the same
```
After the alignment is completed, you will find the results in the `output/` folder.