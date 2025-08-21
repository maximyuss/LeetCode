import os, csv, re, shutil, hashlib, json
from datetime import datetime

BEGIN = '<!-- TABLE:BEGIN -->'
END = '<!-- TABLE:END -->'
LANG_ORDER = {'C++': 0, 'Python': 1, 'Java': 2}

EXT_TO_FOLDER = {
    'py': 'python',
    'cpp': 'cpp',
    'cc': 'cpp',
    'cxx': 'cpp',
    'java': 'java',
    'js': 'javascript',
    'ts': 'typescript',
    'go': 'go',
    'rs': 'rust',
    'kt': 'kotlin',
    'c': 'c',
    'cs': 'csharp',
    'swift': 'swift',
    'php': 'php',
    'rb': 'ruby',
    'scala': 'scala'
}
EXT_TO_LABEL = {
    'py': 'Python',
    'cpp': 'C++',
    'cc': 'C++',
    'cxx': 'C++',
    'java': 'Java',
    'js': 'JavaScript',
    'ts': 'TypeScript',
    'go': 'Go',
    'rs': 'Rust',
    'kt': 'Kotlin',
    'c': 'C',
    'cs': 'C#',
    'swift': 'Swift',
    'php': 'PHP',
    'rb': 'Ruby',
    'scala': 'Scala'
}


def get_paths():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data = os.path.join(root, 'import')
    return {
        'root': root,
        'data': data,
        'new': os.path.join(data, 'new'),
        'code': os.path.join(root, 'code'),
        'csv': os.path.join(data, 'problems.csv'),
        'leetcode_json': os.path.join(data, 'leetcode.json'),
        'md0': os.path.join(root, 'README.md'),
        'md1': os.path.join(root, '1000-1999.md'),
        'md2': os.path.join(root, '2000-3999.md'),
        'log': os.path.join(data, 'errors.log'),
    }


def ensure_data_dirs(paths):
    os.makedirs(paths['data'], exist_ok=True)
    os.makedirs(paths['new'], exist_ok=True)


def log_error(paths, problem_id, err):
    os.makedirs(os.path.dirname(paths['log']), exist_ok=True)
    with open(paths['log'], 'a', encoding='utf-8') as f:
        t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'[{t}] id={problem_id}: {err}\n')


def load_queue(csv_path):
    out = []
    if not os.path.exists(csv_path):
        return out
    with open(csv_path, newline='', encoding='utf-8') as f:
        rdr = csv.reader(f)
        for row in rdr:
            if not row:
                continue
            first = str(row[0]).strip()
            if first.isdigit():
                tags = row[1].strip() if len(row) > 1 else ''
                out.append((int(first), tags))
    return out


def save_queue(csv_path, items):
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        for pid, tags in items:
            w.writerow([pid, tags])


