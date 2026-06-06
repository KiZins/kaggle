import csv
import json
import os

def convert_csv_to_jsonl(csv_path, jsonl_cate_path, output_path):
    # Load categories into a dictionary
    categories_by_id = {}
    
    if os.path.exists(jsonl_cate_path):
        with open(jsonl_cate_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    data = json.loads(line)
                    row_id = str(data.get('id'))
                    categories_by_id[row_id] = data.get('category', 'unknown')
    else:
        print(warning:= f"Warning: {jsonl_cate_path} not found. Proceeding without categories.")

    # Read CSV and write to the final JSONL file
    count = 0
    with open(csv_path, 'r', encoding='utf-8') as csv_file, \
         open(output_path, 'w', encoding='utf-8') as jsonl_file:
        
        reader = csv.DictReader(csv_file)
        
        for row in reader:
            row_id = str(row.get('id'))
            
            # Create the structured JSON object
            json_record = {
                "id": row.get('id'),
                "prompt": row.get('prompt'),
                "answer": row.get('answer'),
                "category": categories_by_id.get(row_id, "unknown") 
            }
            
            # Write as a single line in the JSONL file
            jsonl_file.write(json.dumps(json_record, ensure_ascii=False) + '\n')
            count += 1
            
    print(f"Success! Processed {count} rows and saved to {output_path}")

if __name__ == "__main__":
    CSV_INPUT = "../../data/raw/train.csv"
    JSONL_CATE = "../../data/raw/categories.jsonl"
    JSONL_OUTPUT = "../../data/raw/train_processed.jsonl"
    
    convert_csv_to_jsonl(CSV_INPUT, JSONL_CATE, JSONL_OUTPUT)