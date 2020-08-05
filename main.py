birthdays = {
  'Kirk':'April 1',
  'John':'November 9',
  'Nick': 'February 29'
}

while True:
  name = input("Who's birthday do you want?(or blank to quit)")
  if name =="":
    break
  if name in birthdays:
    print(name+ "\'s birthday is "+birthdays[name])
  else:
    print("I dont have a birthday for", name)
    bday = input("Whats their birthday?")
    birthdays[name] = bday
    print(name+ "\'s birthday is "+birthdays[name])
    print(birthdays)