def file_digest(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def move_files_for_problem(problem_id, paths):
    found = []
    new_dir = paths['new']
    if not os.path.isdir(new_dir):
        return found
    for name in os.listdir(new_dir):
        if not name.startswith(str(problem_id) + '.'):
            continue
        src = os.path.join(new_dir, name)
        if not os.path.isfile(src):
            continue
        ext = name.rsplit('.', 1)[1].lower()
        folder = EXT_TO_FOLDER.get(ext, ext)
        dest_dir = os.path.join(paths['code'], folder)
        os.makedirs(dest_dir, exist_ok=True)
        dest = os.path.join(dest_dir, name)
        try:
            if os.path.exists(dest) and file_digest(src) == file_digest(dest):
                os.remove(src)
            else:
                shutil.move(src, dest)
            label = EXT_TO_LABEL.get(ext, ext.upper())
            rel = f'/code/{folder}/{name}'
            found.append((label, rel))
        except Exception as e:
            log_error(paths, problem_id, f'move error: {e}')
    return found


def scan_existing_solutions(problem_id, code_root):
    found = []
    if not os.path.isdir(code_root):
        return found
    for lang_dir in os.listdir(code_root):
        lang_path = os.path.join(code_root, lang_dir)
        if not os.path.isdir(lang_path):
            continue
        for name in os.listdir(lang_path):
            if name.startswith(str(problem_id) + '.'):
                ext = name.rsplit('.', 1)[1].lower()
                label = EXT_TO_LABEL.get(ext, ext.upper())
                rel = f'/code/{lang_dir}/{name}'
                found.append((label, rel))
    return found


def load_leetcode_index(paths):
    try:
        with open(paths['leetcode_json'], 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception:
        return {}
    out = {}
    pairs = data.get('stat_status_pairs', []) if isinstance(data, dict) else []
    for it in pairs:
        st = it.get('stat') or {}
        pid = st.get('frontend_question_id')
        if not isinstance(pid, int):
            continue
        slug = st.get('question__title_slug', '')
        lvl = (it.get('difficulty') or {}).get('level')
        diff = {1: 'Easy', 2: 'Medium', 3: 'Hard'}.get(lvl, '')
        out[pid] = {
            'title': st.get('question__title', '') or f'Problem {pid}',
            'url': f'https://leetcode.com/problems/{slug}/' if slug else '',
            'difficulty': diff,
        }
    return out


def select_target_md(problem_id, paths):
    if 0 <= problem_id <= 999:
        return paths['md0']
    if 1000 <= problem_id <= 1999:
        return paths['md1']
    return paths['md2']


def build_row(problem_id, info, solutions, tags):
    title = info.get('title') or f'Problem {problem_id}'
    url = info.get('url') or ''
    difficulty = info.get('difficulty') or ''
    title_html = f'<a href="{url}">{title}</a>' if url else title
    sols_html = '&nbsp;'.join(f'<a href="{p}">{lbl}</a>' for lbl, p in solutions)
    return f'| {problem_id} | {title_html} | {sols_html} | {difficulty} | {tags} |'


def insert_or_update_row(md_path, problem_id, new_row):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    a = text.find(BEGIN)
    b = text.find(END, a + len(BEGIN))
    if a == -1 or b == -1:
        return False
    block = text[a + len(BEGIN):b]
    lines = [ln for ln in block.strip().splitlines() if ln.strip()]
    if len(lines) < 2:
        return False
    header1, header2 = lines[0], lines[1]
    data_rows = lines[2:]
    pairs = []
    for r in data_rows:
        m = re.match(r'^\|\s*(\d+)\s*\|', r)
        if m:
            pairs.append((int(m.group(1)), r))
    for i, (pid, _) in enumerate(pairs):
        if pid == problem_id:
            pairs[i] = (pid, new_row)
            break
    else:
        pairs.append((problem_id, new_row))
    pairs.sort(key=lambda x: x[0])
    new_block = '\n'.join([header1, header2] + [r for _, r in pairs])
    new_text = text[:a] + BEGIN + '\n\n' + new_block + '\n' + END + text[b + len(END):]
    if new_text != text:
        with open(md_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(new_text)
    return True


def main():
    paths = get_paths()
    ensure_data_dirs(paths)
    index = load_leetcode_index(paths)
    queue = load_queue(paths['csv'])
    if not queue:
        return
    left = []
    for problem_id, tags in queue:
        info = index.get(problem_id)
        if not info:
            log_error(paths, problem_id, 'metadata not found')
            left.append((problem_id, tags))
            continue
        existing = scan_existing_solutions(problem_id, paths['code'])
        moved = move_files_for_problem(problem_id, paths)
        solutions = existing + moved
        if not solutions:
            log_error(paths, problem_id, 'no solution files found')
            left.append((problem_id, tags))
            continue
        uniq = []
        seen = set()
        for lbl, rel in solutions:
            key = (lbl, rel)
            if key not in seen:
                seen.add(key)
                uniq.append((lbl, rel))
        solutions = sorted(uniq, key=lambda x: (LANG_ORDER.get(x[0], 99), x[0]))
        try:
            md_path = select_target_md(problem_id, paths)
            row = build_row(problem_id, info, solutions, tags)
            if not insert_or_update_row(md_path, problem_id, row):
                log_error(paths, problem_id, 'insert or update failed')
                left.append((problem_id, tags))
        except Exception as e:
            log_error(paths, problem_id, f'insert error: {e}')
            left.append((problem_id, tags))
    if left != queue:
        save_queue(paths['csv'], left)


if __name__ == '__main__':
    main()
