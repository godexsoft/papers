import os
import sys

def generate_index(directory):
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' not found.", file=sys.stderr)
        sys.exit(1)

    html_files = [f for f in os.listdir(directory) if f.endswith('.html') and f != 'index.html']
    html_files.sort()

    index_path = os.path.join(directory, 'index.html')

    with open(index_path, 'w') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html lang="en">\n')
        f.write('<head>\n')
        f.write('  <meta charset="UTF-8">\n')
        f.write('  <title>Papers Index</title>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('  <h1>Papers</h1>\n')
        f.write('  <ul>\n')

        for html_file in html_files:
            link_text = os.path.splitext(html_file)[0].replace('_', ' ').replace('-', ' ')
            f.write(f'    <li><a href="{html_file}">{link_text}</a></li>\n')

        f.write('  </ul>\n')
        f.write('</body>\n')
        f.write('</html>\n')

    print(f"Successfully generated '{index_path}'")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_index.py <directory>", file=sys.stderr)
        sys.exit(1)

    build_dir = sys.argv[1]
    generate_index(build_dir)
