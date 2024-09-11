#!/bin/bash

python clean.py
# define the path of the corpus directory
CORPUS_DIRECTORY="./corpus/"
PHONE_MAPPING_FILE="./phoneMapping.txt"
ORIGIN_PRON_DICT_FILE="./output.txt"
INTER_PRON_DICT_FILE="./inter_pron_dict.txt"
OUTPUT_DIRECTORY="./output"

python star2replacement.py "$CORPUS_DIRECTORY" "$PHONE_MAPPING_FILE" "$ORIGIN_PRON_DICT_FILE"

python convertPronDict.py "$ORIGIN_PRON_DICT_FILE" "$PHONE_MAPPING_FILE" "$INTER_PRON_DICT_FILE" || { echo "convertPronDict.py failed"; exit 1; }



if [ ! -d "$OUTPUT_DIRECTORY" ]; then
    mkdir -p "$OUTPUT_DIRECTORY"
fi

# use MFA to align the corpus
mfa validate --single_speaker --num_jobs=4 "$CORPUS_DIRECTORY" "$INTER_PRON_DICT_FILE" english_mfa.zip
mfa align --single_speaker --num_jobs=4 "$CORPUS_DIRECTORY" "$INTER_PRON_DICT_FILE" english_mfa.zip "$OUTPUT_DIRECTORY"
pip install tgt
# convert the result
python convertAlignments.py wordTranscriptions.pkl "$OUTPUT_DIRECTORY"
python replacement2star.py "$CORPUS_DIRECTORY" "$OUTPUT_DIRECTORY" "$PHONE_MAPPING_FILE" "$ORIGIN_PRON_DICT_FILE"
