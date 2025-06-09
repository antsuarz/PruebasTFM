import os
import csv

VIDEO_DATA = "./csv_outputs"
SURVEY_DATA = "./survey_data"
AU_COLUMNS = [
    "AU01", "AU02", "AU04", "AU05", "AU06", "AU07", "AU09", "AU10",
    "AU11", "AU12", "AU14", "AU15", "AU17", "AU20", "AU21", "AU23",
    "AU24", "AU26", "AU28", "AU43"
]

SURVEY_COLUMNS  = ['birth', 'gender'] + [f'q{i}' for i in range(1, 19)]

def parse_lines(filepath):
    with open(filepath, 'r', newline='', encoding='utf-8') as f:
        return list(csv.reader(f))


def extract_id(filename):
    if "-" in filename:
        return filename.split("-")[0]
    else:
        return os.path.splitext(filename)[0]


def write_csv(output_path, header, rows):
    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)


def process_au_csv():
    au_rows = []
    for file in os.listdir(VIDEO_DATA):
        if file.endswith(".csv"):
            full_path = os.path.join(VIDEO_DATA, file)
            id_value = extract_id(file)
            lines = parse_lines(full_path)
            row = [id_value]
            for i in range(1, len(AU_COLUMNS) + 1):
                row.append(lines[i][1])
            au_rows.append(row)
    return au_rows


def process_survey_csv():
    survey_rows = []
    for file in os.listdir(SURVEY_DATA):
        if file.endswith(".csv"):
            full_path = os.path.join(SURVEY_DATA, file)
            id_value = extract_id(file)
            lines = parse_lines(full_path)
            row = [id_value]
            for line in lines:
                if len(line) == 2:
                    row.append(line[1])
            survey_rows.append(row)
    return survey_rows


write_csv(os.path.join("./", "au_final.csv"), ["ID"] + AU_COLUMNS, process_au_csv())
write_csv(os.path.join("./", "survey_final.csv"), ["ID"] + SURVEY_COLUMNS, process_survey_csv())