scoreboard players operation max_val deepmine.vars = logits[0] deepmine.vars

scoreboard players operation max_val deepmine.vars > logits[1] deepmine.vars
scoreboard players operation max_val deepmine.vars > logits[2] deepmine.vars
scoreboard players operation max_val deepmine.vars > logits[3] deepmine.vars
scoreboard players operation max_val deepmine.vars > logits[4] deepmine.vars
scoreboard players operation max_val deepmine.vars > logits[5] deepmine.vars
scoreboard players operation max_val deepmine.vars > logits[6] deepmine.vars
scoreboard players operation max_val deepmine.vars > logits[7] deepmine.vars
scoreboard players operation max_val deepmine.vars > logits[8] deepmine.vars
scoreboard players operation max_val deepmine.vars > logits[9] deepmine.vars

execute if score logits[0] deepmine.vars = max_val deepmine.vars run scoreboard players set output deepmine.vars 0
execute if score logits[1] deepmine.vars = max_val deepmine.vars run scoreboard players set output deepmine.vars 1
execute if score logits[2] deepmine.vars = max_val deepmine.vars run scoreboard players set output deepmine.vars 2
execute if score logits[3] deepmine.vars = max_val deepmine.vars run scoreboard players set output deepmine.vars 3
execute if score logits[4] deepmine.vars = max_val deepmine.vars run scoreboard players set output deepmine.vars 4
execute if score logits[5] deepmine.vars = max_val deepmine.vars run scoreboard players set output deepmine.vars 5
execute if score logits[6] deepmine.vars = max_val deepmine.vars run scoreboard players set output deepmine.vars 6
execute if score logits[7] deepmine.vars = max_val deepmine.vars run scoreboard players set output deepmine.vars 7
execute if score logits[8] deepmine.vars = max_val deepmine.vars run scoreboard players set output deepmine.vars 8
execute if score logits[9] deepmine.vars = max_val deepmine.vars run scoreboard players set output deepmine.vars 9
