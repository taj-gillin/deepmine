execute at @e[tag=deepmine.number_board] run function deepmine:entity/read
function deepmine:call
tellraw @a [{"text": "Pred: "}, {"score": {"name": "output", "objective": "deepmine.vars"}}]