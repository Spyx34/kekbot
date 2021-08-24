roles = ctx.guild.roles
roles_better = ctx.guild.roles.split(",")
roles_better.pop("<")
roles_better.pop(">")


