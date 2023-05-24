import pygame
import os


WIDTH, HEIGHT = 760,760

ROWS, COLS = 8,8

SQUARE = WIDTH//ROWS

BOARD = 640

FPS = 60

golosFontBlack = "assets/font/GOLOS/GolosText-Black.ttf"
golosFontRegular = "assets/font/GOLOS/GolosText-Regular.ttf"

fontTitleSize = 30
fontSize = 20


# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected


blackKnight = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pieces", "bkn.png")), (SQUARE, SQUARE))
blackBishop = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pieces", "bb.png")), (SQUARE, SQUARE))
blackKing = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pieces", "bk.png")), (SQUARE, SQUARE))
blackPawn = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pieces", "bp.png")), (SQUARE, SQUARE))
blackQueen = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pieces", "bq.png")), (SQUARE, SQUARE))
blackRook = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pieces", "br.png")), (SQUARE, SQUARE))

whiteKnight = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pieces", "wkn.png")), (SQUARE, SQUARE))
whiteBishop = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pieces", "wb.png")), (SQUARE, SQUARE))
whiteKing = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pieces", "wk.png")), (SQUARE, SQUARE))
whitePawn = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pieces", "wp.png")), (SQUARE, SQUARE))
whiteQueen = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pieces", "wq.png")), (SQUARE, SQUARE))
whiteRook = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pieces", "wr.png")), (SQUARE, SQUARE))


""" whiteImages = [whitePawn, whiteQueen, whiteKing, whiteKnight, whiteRook, whiteBishop]
smallWhiteImages = [whitePawnSmall, whiteQueenSmall, whiteKingSmall, whiteKnightSmall, whiteRookSmall, whiteBishopSmall]

blackImages = [blackPawn, blackQueen, blackKing, blackKnight, blackRook, blackBishop]
smallBlackImages = [blackPawnSmall, blackQueenSmall, blackKingSmall, blackKnightSmall, blackRookSmall, blackBishopSmall]

pieceList = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop'] """






