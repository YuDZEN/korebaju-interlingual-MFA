import os
import subprocess
import shutil

subprocess.run(["python", "clean.py"])

CORPUS_DIRECTORY = "./corpus/"
PHONE_MAPPING_FILE = "./phoneMapping.txt"
ORIGIN_PRON_DICT_FILE = "./output.txt"
INTER_PRON_DICT_FILE = "./inter_pron_dict.txt"
OUTPUT_DIRECTORY = "./output"

# Run star2replacement.py
subprocess.run(["python", "star2replacement.py", CORPUS_DIRECTORY, PHONE_MAPPING_FILE, ORIGIN_PRON_DICT_FILE])

# Check if INTER_PRON_DICT_FILE exists or PHONE_MAPPING_FILE is newer
subprocess.run(["python", "convertPronDict.py", ORIGIN_PRON_DICT_FILE, PHONE_MAPPING_FILE, INTER_PRON_DICT_FILE])

# Create output directory if not exists
if not os.path.exists(OUTPUT_DIRECTORY):
    os.makedirs(OUTPUT_DIRECTORY)

# Run MFA validation and alignment
subprocess.run(["mfa", "validate", "--single_speaker", "--num_jobs=4", CORPUS_DIRECTORY, INTER_PRON_DICT_FILE, "english_mfa.zip"])
subprocess.run(["mfa", "align", "--single_speaker", "--num_jobs=4", CORPUS_DIRECTORY, INTER_PRON_DICT_FILE, "english_mfa.zip", OUTPUT_DIRECTORY])
# Install tgt library
subprocess.run(["pip", "install", "tgt"])
# Convert the alignment result
subprocess.run(["python", "convertAlignments.py", "wordTranscriptions.pkl", OUTPUT_DIRECTORY])
subprocess.run(["python", "replacement2star.py", CORPUS_DIRECTORY, OUTPUT_DIRECTORY, PHONE_MAPPING_FILE, ORIGIN_PRON_DICT_FILE])
