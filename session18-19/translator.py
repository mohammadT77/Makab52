import argparse, translators

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Translator project')

    parser.add_argument('file_path', nargs='?', action='store', default=None,
                        help='file path to translate (empty for interactive shell)')
    parser.add_argument('-t', '--to_lang', metavar='TO_LANG', action='store', required=True,
                        help='select destination language')
    parser.add_argument('-f', '--from_lang', metavar='FROM_LANG', action='store', default='auto',
                        help='select origin language')
    parser.add_argument('-p', '--provider', metavar='PROVIDER', action='store', default='google',
                        choices=['alibaba', 'baidu', 'bing', 'deepl', 'google', 'sogou', 'tencent', 'yandex', 'youdao'],
                        help='select provider')
    parser.add_argument('-s', '--save', metavar='SAVE_PATH', action='store', default=None,
                        help='select a path to save the result (optional)')

    args = parser.parse_args()

    if not args.file_path:
        text = ""
        try:
            while True:
                text += input(': ') + '\n'
        except KeyboardInterrupt:
            res = getattr(translators, args.provider)(text, to_language=args.to_lang, from_language=args.from_lang)
    else:
        with open(args.file_path) as f:
            text = f.read()
            res = getattr(translators, args.provider)(text, to_language=args.to_lang, from_language=args.from_lang)

    if args.save:
        with open(args.save, 'w') as f:
            f.write(res)
        print('Result saved:', args.save)
    else:
        print(res)
