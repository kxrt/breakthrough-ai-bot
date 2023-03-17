import discord
import ai.utils
from localgame import Game

TOKEN="YOUR_TOKEN_HERE"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

game = None

@client.event
async def on_ready():
  print("{0.user} is ready!".format(client))

@client.event
async def on_message(message):
  global game
  if message.author == client.user:
    return
  
  elif message.content.startswith("!!"):
    # Create a new game
    if message.content.startswith("!!new"):
      game = Game()
      await message.channel.send("New game started!")
      await message.channel.send(game.print_state())
      # Make initial move (AI)
      await message.channel.send("AI's turn!")
      game.play_AI()
      await message.channel.send(game.print_state())
      await message.channel.send("It's your turn!")
    # Make a move (human)
    elif message.content.startswith("!!move"):
      # Check if game is in progress
      if game == None:
        await message.channel.send("No game in progress!")
      else:
        # Check input validity
        move = message.content[6:].split(" ")[1:]
        if len(move) != 4:
          await message.channel.send("Invalid move!")
        else:
          # Execute move
          src = (int(move[0]), int(move[1]))
          dst = (int(move[2]), int(move[3]))
          res = game.play(src, dst)
          # Check move validity
          if res == "Invalid move!":
            await message.channel.send(res + " Try again.")
          else:
            await message.channel.send(res)
            # Check game state
            if game.is_over():
              await message.channel.send("Game over!")
              game = None
            else:
              # Make a move (AI)
              await message.channel.send("AI's turn!")
              game.play_AI()
              await message.channel.send(game.print_state())
              # Check game state
              if game.is_over():
                await message.channel.send("Game over!")
                game = None
              else: await message.channel.send("It's your turn!")

client.run(TOKEN)