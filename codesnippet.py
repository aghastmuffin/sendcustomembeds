if message.content == ('embed'):
#delete field messages after sent maybe
  await message.channel.send("(end with an 'e') (and finish with an f)")
  await message.channel.send('how many fields? ')
  times = ('{0.content}'.format(message))
  await message.channel.send("Field one: Title")
  field1 = ('{0.content}'.format(message))
    if 'e' in message.content:
      await message.channel.send('Detected! saved set to')
			await message.channel.send(field1)
	await message.channel.send('Field one: Middle')
 	field1mid = ('{0.content}'.format(message))
	if 'e' in message.content:
		await message.channel.send('Detected! saved set to')
		await message.channel.send(field1mid)
  await message.channel.send("Field two: Title")
	field2 = ('{0.content}'.format(message))
	if 'e' in message.content:
		await message.channel.send('Detected! saved set to')
		await message.channel.send(field2)
	await message.channel.send('Field two: Middle')
  field2mid = ('{0.content}'.format(message))
  if 'e' in message.content:
  	await message.channel.send('Detected! saved set to')
    await message.channel.send(field2mid)
	def newembed(name1, value1):
  	embedVar.add_field(name=name1, value=value1, inline=True)
    embedVar = discord.Embed(title='custom embed by {0.author}'.format(message))
    newembed(field1, field1mid)
    newembed(field2, field2mid)
    await message.channel.send(embedVar)
client = MyClient()
client.run('#########################################################')
