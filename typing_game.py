import pygame
import random
import time

# Pygameの初期化
pygame.init()

# 画面サイズ設定
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("タイピングゲーム")

# フォント設定
FONT = pygame.font.Font(None, 50)

# 単語リスト
words = ["python", "programming", "developer", "keyboard", "challenge", "speed", "accuracy"]

# 初期設定
current_word = random.choice(words)
input_text = ""
score = 0
start_time = time.time()
time_limit = 30  # 制限時間（秒）

# ゲームループ
running = True
while running:
    screen.fill((30, 30, 30))  # 背景色
    elapsed_time = int(time.time() - start_time)

    # 終了条件
    if elapsed_time > time_limit:
        running = False

    # テキスト描画
    word_surface = FONT.render(f"Word: {current_word}", True, (255, 255, 255))
    input_surface = FONT.render(f"Your Input: {input_text}", True, (100, 200, 255))
    score_surface = FONT.render(f"Score: {score}", True, (255, 255, 0))
    time_surface = FONT.render(f"Time: {time_limit - elapsed_time}s", True, (255, 100, 100))

    screen.blit(word_surface, (50, 50))
    screen.blit(input_surface, (50, 120))
    screen.blit(score_surface, (50, 190))
    screen.blit(time_surface, (50, 260))

    pygame.display.flip()

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text == current_word:
                    score += 1
                    current_word = random.choice(words)
                    input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

pygame.quit()

print(f"ゲーム終了！スコア: {score}")