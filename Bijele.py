pieces = input().split()

print('{king} {queen} {rook} {bishop} {knight} {pawn}'.format(king = 1 - int(pieces[0]), queen = 1 - int(pieces[1]), 
rook = 2 - int(pieces[2]), bishop = 2 - int(pieces[3]), knight = 2 - int(pieces[4]), pawn = 8 - int(pieces[5])))

