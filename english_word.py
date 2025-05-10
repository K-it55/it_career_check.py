import csv
import random

CSV_FILE = "vocabulary.csv"

def load_words():
    """CSVから単語リストを読み込む"""
    try:
        with open(CSV_FILE, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_words(words):
    """単語リストをCSVに保存"""
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ["word", "meaning", "example", "correct", "incorrect"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(words)

def add_word():
    """新しい単語を追加"""
    word = input("英単語: ")
    meaning = input("意味: ")
    example = input("例文: ")
    words = load_words()
    words.append({"word": word, "meaning": meaning, "example": example, "correct": "0", "incorrect": "0"})
    save_words(words)
    print(f"単語 '{word}' を追加しました！")

def search_word():
    """単語を検索"""
    query = input("検索する単語: ")
    words = load_words()
    for word in words:
        if word['word'] == query:
            print(f"単語: {word['word']}, 意味: {word['meaning']}, 例文: {word['example']}, 正解: {word['correct']}, 不正解: {word['incorrect']}")
            return
    print("単語が見つかりませんでした。")

def edit_word():
    """単語を編集"""
    query = input("編集する単語: ")
    words = load_words()
    for word in words:
        if word['word'] == query:
            word['meaning'] = input(f"新しい意味 ({word['meaning']}): ") or word['meaning']
            word['example'] = input(f"新しい例文 ({word['example']}): ") or word['example']
            save_words(words)
            print(f"単語 '{query}' を更新しました！")
            return
    print("単語が見つかりませんでした。")

def delete_word():
    """単語を削除"""
    query = input("削除する単語: ")
    words = load_words()
    words = [word for word in words if word['word'] != query]
    save_words(words)
    print(f"単語 '{query}' を削除しました！")

def quiz():
    """ランダムに単語を出題し、正誤を記録"""
    words = load_words()
    if not words:
        print("単語が登録されていません。")
        return
    question = random.choice(words)
    print(f"単語: {question['word']}")
    answer = input("意味を入力: ")
    if answer == question['meaning']:
        print("正解！")
        question['correct'] = str(int(question['correct']) + 1)
    else:
        print(f"不正解。正しい意味: {question['meaning']}")
        question['incorrect'] = str(int(question['incorrect']) + 1)
    save_words(words)

def main():
    """メインメニュー"""
    while True:
        print("\n英単語学習システム")
        print("1. 単語を追加")
        print("2. 単語を検索")
        print("3. 単語を編集")
        print("4. 単語を削除")
        print("5. テスト")
        print("6. 終了")
        choice = input("選択: ")
        if choice == "1":
            add_word()
        elif choice == "2":
            search_word()
        elif choice == "3":
            edit_word()
        elif choice == "4":
            delete_word()
        elif choice == "5":
            quiz()
        elif choice == "6":
            print("終了します。")
            break
        else:
            print("無効な入力です。")

if __name__ == "__main__":
    main()
