import random

def spin_reels():
  """Spins the three reels and returns a tuple of symbols."""
  symbols = ["Cherry", "Bell", "Orange", "Lemon", "Diamond", "Seven"]
  reel1 = random.choice(symbols)
  reel2 = random.choice(symbols)
  reel3 = random.choice(symbols)
  return reel1, reel2, reel3

def calculate_winnings(bet, reels):
  """Calculates the winnings based on matching symbols."""
  if reels[0] == reels[1] == reels[2]:
    if reels[0] == "Seven":
      return bet * 10
    elif reels[0] == "Diamond":
      return bet * 5
    else:
      return bet * 3
  elif reels[0] == reels[1] or reels[0] == reels[2] or reels[1] == reels[2]:
    return bet
  else:
    return 0

def play_slot_machine():
  """Simulates a slot machine game."""
  balance = 100  # Initial balance

  while balance > 0:
    print(f"Current Balance: ${balance}")
    bet = int(input("Enter your bet: "))
    if bet > balance:
      print("Insufficient funds.")
      continue

    reels = spin_reels()
    print(f"Reels: {reels[0]} {reels[1]} {reels[2]}")

    winnings = calculate_winnings(bet, reels)
    if winnings > 0:
      print(f"You won ${winnings}!")
    else:
      print("You lost.")

    balance -= bet
    balance += winnings

  print("Game Over! You are out of money.")

play_slot_machine()