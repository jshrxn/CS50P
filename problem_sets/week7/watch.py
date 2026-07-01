import re

def main():
    result = parse(input("HTML: "))
    if result:
        print(result)
    else:
        return None

def parse(s):

    pattern = r'<iframe[^>]*src=["\']((?:https?://)?(?:www\.)?(?:youtube\.com/(?:embed|v|shorts)/|youtu\.be/)[a-zA-Z0-9_-]{11}[^"\']*)["\']'

    matches = re.findall(pattern, s)

    if matches:
        url = matches[0]
        id_match = re.search(r'(?:youtube\.com/(?:embed|v|shorts)/|youtu\.be/)([a-zA-Z0-9_-]{11})', url)

        if id_match:
            video_id = id_match.group(1)
            return f"https://youtu.be/{video_id}"

    return None

if __name__ == "__main__":
    main()
