import json
import os
import re

def extract_metadata(md_directory):
    metadata_list = []
    for filename in os.listdir(md_directory):
        if filename.endswith(".md"):
            file_path = os.path.join(md_directory, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as md_file:
                    content = md_file.read()

                # Search for the YAML block at the beginning of the file
                match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)

                if match:
                    yaml_block = match.group(1)
                    metadata = {}
                    for line in yaml_block.splitlines():
                        if ":" in line:
                            key, value = line.split(":", 1)
                            key = key.strip()
                            value = value.strip().strip('"')  # Remove quotes around the value
                            metadata[key] = value
                    metadata['link'] = filename[:-3]  # Remove '.md' extension
                    metadata_list.append(metadata)

            except Exception as e:
                print(f"Error processing {filename}: {e}")

    return metadata_list

def sort_by_date(metadata_list):
    """Sort the metadata list by date (most recent to least recent)."""
    return sorted(metadata_list, key=lambda x: x.get('date', ''), reverse=True)

def save_to_json(metadata_list, json_file):
    data = {"posts": metadata_list}
    try:
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Metadata saved to {json_file}")
    except Exception as e:
        print(f"Error saving to {json_file}: {e}")

if __name__ == "__main__":
    # Directories of the files
    md_directory = './docs/blog/posts'
    json_file = './docs/en/blog/posts.json' 
    md_directory_es = './docs/es/blog/posts'
    json_file_es = './docs/es/blog/posts.json' 
    metadata = extract_metadata(md_directory)
    metadata_es = extract_metadata(md_directory_es)
    sorted_metadata = sort_by_date(metadata) 
    sorted_metadata_es = sort_by_date(metadata_es) 
    save_to_json(sorted_metadata, json_file)
    save_to_json(sorted_metadata_es, json_file_es)


