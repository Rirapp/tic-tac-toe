#--the first projec of my entire life--
#Credits to whoever made this
# board here 
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

# the game is over yet?
game_still_going = True

#yang menang siape?
winner = None 

# yang jalan duluan
current_player = "X"

#----HERE WE GO----

# play the game nih  
def play_game():
  
  #biar board nya nongol 
  display_board()

  #loop sampe game abis
  while game_still_going:

    #handle the giliran
    handle_turn(current_player)

    #the game is over yet? take 2 
    check_if_game_over()

    #gantian giliran 
    flip_player()

  #pas game over, print menang ato Seri 
    if winner == "X" or winner =="O":
      print (winner +" won .")
    elif winner == None:
      print ("Tie.")

#biar board nya nongol take 2
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


#yang ngatur giliran player 
def handle_turn(player):

  #get posisi player 
  print(player + "'s turn.")
  position = input("Pilih posisi dari 1-9:")
  
  #biar input user gk salah
  valid = False
  while not valid:

    #make sure the input itu valid
    while position not in ["1", "2", "3", "4", "5", "6", "7","8", "9",]:
     position = input ("Pilih posisi dari 1-9:")

    #get correct index di board list
    position = int(position) - 1 

    #make sure the spot di board kosong 
    if board[position] == "-":
      valid = True
    else:
      print("tidak bisa kesana gan.")

  #put the game piece on the board eh
  board[position] = player

  #biar board nya nongol take 3 
  display_board()

#the game is over yet? take 3
def check_if_game_over():
  check_for_winner()
  check_for_tie()

#check if somebody ada yg menang 
def check_for_winner():
  #set variabel global
  global winner 
  #check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = Check_diagonals()
  #HERE THE WINNER 
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None

#check rows for a win
def check_rows():
  #set variabel global take 2 
  global game_still_going
  #check any of the rows have value yang sama gk kosong 
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  #jika any rows does have a match maka flag buat pemenang 
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner 
  if row_1:
    return board[0]
  elif row_2 :
    return board[3]
  elif row_3 :
    return board[6]
  #atau return none if there wa no winner chicken dinner 
  else:
    return None

#check column for winner 
def check_columns():
  #global variabel
  global game_still_going
  #check any of the rows have value yang sama gk kosong take 2
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  #jika any rows does have a match maka flag buat pemenang take 2  
  if column_1:
    return board[0] 
  elif column_2:
    return board[3] 
  elif column_3:
    return board[6] 
  #atau return none if there was no winner
  else:
   return None
  
#check diagonals winner 
def Check_diagonals():
  #global variabel
  global game_still_going
  #check if any of the column  yang sama gk kosong 
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  #jika any rows does have a match maka flag buat pemenang take 3
  if diagonal_1 or diagonal_2:
    game_still_going = False
  #return the winner
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  #or return none if the was no booyah
  else:
    return None

#check klo seri 
def check_for_tie():
  #global variabel 
  global game_still_going
  #if board is penuh 
  if "-" not in board:
    game_still_going = false 
    return True
  #else there is no seri
  else:
    return False

#flip player dari X ke O or O ke X
def flip_player():
  # variabel global
  global current_player
  # If the player X
  if current_player == "X":
    current_player = "O"
  # Or if the player O
  elif current_player == "O":
    current_player = "X"

#compile
#maen gamenya 
play_game()
  

