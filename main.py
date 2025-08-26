import pygame
import chess
import chess.engine
import sys

# --- 参数设置 ---
BOARD_SIZE = 600
SQUARE_SIZE = BOARD_SIZE // 8
FPS = 30

# 棋子图片
PIECE_IMAGES = {}

def load_images():
    pieces = ["P","N","B","R","Q","K","p","n","b","r","q","k"]
    for p in pieces:
        PIECE_IMAGES[p] = pygame.transform.scale(
            pygame.image.load(f"pieces/{p}.png"), (SQUARE_SIZE, SQUARE_SIZE)
        )

def draw_board(screen, board, selected_square=None):
    colors = [pygame.Color(235, 236, 208), pygame.Color(119, 149, 86)]
    for r in range(8):
        for c in range(8):
            color = colors[(r+c)%2]
            rect = pygame.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect)

            square = chess.square(c, 7-r)
            piece = board.piece_at(square)
            if piece:
                screen.blit(PIECE_IMAGES[piece.symbol()], rect.topleft)

    # 高亮选中
    if selected_square is not None:
        r, c = 7 - chess.square_rank(selected_square), chess.square_file(selected_square)
        highlight = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        highlight.set_alpha(100)
        highlight.fill(pygame.Color("yellow"))
        screen.blit(highlight, (c*SQUARE_SIZE, r*SQUARE_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
    pygame.display.set_caption("国际象棋")
    clock = pygame.time.Clock()

    # 加载棋子图片
    load_images()

    # 初始化棋盘和引擎
    board = chess.Board()
    try:
        engine = chess.engine.SimpleEngine.popen_uci("stockfish")
    except FileNotFoundError:
        print("⚠️ 未找到 stockfish，请安装并确保可执行。")
        sys.exit(1)

    selected_square = None
    running = True
    player_turn = True  # 轮到玩家

    while running:
        draw_board(screen, board, selected_square)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if player_turn and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                c, r = x // SQUARE_SIZE, y // SQUARE_SIZE
                square = chess.square(c, 7-r)

                if selected_square is None:
                    # 第一次点击，选择棋子
                    piece = board.piece_at(square)
                    if piece and piece.color == board.turn:
                        selected_square = square
                else:
                    # 第二次点击，尝试走子
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        board.push(move)
                        player_turn = False
                    selected_square = None

        # 电脑走棋
        if not player_turn and not board.is_game_over():
            result = engine.play(board, chess.engine.Limit(time=0.5))
            board.push(result.move)
            player_turn = True

        clock.tick(FPS)

    engine.quit()
    pygame.quit()

if __name__ == "__main__":
    main()